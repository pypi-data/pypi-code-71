# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from admobilize.proto.iam.v1alpha1 import iam_service_pb2 as admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2
from admobilize.proto.iam.v1alpha1 import resources_pb2 as admobilize_dot_iam_dot_v1alpha1_dot_resources__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class IamServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreatePermission = channel.unary_unary(
                '/admobilize.iam.v1alpha1.IamService/CreatePermission',
                request_serializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.CreatePermissionRequest.SerializeToString,
                response_deserializer=admobilize_dot_iam_dot_v1alpha1_dot_resources__pb2.Permission.FromString,
                )
        self.GetPermission = channel.unary_unary(
                '/admobilize.iam.v1alpha1.IamService/GetPermission',
                request_serializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.GetPermissionRequest.SerializeToString,
                response_deserializer=admobilize_dot_iam_dot_v1alpha1_dot_resources__pb2.Permission.FromString,
                )
        self.UpdatePermission = channel.unary_unary(
                '/admobilize.iam.v1alpha1.IamService/UpdatePermission',
                request_serializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.UpdatePermissionRequest.SerializeToString,
                response_deserializer=admobilize_dot_iam_dot_v1alpha1_dot_resources__pb2.Permission.FromString,
                )
        self.ListPermissions = channel.unary_unary(
                '/admobilize.iam.v1alpha1.IamService/ListPermissions',
                request_serializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.ListPermissionsRequest.SerializeToString,
                response_deserializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.ListPermissionsResponse.FromString,
                )
        self.DeletePermission = channel.unary_unary(
                '/admobilize.iam.v1alpha1.IamService/DeletePermission',
                request_serializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.DeletePermissionRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.CreateRole = channel.unary_unary(
                '/admobilize.iam.v1alpha1.IamService/CreateRole',
                request_serializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.CreateRoleRequest.SerializeToString,
                response_deserializer=admobilize_dot_iam_dot_v1alpha1_dot_resources__pb2.Role.FromString,
                )
        self.GetRole = channel.unary_unary(
                '/admobilize.iam.v1alpha1.IamService/GetRole',
                request_serializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.GetRoleRequest.SerializeToString,
                response_deserializer=admobilize_dot_iam_dot_v1alpha1_dot_resources__pb2.Role.FromString,
                )
        self.UpdateRole = channel.unary_unary(
                '/admobilize.iam.v1alpha1.IamService/UpdateRole',
                request_serializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.UpdateRoleRequest.SerializeToString,
                response_deserializer=admobilize_dot_iam_dot_v1alpha1_dot_resources__pb2.Role.FromString,
                )
        self.ListRoles = channel.unary_unary(
                '/admobilize.iam.v1alpha1.IamService/ListRoles',
                request_serializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.ListRolesRequest.SerializeToString,
                response_deserializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.ListRolesResponse.FromString,
                )
        self.DeleteRole = channel.unary_unary(
                '/admobilize.iam.v1alpha1.IamService/DeleteRole',
                request_serializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.DeleteRoleRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.SetPolicy = channel.unary_unary(
                '/admobilize.iam.v1alpha1.IamService/SetPolicy',
                request_serializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.SetPolicyRequest.SerializeToString,
                response_deserializer=admobilize_dot_iam_dot_v1alpha1_dot_resources__pb2.Policy.FromString,
                )
        self.GetPolicy = channel.unary_unary(
                '/admobilize.iam.v1alpha1.IamService/GetPolicy',
                request_serializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.GetPolicyRequest.SerializeToString,
                response_deserializer=admobilize_dot_iam_dot_v1alpha1_dot_resources__pb2.Policy.FromString,
                )
        self.TestPermissions = channel.unary_unary(
                '/admobilize.iam.v1alpha1.IamService/TestPermissions',
                request_serializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.TestPermissionsRequest.SerializeToString,
                response_deserializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.TestPermissionsResponse.FromString,
                )
        self.ListResources = channel.unary_unary(
                '/admobilize.iam.v1alpha1.IamService/ListResources',
                request_serializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.ListResourcesRequest.SerializeToString,
                response_deserializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.ListResourcesResponse.FromString,
                )
        self.DeleteResource = channel.unary_unary(
                '/admobilize.iam.v1alpha1.IamService/DeleteResource',
                request_serializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.DeleteResourceRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.BatchCreateResources = channel.unary_unary(
                '/admobilize.iam.v1alpha1.IamService/BatchCreateResources',
                request_serializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.BatchCreateResourcesRequest.SerializeToString,
                response_deserializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.BatchCreateResourcesResponse.FromString,
                )
        self.DeleteIdentity = channel.unary_unary(
                '/admobilize.iam.v1alpha1.IamService/DeleteIdentity',
                request_serializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.DeleteIdentityRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.ListResourceAncestors = channel.unary_unary(
                '/admobilize.iam.v1alpha1.IamService/ListResourceAncestors',
                request_serializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.ListResourceAncestorsRequest.SerializeToString,
                response_deserializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.ListResourceAncestorsResponse.FromString,
                )
        self.GetResourcesPolicies = channel.unary_unary(
                '/admobilize.iam.v1alpha1.IamService/GetResourcesPolicies',
                request_serializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.GetResourcesPoliciesRequest.SerializeToString,
                response_deserializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.GetResourcesPoliciesResponse.FromString,
                )


class IamServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreatePermission(self, request, context):
        """Create Permission
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPermission(self, request, context):
        """Get permission
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdatePermission(self, request, context):
        """Update permission
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListPermissions(self, request, context):
        """List permissions
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeletePermission(self, request, context):
        """Delete permission
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateRole(self, request, context):
        """Create Role
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRole(self, request, context):
        """Get role
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateRole(self, request, context):
        """Update role
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListRoles(self, request, context):
        """List roles
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteRole(self, request, context):
        """Delete role
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetPolicy(self, request, context):
        """Set Policy
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPolicy(self, request, context):
        """Get Policy
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TestPermissions(self, request, context):
        """Test permissions
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListResources(self, request, context):
        """List Resources
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteResource(self, request, context):
        """Delete resource
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchCreateResources(self, request, context):
        """Batch create resources
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteIdentity(self, request, context):
        """Delete identity
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListResourceAncestors(self, request, context):
        """List resource ancestors
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetResourcesPolicies(self, request, context):
        """Get resources
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IamServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreatePermission': grpc.unary_unary_rpc_method_handler(
                    servicer.CreatePermission,
                    request_deserializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.CreatePermissionRequest.FromString,
                    response_serializer=admobilize_dot_iam_dot_v1alpha1_dot_resources__pb2.Permission.SerializeToString,
            ),
            'GetPermission': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPermission,
                    request_deserializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.GetPermissionRequest.FromString,
                    response_serializer=admobilize_dot_iam_dot_v1alpha1_dot_resources__pb2.Permission.SerializeToString,
            ),
            'UpdatePermission': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdatePermission,
                    request_deserializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.UpdatePermissionRequest.FromString,
                    response_serializer=admobilize_dot_iam_dot_v1alpha1_dot_resources__pb2.Permission.SerializeToString,
            ),
            'ListPermissions': grpc.unary_unary_rpc_method_handler(
                    servicer.ListPermissions,
                    request_deserializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.ListPermissionsRequest.FromString,
                    response_serializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.ListPermissionsResponse.SerializeToString,
            ),
            'DeletePermission': grpc.unary_unary_rpc_method_handler(
                    servicer.DeletePermission,
                    request_deserializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.DeletePermissionRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'CreateRole': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateRole,
                    request_deserializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.CreateRoleRequest.FromString,
                    response_serializer=admobilize_dot_iam_dot_v1alpha1_dot_resources__pb2.Role.SerializeToString,
            ),
            'GetRole': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRole,
                    request_deserializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.GetRoleRequest.FromString,
                    response_serializer=admobilize_dot_iam_dot_v1alpha1_dot_resources__pb2.Role.SerializeToString,
            ),
            'UpdateRole': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateRole,
                    request_deserializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.UpdateRoleRequest.FromString,
                    response_serializer=admobilize_dot_iam_dot_v1alpha1_dot_resources__pb2.Role.SerializeToString,
            ),
            'ListRoles': grpc.unary_unary_rpc_method_handler(
                    servicer.ListRoles,
                    request_deserializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.ListRolesRequest.FromString,
                    response_serializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.ListRolesResponse.SerializeToString,
            ),
            'DeleteRole': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteRole,
                    request_deserializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.DeleteRoleRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'SetPolicy': grpc.unary_unary_rpc_method_handler(
                    servicer.SetPolicy,
                    request_deserializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.SetPolicyRequest.FromString,
                    response_serializer=admobilize_dot_iam_dot_v1alpha1_dot_resources__pb2.Policy.SerializeToString,
            ),
            'GetPolicy': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPolicy,
                    request_deserializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.GetPolicyRequest.FromString,
                    response_serializer=admobilize_dot_iam_dot_v1alpha1_dot_resources__pb2.Policy.SerializeToString,
            ),
            'TestPermissions': grpc.unary_unary_rpc_method_handler(
                    servicer.TestPermissions,
                    request_deserializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.TestPermissionsRequest.FromString,
                    response_serializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.TestPermissionsResponse.SerializeToString,
            ),
            'ListResources': grpc.unary_unary_rpc_method_handler(
                    servicer.ListResources,
                    request_deserializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.ListResourcesRequest.FromString,
                    response_serializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.ListResourcesResponse.SerializeToString,
            ),
            'DeleteResource': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteResource,
                    request_deserializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.DeleteResourceRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'BatchCreateResources': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchCreateResources,
                    request_deserializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.BatchCreateResourcesRequest.FromString,
                    response_serializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.BatchCreateResourcesResponse.SerializeToString,
            ),
            'DeleteIdentity': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteIdentity,
                    request_deserializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.DeleteIdentityRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'ListResourceAncestors': grpc.unary_unary_rpc_method_handler(
                    servicer.ListResourceAncestors,
                    request_deserializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.ListResourceAncestorsRequest.FromString,
                    response_serializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.ListResourceAncestorsResponse.SerializeToString,
            ),
            'GetResourcesPolicies': grpc.unary_unary_rpc_method_handler(
                    servicer.GetResourcesPolicies,
                    request_deserializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.GetResourcesPoliciesRequest.FromString,
                    response_serializer=admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.GetResourcesPoliciesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'admobilize.iam.v1alpha1.IamService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class IamService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreatePermission(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.iam.v1alpha1.IamService/CreatePermission',
            admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.CreatePermissionRequest.SerializeToString,
            admobilize_dot_iam_dot_v1alpha1_dot_resources__pb2.Permission.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPermission(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.iam.v1alpha1.IamService/GetPermission',
            admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.GetPermissionRequest.SerializeToString,
            admobilize_dot_iam_dot_v1alpha1_dot_resources__pb2.Permission.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdatePermission(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.iam.v1alpha1.IamService/UpdatePermission',
            admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.UpdatePermissionRequest.SerializeToString,
            admobilize_dot_iam_dot_v1alpha1_dot_resources__pb2.Permission.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListPermissions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.iam.v1alpha1.IamService/ListPermissions',
            admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.ListPermissionsRequest.SerializeToString,
            admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.ListPermissionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeletePermission(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.iam.v1alpha1.IamService/DeletePermission',
            admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.DeletePermissionRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateRole(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.iam.v1alpha1.IamService/CreateRole',
            admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.CreateRoleRequest.SerializeToString,
            admobilize_dot_iam_dot_v1alpha1_dot_resources__pb2.Role.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRole(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.iam.v1alpha1.IamService/GetRole',
            admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.GetRoleRequest.SerializeToString,
            admobilize_dot_iam_dot_v1alpha1_dot_resources__pb2.Role.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateRole(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.iam.v1alpha1.IamService/UpdateRole',
            admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.UpdateRoleRequest.SerializeToString,
            admobilize_dot_iam_dot_v1alpha1_dot_resources__pb2.Role.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListRoles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.iam.v1alpha1.IamService/ListRoles',
            admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.ListRolesRequest.SerializeToString,
            admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.ListRolesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteRole(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.iam.v1alpha1.IamService/DeleteRole',
            admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.DeleteRoleRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetPolicy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.iam.v1alpha1.IamService/SetPolicy',
            admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.SetPolicyRequest.SerializeToString,
            admobilize_dot_iam_dot_v1alpha1_dot_resources__pb2.Policy.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPolicy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.iam.v1alpha1.IamService/GetPolicy',
            admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.GetPolicyRequest.SerializeToString,
            admobilize_dot_iam_dot_v1alpha1_dot_resources__pb2.Policy.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TestPermissions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.iam.v1alpha1.IamService/TestPermissions',
            admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.TestPermissionsRequest.SerializeToString,
            admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.TestPermissionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListResources(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.iam.v1alpha1.IamService/ListResources',
            admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.ListResourcesRequest.SerializeToString,
            admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.ListResourcesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteResource(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.iam.v1alpha1.IamService/DeleteResource',
            admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.DeleteResourceRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BatchCreateResources(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.iam.v1alpha1.IamService/BatchCreateResources',
            admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.BatchCreateResourcesRequest.SerializeToString,
            admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.BatchCreateResourcesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteIdentity(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.iam.v1alpha1.IamService/DeleteIdentity',
            admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.DeleteIdentityRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListResourceAncestors(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.iam.v1alpha1.IamService/ListResourceAncestors',
            admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.ListResourceAncestorsRequest.SerializeToString,
            admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.ListResourceAncestorsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetResourcesPolicies(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.iam.v1alpha1.IamService/GetResourcesPolicies',
            admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.GetResourcesPoliciesRequest.SerializeToString,
            admobilize_dot_iam_dot_v1alpha1_dot_iam__service__pb2.GetResourcesPoliciesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
