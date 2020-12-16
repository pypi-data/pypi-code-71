# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables

__all__ = [
    'GetHybridConnectionResult',
    'AwaitableGetHybridConnectionResult',
    'get_hybrid_connection',
]

@pulumi.output_type
class GetHybridConnectionResult:
    """
    Description of hybrid connection resource.
    """
    def __init__(__self__, created_at=None, id=None, listener_count=None, name=None, requires_client_authorization=None, type=None, updated_at=None, user_metadata=None):
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if listener_count and not isinstance(listener_count, int):
            raise TypeError("Expected argument 'listener_count' to be a int")
        pulumi.set(__self__, "listener_count", listener_count)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if requires_client_authorization and not isinstance(requires_client_authorization, bool):
            raise TypeError("Expected argument 'requires_client_authorization' to be a bool")
        pulumi.set(__self__, "requires_client_authorization", requires_client_authorization)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)
        if user_metadata and not isinstance(user_metadata, str):
            raise TypeError("Expected argument 'user_metadata' to be a str")
        pulumi.set(__self__, "user_metadata", user_metadata)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        The time the hybrid connection was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="listenerCount")
    def listener_count(self) -> int:
        """
        The number of listeners for this hybrid connection. Note that min : 1 and max:25 are supported.
        """
        return pulumi.get(self, "listener_count")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="requiresClientAuthorization")
    def requires_client_authorization(self) -> Optional[bool]:
        """
        Returns true if client authorization is needed for this hybrid connection; otherwise, false.
        """
        return pulumi.get(self, "requires_client_authorization")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> str:
        """
        The time the namespace was updated.
        """
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter(name="userMetadata")
    def user_metadata(self) -> Optional[str]:
        """
        The usermetadata is a placeholder to store user-defined string data for the hybrid connection endpoint. For example, it can be used to store descriptive data, such as a list of teams and their contact information. Also, user-defined configuration settings can be stored.
        """
        return pulumi.get(self, "user_metadata")


class AwaitableGetHybridConnectionResult(GetHybridConnectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetHybridConnectionResult(
            created_at=self.created_at,
            id=self.id,
            listener_count=self.listener_count,
            name=self.name,
            requires_client_authorization=self.requires_client_authorization,
            type=self.type,
            updated_at=self.updated_at,
            user_metadata=self.user_metadata)


def get_hybrid_connection(hybrid_connection_name: Optional[str] = None,
                          namespace_name: Optional[str] = None,
                          resource_group_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetHybridConnectionResult:
    """
    Use this data source to access information about an existing resource.

    :param str hybrid_connection_name: The hybrid connection name.
    :param str namespace_name: The namespace name
    :param str resource_group_name: Name of the Resource group within the Azure subscription.
    """
    __args__ = dict()
    __args__['hybridConnectionName'] = hybrid_connection_name
    __args__['namespaceName'] = namespace_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-nextgen:relay/latest:getHybridConnection', __args__, opts=opts, typ=GetHybridConnectionResult).value

    return AwaitableGetHybridConnectionResult(
        created_at=__ret__.created_at,
        id=__ret__.id,
        listener_count=__ret__.listener_count,
        name=__ret__.name,
        requires_client_authorization=__ret__.requires_client_authorization,
        type=__ret__.type,
        updated_at=__ret__.updated_at,
        user_metadata=__ret__.user_metadata)
