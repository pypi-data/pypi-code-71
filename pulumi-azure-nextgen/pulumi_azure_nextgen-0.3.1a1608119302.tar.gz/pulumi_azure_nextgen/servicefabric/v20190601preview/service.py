# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['Service']


class Service(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_name: Optional[pulumi.Input[str]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 correlation_scheme: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceCorrelationDescriptionArgs']]]]] = None,
                 default_move_cost: Optional[pulumi.Input[Union[str, 'MoveCost']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 partition_description: Optional[pulumi.Input[Union[pulumi.InputType['NamedPartitionSchemeDescriptionArgs'], pulumi.InputType['SingletonPartitionSchemeDescriptionArgs'], pulumi.InputType['UniformInt64RangePartitionSchemeDescriptionArgs']]]] = None,
                 placement_constraints: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_kind: Optional[pulumi.Input[Union[str, 'ServiceKind']]] = None,
                 service_load_metrics: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceLoadMetricDescriptionArgs']]]]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 service_package_activation_mode: Optional[pulumi.Input[Union[str, 'ArmServicePackageActivationMode']]] = None,
                 service_placement_policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServicePlacementPolicyDescriptionArgs']]]]] = None,
                 service_type_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        The service resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_name: The name of the application resource.
        :param pulumi.Input[str] cluster_name: The name of the cluster resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceCorrelationDescriptionArgs']]]] correlation_scheme: A list that describes the correlation of the service with other services.
        :param pulumi.Input[Union[str, 'MoveCost']] default_move_cost: Specifies the move cost for the service.
        :param pulumi.Input[str] location: It will be deprecated in New API, resource location depends on the parent resource.
        :param pulumi.Input[Union[pulumi.InputType['NamedPartitionSchemeDescriptionArgs'], pulumi.InputType['SingletonPartitionSchemeDescriptionArgs'], pulumi.InputType['UniformInt64RangePartitionSchemeDescriptionArgs']]] partition_description: Describes how the service is partitioned.
        :param pulumi.Input[str] placement_constraints: The placement constraints as a string. Placement constraints are boolean expressions on node properties and allow for restricting a service to particular nodes based on the service requirements. For example, to place a service on nodes where NodeType is blue specify the following: "NodeColor == blue)".
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Union[str, 'ServiceKind']] service_kind: The kind of service (Stateless or Stateful).
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceLoadMetricDescriptionArgs']]]] service_load_metrics: The service load metrics is given as an array of ServiceLoadMetricDescription objects.
        :param pulumi.Input[str] service_name: The name of the service resource in the format of {applicationName}~{serviceName}.
        :param pulumi.Input[Union[str, 'ArmServicePackageActivationMode']] service_package_activation_mode: The activation Mode of the service package
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServicePlacementPolicyDescriptionArgs']]]] service_placement_policies: A list that describes the correlation of the service with other services.
        :param pulumi.Input[str] service_type_name: The name of the service type
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Azure resource tags.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if application_name is None and not opts.urn:
                raise TypeError("Missing required property 'application_name'")
            __props__['application_name'] = application_name
            if cluster_name is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_name'")
            __props__['cluster_name'] = cluster_name
            __props__['correlation_scheme'] = correlation_scheme
            __props__['default_move_cost'] = default_move_cost
            __props__['location'] = location
            __props__['partition_description'] = partition_description
            __props__['placement_constraints'] = placement_constraints
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            if service_kind is None and not opts.urn:
                raise TypeError("Missing required property 'service_kind'")
            __props__['service_kind'] = service_kind
            __props__['service_load_metrics'] = service_load_metrics
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__['service_name'] = service_name
            __props__['service_package_activation_mode'] = service_package_activation_mode
            __props__['service_placement_policies'] = service_placement_policies
            __props__['service_type_name'] = service_type_name
            __props__['tags'] = tags
            __props__['etag'] = None
            __props__['name'] = None
            __props__['provisioning_state'] = None
            __props__['type'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:servicefabric/latest:Service"), pulumi.Alias(type_="azure-nextgen:servicefabric/v20170701preview:Service"), pulumi.Alias(type_="azure-nextgen:servicefabric/v20190301:Service"), pulumi.Alias(type_="azure-nextgen:servicefabric/v20190301preview:Service"), pulumi.Alias(type_="azure-nextgen:servicefabric/v20191101preview:Service"), pulumi.Alias(type_="azure-nextgen:servicefabric/v20200301:Service")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Service, __self__).__init__(
            'azure-nextgen:servicefabric/v20190601preview:Service',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Service':
        """
        Get an existing Service resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return Service(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="correlationScheme")
    def correlation_scheme(self) -> pulumi.Output[Optional[Sequence['outputs.ServiceCorrelationDescriptionResponse']]]:
        """
        A list that describes the correlation of the service with other services.
        """
        return pulumi.get(self, "correlation_scheme")

    @property
    @pulumi.getter(name="defaultMoveCost")
    def default_move_cost(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the move cost for the service.
        """
        return pulumi.get(self, "default_move_cost")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        Azure resource etag.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        It will be deprecated in New API, resource location depends on the parent resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Azure resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partitionDescription")
    def partition_description(self) -> pulumi.Output[Optional[Any]]:
        """
        Describes how the service is partitioned.
        """
        return pulumi.get(self, "partition_description")

    @property
    @pulumi.getter(name="placementConstraints")
    def placement_constraints(self) -> pulumi.Output[Optional[str]]:
        """
        The placement constraints as a string. Placement constraints are boolean expressions on node properties and allow for restricting a service to particular nodes based on the service requirements. For example, to place a service on nodes where NodeType is blue specify the following: "NodeColor == blue)".
        """
        return pulumi.get(self, "placement_constraints")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The current deployment or provisioning state, which only appears in the response
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="serviceKind")
    def service_kind(self) -> pulumi.Output[str]:
        """
        The kind of service (Stateless or Stateful).
        """
        return pulumi.get(self, "service_kind")

    @property
    @pulumi.getter(name="serviceLoadMetrics")
    def service_load_metrics(self) -> pulumi.Output[Optional[Sequence['outputs.ServiceLoadMetricDescriptionResponse']]]:
        """
        The service load metrics is given as an array of ServiceLoadMetricDescription objects.
        """
        return pulumi.get(self, "service_load_metrics")

    @property
    @pulumi.getter(name="servicePackageActivationMode")
    def service_package_activation_mode(self) -> pulumi.Output[Optional[str]]:
        """
        The activation Mode of the service package
        """
        return pulumi.get(self, "service_package_activation_mode")

    @property
    @pulumi.getter(name="servicePlacementPolicies")
    def service_placement_policies(self) -> pulumi.Output[Optional[Sequence['outputs.ServicePlacementPolicyDescriptionResponse']]]:
        """
        A list that describes the correlation of the service with other services.
        """
        return pulumi.get(self, "service_placement_policies")

    @property
    @pulumi.getter(name="serviceTypeName")
    def service_type_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the service type
        """
        return pulumi.get(self, "service_type_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Azure resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Azure resource type.
        """
        return pulumi.get(self, "type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

