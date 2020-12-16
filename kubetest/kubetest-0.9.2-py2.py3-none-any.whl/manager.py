"""Kubetest manager for test client instances and namespace management."""

import logging
from typing import Generator, List, Union

import kubernetes

from kubetest import client, objects, utils

log = logging.getLogger('kubetest')


class ObjectManager:
    """ObjectManager is a convenience class used to manage Kubernetes API
    objects that are registered with a test case.

    The core usage of the ObjectManager is to sort each of the registered
    objects into different buckets by type. An "apply order" is also
    defined here so we can get the bucketed objects in the order that they
    should be applied onto the cluster.

    This manager will only be used for API objects loaded from manifests
    that are specified by the `pytest.mark.applymanifests` marker on a
    test case by default.
    """

    # The ApiObject buckets in the order that that should be
    # applied when creating them on the cluster.
    ordered_buckets = [
        'namespace',
        'rolebinding',
        'clusterrolebinding',
        'secret',
        'networkpolicy',
        'service',
        'configmap',
        'persistentvolumeclaim',
        'ingress',
        'daemonset',
        'statefulset',
        'replicaset',
        'deployment',
        'pod',
    ]

    def __init__(self):
        # Add attributes with the bucket names to the instance.
        # By default they will all be empty lists. While this could
        # be done in a more readable way by explicitly setting the
        # buckets as members, e.g. self.pod = [], but by tying the
        # creation to the ordered_buckets list (which the other
        # instance methods use), adding and removing buckets means
        # only adding to the list, not updating in numerous locations.
        for bucket in self.ordered_buckets:
            self.__setattr__(bucket, [])

    def add(self, *args: objects.ApiObject) -> None:
        """Add API objects to the object manager.

        This method will take in any number of ApiObjects and sort them into the
        correct buckets. It will not check for duplicates. If a non-ApiObject is
        passed in, an error will be raised.

        Args:
            args: Any subclass of the kubetest ApiObject wrapping a Kubernetes
                API object.

        Raises:
            ValueError: One or more arguments passed to the function are not
                ApiObject subclasses.
        """
        for arg in args:
            if not isinstance(arg, objects.ApiObject):
                raise ValueError(
                    'Only ApiObject instances can be added to the ObjectManager, '
                    f'but was given: {arg}'
                )

            # Get the type name of the ApiObject wrapper and lower case it,
            # e.g. ClusterRoleBinding -> clusterrolebinding. This will be
            # used to compare to the buckets.
            name = type(arg).__name__.lower()

            # Check if we have a bucket for the name, if so, add it to the
            # bucket. If not, raise an error.
            if name in self.ordered_buckets:
                self.__getattribute__(name).append(arg)
            else:
                raise ValueError(f'Unable to determine bucket for ApiObject: {arg}')

    def get_objects_in_apply_order(self) -> Generator[objects.ApiObject, None, None]:
        """Get all of the managed objects in the order that they should be
        applied onto the cluster.

        Within the buckets themselves, API objects are not sorted. This function
        only yields the buckets in the correct order.

        Each of the buckets corresponds to an ApiObject wrapper that is supported
        by kubetest. As more ApiObject wrappers are added, the buckets here
        should be updated to reflect that.

        The bucket order in which objects are yielded are:
          - Namespace
          - RoleBinding
          - ClusterRoleBinding
          - Secret
          - NetworkPolicy
          - Service
          - ConfigMap
          - PersistentVolumeClaim
          - Ingress
          - DaemonSet
          - StatefulSet
          - ReplicaSet
          - Deployment
          - Pod

        Yields:
            The kubetest ApiObject wrapper to be created on the cluster.
        """
        for bucket in self.ordered_buckets:
            for obj in self.__getattribute__(bucket):
                yield obj


class TestMeta:
    """TestMeta holds information associated with a single test node.

    Args:
        name: The name of the test.
        node_id: The id of the test node.
        namespace_create: Option to create a new namespace. This can be toggled
            off in the event that a user is using an existing namespace on their
            test cluster.
        namespace_name: The name of the namespace to use. If the namespace is to
            be autogenerated, this can be left as None.
    """

    def __init__(
            self,
            name: str,
            node_id: str,
            namespace_create: bool = True,
            namespace_name: str = None,
    ) -> None:

        self.name = name
        self.node_id = node_id

        if namespace_name is None:
            self.ns = utils.new_namespace(name)
        else:
            self.ns = namespace_name

        # Flag to designate whether pytest setup (not TestMeta.setup) failed.
        # If pytest setup failed for the case, we can skip teardown, as there
        # will be nothing on the cluster itself.
        self._pt_setup_failed = False

        # lazy load
        self._client = None
        self._namespace = None

        self.namespace_create = namespace_create
        self.rolebindings = []
        self.clusterrolebindings = []

        self.test_objects = ObjectManager()

    @property
    def client(self) -> client.TestClient:
        """Get the TestClient for the test case."""
        if self._client is None:
            self._client = client.TestClient(self.ns)
        return self._client

    @property
    def namespace(self) -> objects.Namespace:
        """Get the Namespace API Object associated with the test case."""
        if self._namespace is None:
            self._namespace = objects.Namespace.new(self.ns)
        return self._namespace

    def setup(self) -> None:
        """Setup the cluster state for the test case.

        This performs all actions needed in order for the test client to be
        ready to use by a test case.
        """
        # create the test case namespace
        if self.namespace_create:
            self.namespace.create()

        # if there are any role bindings, create them.
        for rb in self.rolebindings:
            self.client.create(rb)

        # if there are any cluster role bindings, create them.
        for crb in self.clusterrolebindings:
            self.client.create(crb)

        # if any objects were registered with the test case via the
        # `applymanifests` marker, register them to the test client
        # and add them to the cluster now
        for obj in self.test_objects.get_objects_in_apply_order():
            self.client.create(obj)
            self.client.wait_until_created(obj, timeout=10, interval=0.5)
            self.client.pre_registered.append(obj)

    def teardown(self) -> None:
        """Clean up the cluster state for the given test case.

        This performs all actions needed in order to clean up the state that
        was previously set up for the test client in `setup`.
        """
        # Only perform teardown if pytest setup was successful and there is a
        # possibility of things existing on the cluster.
        if self._pt_setup_failed:
            log.info(
                f'pytest setup failed for {self.name}: not running test case teardown')
            return

        # Delete the test case namespace if we've created it.
        # This will also delete anything in the namespace, which includes RoleBindings.
        if self._namespace and self.namespace_create:
            self.namespace.delete()

        # ClusterRoleBindings are not bound to a namespace, so we will need
        # to delete them ourselves.
        for crb in self.clusterrolebindings:
            self.client.delete(crb)

    def yield_container_logs(self, tail_lines: int = None) -> Generator[str, None, None]:
        """Yield the container logs for the test case.

        These logs will be printed out if the test was in error to provide
        more context and make it easier to debug the issue.

        Args:
            tail_lines: The number of container log lines to print.

        Yields:
            str: Logs for the running containers on the cluster.
        """
        try:
            # prior to tearing down the namespace and cleaning up all of the
            # objects in the namespace, get the logs for the containers in the
            # namespace.
            pods_list = kubernetes.client.CoreV1Api().list_namespaced_pod(
                namespace=self.ns
            )
        except Exception as e:
            log.warning(
                f'Unable to get pods for namespace "{self.ns}" to cache logs ({e})',
            )
            return

        log_kwargs = {}
        if tail_lines is not None and tail_lines > 0:
            log_kwargs['tail_lines'] = tail_lines

        for pod in pods_list.items:
            for container in pod.spec.containers:
                pod_name = pod.metadata.name
                pod_ns = pod.metadata.namespace
                container_name = container.name
                try:
                    logs = kubernetes.client.CoreV1Api().read_namespaced_pod_log(
                        name=pod_name,
                        namespace=pod_ns,
                        container=container_name,
                        **log_kwargs,
                    )
                except Exception as e:
                    log.warning(
                        f'Unable to cache logs for {pod_name}::{container_name} ({e})',
                    )
                    continue

                if logs != '':
                    _id = f'=== {self.node_id} -> {pod_name}::{container_name} ==='
                    border = '=' * len(_id)
                    yield '\n'.join([border, _id, border, logs, '\n'])
        return

    def register_rolebindings(self, *rolebindings: objects.RoleBinding) -> None:
        """Register a RoleBinding requirement with the test case.

        Args:
            rolebindings: The RoleBindings that are needed for the test case.
        """
        self.rolebindings.extend(rolebindings)

    def register_clusterrolebindings(
            self,
            *clusterrolebindings: objects.ClusterRoleBinding,
    ) -> None:
        """Register a ClusterRoleBinding requirement with the test case.

        Args:
            clusterrolebindings: The ClusterRoleBindings that are needed for
                the test case.
        """
        self.clusterrolebindings.extend(clusterrolebindings)

    def register_objects(self, api_objects: List[objects.ApiObject]):
        """Register the provided objects with the test case.

        These objects will be registered to the test client and applied to the
        namespace on test setup.

        Args:
            api_objects: The wrapped Kubernetes API objects to create on the cluster.
        """
        self.test_objects.add(*api_objects)


class KubetestManager:
    """The manager for kubetest state.

    The KubetestManager is in charge of providing test clients for the tests
    that request them and mediating the namespace management corresponding to
    those test clients.
    """

    def __init__(self):

        # A dictionary mapping test node IDs to their corresponding TestMeta
        # object. Each test node will have a TestMeta created when the client
        # is created for the test node.
        self.nodes = {}

    def new_test(
            self,
            node_id: str,
            test_name: str,
            namespace_create: bool = True,
            namespace_name: str = None,
    ) -> TestMeta:
        """Create a new TestMeta for a test case.

        This will be called by the test setup hook in order to create a new
        TestMeta for the manager to keep track of.

        Args:
            node_id: The id of the test node.
            test_name: The name of the test.
            namespace_create: Option to create a new namespace. This can be toggled
                off in the event that a user is using an existing namespace on their
                test cluster.
            namespace_name: The name of the namespace to use. If the namespace is to
                be autogenerated, this can be left as None.

        Returns:
            The newly created TestMeta for the test case.
        """
        log.info(f'creating test meta for {node_id}')
        meta = TestMeta(
            node_id=node_id,
            name=test_name,
            namespace_create=namespace_create,
            namespace_name=namespace_name
        )

        self.nodes[node_id] = meta
        return meta

    def get_test(self, node_id: str) -> Union[TestMeta, None]:
        """Get the test metadata for the specified test node.

        Args:
            node_id: The id of the test node.

        Returns:
            The test metadata for the given node. If no test metadata is found
            for the given node, None is returned.
        """
        return self.nodes.get(node_id)

    def teardown(self, node_id: str) -> None:
        """Tear down the test case.

        This is effectively a wrapper around the `teardown` method of the
        test client. It will also remove the test client from the manager.

        Test client teardown will delete the test client's namespace from
        the cluster. Deleting a namespace will delete all the things in the
        namespace (e.g. API objects bound to the namespace).

        Args:
            node_id: The id of the test node.
        """
        test_case = self.nodes.get(node_id)
        if test_case is not None:
            test_case.teardown()
            del self.nodes[node_id]
