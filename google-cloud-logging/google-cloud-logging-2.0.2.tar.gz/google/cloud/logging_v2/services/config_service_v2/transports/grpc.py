# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import warnings
from typing import Callable, Dict, Optional, Sequence, Tuple

from google.api_core import grpc_helpers  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google import auth  # type: ignore
from google.auth import credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc  # type: ignore

from google.cloud.logging_v2.types import logging_config
from google.protobuf import empty_pb2 as empty  # type: ignore

from .base import ConfigServiceV2Transport, DEFAULT_CLIENT_INFO


class ConfigServiceV2GrpcTransport(ConfigServiceV2Transport):
    """gRPC backend transport for ConfigServiceV2.

    Service for configuring sinks used to route log entries.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _stubs: Dict[str, Callable]

    def __init__(
        self,
        *,
        host: str = "logging.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: str = None,
        scopes: Sequence[str] = None,
        channel: grpc.Channel = None,
        api_mtls_endpoint: str = None,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
        ssl_channel_credentials: grpc.ChannelCredentials = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]): The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            channel (Optional[grpc.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or applicatin default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for grpc channel. It is ignored if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
          google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._ssl_channel_credentials = ssl_channel_credentials

        if channel:
            # Sanity check: Ensure that channel and credentials are not both
            # provided.
            credentials = False

            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None
        elif api_mtls_endpoint:
            warnings.warn(
                "api_mtls_endpoint and client_cert_source are deprecated",
                DeprecationWarning,
            )

            host = (
                api_mtls_endpoint
                if ":" in api_mtls_endpoint
                else api_mtls_endpoint + ":443"
            )

            if credentials is None:
                credentials, _ = auth.default(
                    scopes=self.AUTH_SCOPES, quota_project_id=quota_project_id
                )

            # Create SSL credentials with client_cert_source or application
            # default SSL credentials.
            if client_cert_source:
                cert, key = client_cert_source()
                ssl_credentials = grpc.ssl_channel_credentials(
                    certificate_chain=cert, private_key=key
                )
            else:
                ssl_credentials = SslCredentials().ssl_credentials

            # create a new channel. The provided one is ignored.
            self._grpc_channel = type(self).create_channel(
                host,
                credentials=credentials,
                credentials_file=credentials_file,
                ssl_credentials=ssl_credentials,
                scopes=scopes or self.AUTH_SCOPES,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )
            self._ssl_channel_credentials = ssl_credentials
        else:
            host = host if ":" in host else host + ":443"

            if credentials is None:
                credentials, _ = auth.default(
                    scopes=self.AUTH_SCOPES, quota_project_id=quota_project_id
                )

            # create a new channel. The provided one is ignored.
            self._grpc_channel = type(self).create_channel(
                host,
                credentials=credentials,
                credentials_file=credentials_file,
                ssl_credentials=ssl_channel_credentials,
                scopes=scopes or self.AUTH_SCOPES,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        self._stubs = {}  # type: Dict[str, Callable]

        # Run the base constructor.
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes or self.AUTH_SCOPES,
            quota_project_id=quota_project_id,
            client_info=client_info,
        )

    @classmethod
    def create_channel(
        cls,
        host: str = "logging.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: str = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            address (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            grpc.Channel: A gRPC channel object.

        Raises:
            google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        scopes = scopes or cls.AUTH_SCOPES
        return grpc_helpers.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            **kwargs,
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Return the channel designed to connect to this service.
        """
        return self._grpc_channel

    @property
    def list_buckets(
        self,
    ) -> Callable[
        [logging_config.ListBucketsRequest], logging_config.ListBucketsResponse
    ]:
        r"""Return a callable for the list buckets method over gRPC.

        Lists buckets.

        Returns:
            Callable[[~.ListBucketsRequest],
                    ~.ListBucketsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_buckets" not in self._stubs:
            self._stubs["list_buckets"] = self.grpc_channel.unary_unary(
                "/google.logging.v2.ConfigServiceV2/ListBuckets",
                request_serializer=logging_config.ListBucketsRequest.serialize,
                response_deserializer=logging_config.ListBucketsResponse.deserialize,
            )
        return self._stubs["list_buckets"]

    @property
    def get_bucket(
        self,
    ) -> Callable[[logging_config.GetBucketRequest], logging_config.LogBucket]:
        r"""Return a callable for the get bucket method over gRPC.

        Gets a bucket.

        Returns:
            Callable[[~.GetBucketRequest],
                    ~.LogBucket]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_bucket" not in self._stubs:
            self._stubs["get_bucket"] = self.grpc_channel.unary_unary(
                "/google.logging.v2.ConfigServiceV2/GetBucket",
                request_serializer=logging_config.GetBucketRequest.serialize,
                response_deserializer=logging_config.LogBucket.deserialize,
            )
        return self._stubs["get_bucket"]

    @property
    def create_bucket(
        self,
    ) -> Callable[[logging_config.CreateBucketRequest], logging_config.LogBucket]:
        r"""Return a callable for the create bucket method over gRPC.

        Creates a bucket that can be used to store log
        entries. Once a bucket has been created, the region
        cannot be changed.

        Returns:
            Callable[[~.CreateBucketRequest],
                    ~.LogBucket]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_bucket" not in self._stubs:
            self._stubs["create_bucket"] = self.grpc_channel.unary_unary(
                "/google.logging.v2.ConfigServiceV2/CreateBucket",
                request_serializer=logging_config.CreateBucketRequest.serialize,
                response_deserializer=logging_config.LogBucket.deserialize,
            )
        return self._stubs["create_bucket"]

    @property
    def update_bucket(
        self,
    ) -> Callable[[logging_config.UpdateBucketRequest], logging_config.LogBucket]:
        r"""Return a callable for the update bucket method over gRPC.

        Updates a bucket. This method replaces the following fields in
        the existing bucket with values from the new bucket:
        ``retention_period``

        If the retention period is decreased and the bucket is locked,
        FAILED_PRECONDITION will be returned.

        If the bucket has a LifecycleState of DELETE_REQUESTED,
        FAILED_PRECONDITION will be returned.

        A buckets region may not be modified after it is created.

        Returns:
            Callable[[~.UpdateBucketRequest],
                    ~.LogBucket]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_bucket" not in self._stubs:
            self._stubs["update_bucket"] = self.grpc_channel.unary_unary(
                "/google.logging.v2.ConfigServiceV2/UpdateBucket",
                request_serializer=logging_config.UpdateBucketRequest.serialize,
                response_deserializer=logging_config.LogBucket.deserialize,
            )
        return self._stubs["update_bucket"]

    @property
    def delete_bucket(
        self,
    ) -> Callable[[logging_config.DeleteBucketRequest], empty.Empty]:
        r"""Return a callable for the delete bucket method over gRPC.

        Deletes a bucket. Moves the bucket to the DELETE_REQUESTED
        state. After 7 days, the bucket will be purged and all logs in
        the bucket will be permanently deleted.

        Returns:
            Callable[[~.DeleteBucketRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_bucket" not in self._stubs:
            self._stubs["delete_bucket"] = self.grpc_channel.unary_unary(
                "/google.logging.v2.ConfigServiceV2/DeleteBucket",
                request_serializer=logging_config.DeleteBucketRequest.serialize,
                response_deserializer=empty.Empty.FromString,
            )
        return self._stubs["delete_bucket"]

    @property
    def undelete_bucket(
        self,
    ) -> Callable[[logging_config.UndeleteBucketRequest], empty.Empty]:
        r"""Return a callable for the undelete bucket method over gRPC.

        Undeletes a bucket. A bucket that has been deleted
        may be undeleted within the grace period of 7 days.

        Returns:
            Callable[[~.UndeleteBucketRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "undelete_bucket" not in self._stubs:
            self._stubs["undelete_bucket"] = self.grpc_channel.unary_unary(
                "/google.logging.v2.ConfigServiceV2/UndeleteBucket",
                request_serializer=logging_config.UndeleteBucketRequest.serialize,
                response_deserializer=empty.Empty.FromString,
            )
        return self._stubs["undelete_bucket"]

    @property
    def list_views(
        self,
    ) -> Callable[[logging_config.ListViewsRequest], logging_config.ListViewsResponse]:
        r"""Return a callable for the list views method over gRPC.

        Lists views on a bucket.

        Returns:
            Callable[[~.ListViewsRequest],
                    ~.ListViewsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_views" not in self._stubs:
            self._stubs["list_views"] = self.grpc_channel.unary_unary(
                "/google.logging.v2.ConfigServiceV2/ListViews",
                request_serializer=logging_config.ListViewsRequest.serialize,
                response_deserializer=logging_config.ListViewsResponse.deserialize,
            )
        return self._stubs["list_views"]

    @property
    def get_view(
        self,
    ) -> Callable[[logging_config.GetViewRequest], logging_config.LogView]:
        r"""Return a callable for the get view method over gRPC.

        Gets a view.

        Returns:
            Callable[[~.GetViewRequest],
                    ~.LogView]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_view" not in self._stubs:
            self._stubs["get_view"] = self.grpc_channel.unary_unary(
                "/google.logging.v2.ConfigServiceV2/GetView",
                request_serializer=logging_config.GetViewRequest.serialize,
                response_deserializer=logging_config.LogView.deserialize,
            )
        return self._stubs["get_view"]

    @property
    def create_view(
        self,
    ) -> Callable[[logging_config.CreateViewRequest], logging_config.LogView]:
        r"""Return a callable for the create view method over gRPC.

        Creates a view over logs in a bucket. A bucket may
        contain a maximum of 50 views.

        Returns:
            Callable[[~.CreateViewRequest],
                    ~.LogView]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_view" not in self._stubs:
            self._stubs["create_view"] = self.grpc_channel.unary_unary(
                "/google.logging.v2.ConfigServiceV2/CreateView",
                request_serializer=logging_config.CreateViewRequest.serialize,
                response_deserializer=logging_config.LogView.deserialize,
            )
        return self._stubs["create_view"]

    @property
    def update_view(
        self,
    ) -> Callable[[logging_config.UpdateViewRequest], logging_config.LogView]:
        r"""Return a callable for the update view method over gRPC.

        Updates a view. This method replaces the following fields in the
        existing view with values from the new view: ``filter``.

        Returns:
            Callable[[~.UpdateViewRequest],
                    ~.LogView]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_view" not in self._stubs:
            self._stubs["update_view"] = self.grpc_channel.unary_unary(
                "/google.logging.v2.ConfigServiceV2/UpdateView",
                request_serializer=logging_config.UpdateViewRequest.serialize,
                response_deserializer=logging_config.LogView.deserialize,
            )
        return self._stubs["update_view"]

    @property
    def delete_view(self) -> Callable[[logging_config.DeleteViewRequest], empty.Empty]:
        r"""Return a callable for the delete view method over gRPC.

        Deletes a view from a bucket.

        Returns:
            Callable[[~.DeleteViewRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_view" not in self._stubs:
            self._stubs["delete_view"] = self.grpc_channel.unary_unary(
                "/google.logging.v2.ConfigServiceV2/DeleteView",
                request_serializer=logging_config.DeleteViewRequest.serialize,
                response_deserializer=empty.Empty.FromString,
            )
        return self._stubs["delete_view"]

    @property
    def list_sinks(
        self,
    ) -> Callable[[logging_config.ListSinksRequest], logging_config.ListSinksResponse]:
        r"""Return a callable for the list sinks method over gRPC.

        Lists sinks.

        Returns:
            Callable[[~.ListSinksRequest],
                    ~.ListSinksResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_sinks" not in self._stubs:
            self._stubs["list_sinks"] = self.grpc_channel.unary_unary(
                "/google.logging.v2.ConfigServiceV2/ListSinks",
                request_serializer=logging_config.ListSinksRequest.serialize,
                response_deserializer=logging_config.ListSinksResponse.deserialize,
            )
        return self._stubs["list_sinks"]

    @property
    def get_sink(
        self,
    ) -> Callable[[logging_config.GetSinkRequest], logging_config.LogSink]:
        r"""Return a callable for the get sink method over gRPC.

        Gets a sink.

        Returns:
            Callable[[~.GetSinkRequest],
                    ~.LogSink]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_sink" not in self._stubs:
            self._stubs["get_sink"] = self.grpc_channel.unary_unary(
                "/google.logging.v2.ConfigServiceV2/GetSink",
                request_serializer=logging_config.GetSinkRequest.serialize,
                response_deserializer=logging_config.LogSink.deserialize,
            )
        return self._stubs["get_sink"]

    @property
    def create_sink(
        self,
    ) -> Callable[[logging_config.CreateSinkRequest], logging_config.LogSink]:
        r"""Return a callable for the create sink method over gRPC.

        Creates a sink that exports specified log entries to a
        destination. The export of newly-ingested log entries begins
        immediately, unless the sink's ``writer_identity`` is not
        permitted to write to the destination. A sink can export log
        entries only from the resource owning the sink.

        Returns:
            Callable[[~.CreateSinkRequest],
                    ~.LogSink]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_sink" not in self._stubs:
            self._stubs["create_sink"] = self.grpc_channel.unary_unary(
                "/google.logging.v2.ConfigServiceV2/CreateSink",
                request_serializer=logging_config.CreateSinkRequest.serialize,
                response_deserializer=logging_config.LogSink.deserialize,
            )
        return self._stubs["create_sink"]

    @property
    def update_sink(
        self,
    ) -> Callable[[logging_config.UpdateSinkRequest], logging_config.LogSink]:
        r"""Return a callable for the update sink method over gRPC.

        Updates a sink. This method replaces the following fields in the
        existing sink with values from the new sink: ``destination``,
        and ``filter``.

        The updated sink might also have a new ``writer_identity``; see
        the ``unique_writer_identity`` field.

        Returns:
            Callable[[~.UpdateSinkRequest],
                    ~.LogSink]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_sink" not in self._stubs:
            self._stubs["update_sink"] = self.grpc_channel.unary_unary(
                "/google.logging.v2.ConfigServiceV2/UpdateSink",
                request_serializer=logging_config.UpdateSinkRequest.serialize,
                response_deserializer=logging_config.LogSink.deserialize,
            )
        return self._stubs["update_sink"]

    @property
    def delete_sink(self) -> Callable[[logging_config.DeleteSinkRequest], empty.Empty]:
        r"""Return a callable for the delete sink method over gRPC.

        Deletes a sink. If the sink has a unique ``writer_identity``,
        then that service account is also deleted.

        Returns:
            Callable[[~.DeleteSinkRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_sink" not in self._stubs:
            self._stubs["delete_sink"] = self.grpc_channel.unary_unary(
                "/google.logging.v2.ConfigServiceV2/DeleteSink",
                request_serializer=logging_config.DeleteSinkRequest.serialize,
                response_deserializer=empty.Empty.FromString,
            )
        return self._stubs["delete_sink"]

    @property
    def list_exclusions(
        self,
    ) -> Callable[
        [logging_config.ListExclusionsRequest], logging_config.ListExclusionsResponse
    ]:
        r"""Return a callable for the list exclusions method over gRPC.

        Lists all the exclusions in a parent resource.

        Returns:
            Callable[[~.ListExclusionsRequest],
                    ~.ListExclusionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_exclusions" not in self._stubs:
            self._stubs["list_exclusions"] = self.grpc_channel.unary_unary(
                "/google.logging.v2.ConfigServiceV2/ListExclusions",
                request_serializer=logging_config.ListExclusionsRequest.serialize,
                response_deserializer=logging_config.ListExclusionsResponse.deserialize,
            )
        return self._stubs["list_exclusions"]

    @property
    def get_exclusion(
        self,
    ) -> Callable[[logging_config.GetExclusionRequest], logging_config.LogExclusion]:
        r"""Return a callable for the get exclusion method over gRPC.

        Gets the description of an exclusion.

        Returns:
            Callable[[~.GetExclusionRequest],
                    ~.LogExclusion]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_exclusion" not in self._stubs:
            self._stubs["get_exclusion"] = self.grpc_channel.unary_unary(
                "/google.logging.v2.ConfigServiceV2/GetExclusion",
                request_serializer=logging_config.GetExclusionRequest.serialize,
                response_deserializer=logging_config.LogExclusion.deserialize,
            )
        return self._stubs["get_exclusion"]

    @property
    def create_exclusion(
        self,
    ) -> Callable[[logging_config.CreateExclusionRequest], logging_config.LogExclusion]:
        r"""Return a callable for the create exclusion method over gRPC.

        Creates a new exclusion in a specified parent
        resource. Only log entries belonging to that resource
        can be excluded. You can have up to 10 exclusions in a
        resource.

        Returns:
            Callable[[~.CreateExclusionRequest],
                    ~.LogExclusion]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_exclusion" not in self._stubs:
            self._stubs["create_exclusion"] = self.grpc_channel.unary_unary(
                "/google.logging.v2.ConfigServiceV2/CreateExclusion",
                request_serializer=logging_config.CreateExclusionRequest.serialize,
                response_deserializer=logging_config.LogExclusion.deserialize,
            )
        return self._stubs["create_exclusion"]

    @property
    def update_exclusion(
        self,
    ) -> Callable[[logging_config.UpdateExclusionRequest], logging_config.LogExclusion]:
        r"""Return a callable for the update exclusion method over gRPC.

        Changes one or more properties of an existing
        exclusion.

        Returns:
            Callable[[~.UpdateExclusionRequest],
                    ~.LogExclusion]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_exclusion" not in self._stubs:
            self._stubs["update_exclusion"] = self.grpc_channel.unary_unary(
                "/google.logging.v2.ConfigServiceV2/UpdateExclusion",
                request_serializer=logging_config.UpdateExclusionRequest.serialize,
                response_deserializer=logging_config.LogExclusion.deserialize,
            )
        return self._stubs["update_exclusion"]

    @property
    def delete_exclusion(
        self,
    ) -> Callable[[logging_config.DeleteExclusionRequest], empty.Empty]:
        r"""Return a callable for the delete exclusion method over gRPC.

        Deletes an exclusion.

        Returns:
            Callable[[~.DeleteExclusionRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_exclusion" not in self._stubs:
            self._stubs["delete_exclusion"] = self.grpc_channel.unary_unary(
                "/google.logging.v2.ConfigServiceV2/DeleteExclusion",
                request_serializer=logging_config.DeleteExclusionRequest.serialize,
                response_deserializer=empty.Empty.FromString,
            )
        return self._stubs["delete_exclusion"]

    @property
    def get_cmek_settings(
        self,
    ) -> Callable[[logging_config.GetCmekSettingsRequest], logging_config.CmekSettings]:
        r"""Return a callable for the get cmek settings method over gRPC.

        Gets the Logs Router CMEK settings for the given resource.

        Note: CMEK for the Logs Router can currently only be configured
        for GCP organizations. Once configured, it applies to all
        projects and folders in the GCP organization.

        See `Enabling CMEK for Logs
        Router <https://cloud.google.com/logging/docs/routing/managed-encryption>`__
        for more information.

        Returns:
            Callable[[~.GetCmekSettingsRequest],
                    ~.CmekSettings]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_cmek_settings" not in self._stubs:
            self._stubs["get_cmek_settings"] = self.grpc_channel.unary_unary(
                "/google.logging.v2.ConfigServiceV2/GetCmekSettings",
                request_serializer=logging_config.GetCmekSettingsRequest.serialize,
                response_deserializer=logging_config.CmekSettings.deserialize,
            )
        return self._stubs["get_cmek_settings"]

    @property
    def update_cmek_settings(
        self,
    ) -> Callable[
        [logging_config.UpdateCmekSettingsRequest], logging_config.CmekSettings
    ]:
        r"""Return a callable for the update cmek settings method over gRPC.

        Updates the Logs Router CMEK settings for the given resource.

        Note: CMEK for the Logs Router can currently only be configured
        for GCP organizations. Once configured, it applies to all
        projects and folders in the GCP organization.

        [UpdateCmekSettings][google.logging.v2.ConfigServiceV2.UpdateCmekSettings]
        will fail if 1) ``kms_key_name`` is invalid, or 2) the
        associated service account does not have the required
        ``roles/cloudkms.cryptoKeyEncrypterDecrypter`` role assigned for
        the key, or 3) access to the key is disabled.

        See `Enabling CMEK for Logs
        Router <https://cloud.google.com/logging/docs/routing/managed-encryption>`__
        for more information.

        Returns:
            Callable[[~.UpdateCmekSettingsRequest],
                    ~.CmekSettings]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_cmek_settings" not in self._stubs:
            self._stubs["update_cmek_settings"] = self.grpc_channel.unary_unary(
                "/google.logging.v2.ConfigServiceV2/UpdateCmekSettings",
                request_serializer=logging_config.UpdateCmekSettingsRequest.serialize,
                response_deserializer=logging_config.CmekSettings.deserialize,
            )
        return self._stubs["update_cmek_settings"]


__all__ = ("ConfigServiceV2GrpcTransport",)
