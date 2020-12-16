# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables

__all__ = [
    'GetServerAdministratorResult',
    'AwaitableGetServerAdministratorResult',
    'get_server_administrator',
]

@pulumi.output_type
class GetServerAdministratorResult:
    """
    Represents a and external administrator to be created.
    """
    def __init__(__self__, administrator_type=None, id=None, login=None, name=None, sid=None, tenant_id=None, type=None):
        if administrator_type and not isinstance(administrator_type, str):
            raise TypeError("Expected argument 'administrator_type' to be a str")
        pulumi.set(__self__, "administrator_type", administrator_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if login and not isinstance(login, str):
            raise TypeError("Expected argument 'login' to be a str")
        pulumi.set(__self__, "login", login)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if sid and not isinstance(sid, str):
            raise TypeError("Expected argument 'sid' to be a str")
        pulumi.set(__self__, "sid", sid)
        if tenant_id and not isinstance(tenant_id, str):
            raise TypeError("Expected argument 'tenant_id' to be a str")
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="administratorType")
    def administrator_type(self) -> str:
        """
        The type of administrator.
        """
        return pulumi.get(self, "administrator_type")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def login(self) -> str:
        """
        The server administrator login account name.
        """
        return pulumi.get(self, "login")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def sid(self) -> str:
        """
        The server administrator Sid (Secure ID).
        """
        return pulumi.get(self, "sid")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The server Active Directory Administrator tenant id.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetServerAdministratorResult(GetServerAdministratorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServerAdministratorResult(
            administrator_type=self.administrator_type,
            id=self.id,
            login=self.login,
            name=self.name,
            sid=self.sid,
            tenant_id=self.tenant_id,
            type=self.type)


def get_server_administrator(resource_group_name: Optional[str] = None,
                             server_name: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServerAdministratorResult:
    """
    Use this data source to access information about an existing resource.

    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str server_name: The name of the server.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverName'] = server_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-nextgen:dbforpostgresql/v20171201:getServerAdministrator', __args__, opts=opts, typ=GetServerAdministratorResult).value

    return AwaitableGetServerAdministratorResult(
        administrator_type=__ret__.administrator_type,
        id=__ret__.id,
        login=__ret__.login,
        name=__ret__.name,
        sid=__ret__.sid,
        tenant_id=__ret__.tenant_id,
        type=__ret__.type)
