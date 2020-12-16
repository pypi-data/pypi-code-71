# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables

__all__ = [
    'GetFileShareResult',
    'AwaitableGetFileShareResult',
    'get_file_share',
]

@pulumi.output_type
class GetFileShareResult:
    """
    The File Share.
    """
    def __init__(__self__, admin_user=None, data_policy=None, description=None, id=None, local_used_capacity_in_bytes=None, monitoring_status=None, name=None, provisioned_capacity_in_bytes=None, share_status=None, type=None, used_capacity_in_bytes=None):
        if admin_user and not isinstance(admin_user, str):
            raise TypeError("Expected argument 'admin_user' to be a str")
        pulumi.set(__self__, "admin_user", admin_user)
        if data_policy and not isinstance(data_policy, str):
            raise TypeError("Expected argument 'data_policy' to be a str")
        pulumi.set(__self__, "data_policy", data_policy)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if local_used_capacity_in_bytes and not isinstance(local_used_capacity_in_bytes, int):
            raise TypeError("Expected argument 'local_used_capacity_in_bytes' to be a int")
        pulumi.set(__self__, "local_used_capacity_in_bytes", local_used_capacity_in_bytes)
        if monitoring_status and not isinstance(monitoring_status, str):
            raise TypeError("Expected argument 'monitoring_status' to be a str")
        pulumi.set(__self__, "monitoring_status", monitoring_status)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioned_capacity_in_bytes and not isinstance(provisioned_capacity_in_bytes, int):
            raise TypeError("Expected argument 'provisioned_capacity_in_bytes' to be a int")
        pulumi.set(__self__, "provisioned_capacity_in_bytes", provisioned_capacity_in_bytes)
        if share_status and not isinstance(share_status, str):
            raise TypeError("Expected argument 'share_status' to be a str")
        pulumi.set(__self__, "share_status", share_status)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if used_capacity_in_bytes and not isinstance(used_capacity_in_bytes, int):
            raise TypeError("Expected argument 'used_capacity_in_bytes' to be a int")
        pulumi.set(__self__, "used_capacity_in_bytes", used_capacity_in_bytes)

    @property
    @pulumi.getter(name="adminUser")
    def admin_user(self) -> str:
        """
        The user/group who will have full permission in this share. Active directory email address. Example: xyz@contoso.com or Contoso\\xyz.
        """
        return pulumi.get(self, "admin_user")

    @property
    @pulumi.getter(name="dataPolicy")
    def data_policy(self) -> str:
        """
        The data policy
        """
        return pulumi.get(self, "data_policy")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description for file share
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The identifier.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="localUsedCapacityInBytes")
    def local_used_capacity_in_bytes(self) -> int:
        """
        The local used capacity in Bytes.
        """
        return pulumi.get(self, "local_used_capacity_in_bytes")

    @property
    @pulumi.getter(name="monitoringStatus")
    def monitoring_status(self) -> str:
        """
        The monitoring status
        """
        return pulumi.get(self, "monitoring_status")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisionedCapacityInBytes")
    def provisioned_capacity_in_bytes(self) -> int:
        """
        The total provisioned capacity in Bytes
        """
        return pulumi.get(self, "provisioned_capacity_in_bytes")

    @property
    @pulumi.getter(name="shareStatus")
    def share_status(self) -> str:
        """
        The Share Status
        """
        return pulumi.get(self, "share_status")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="usedCapacityInBytes")
    def used_capacity_in_bytes(self) -> int:
        """
        The used capacity in Bytes.
        """
        return pulumi.get(self, "used_capacity_in_bytes")


class AwaitableGetFileShareResult(GetFileShareResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFileShareResult(
            admin_user=self.admin_user,
            data_policy=self.data_policy,
            description=self.description,
            id=self.id,
            local_used_capacity_in_bytes=self.local_used_capacity_in_bytes,
            monitoring_status=self.monitoring_status,
            name=self.name,
            provisioned_capacity_in_bytes=self.provisioned_capacity_in_bytes,
            share_status=self.share_status,
            type=self.type,
            used_capacity_in_bytes=self.used_capacity_in_bytes)


def get_file_share(device_name: Optional[str] = None,
                   file_server_name: Optional[str] = None,
                   manager_name: Optional[str] = None,
                   resource_group_name: Optional[str] = None,
                   share_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFileShareResult:
    """
    Use this data source to access information about an existing resource.

    :param str device_name: The device name.
    :param str file_server_name: The file server name.
    :param str manager_name: The manager name
    :param str resource_group_name: The resource group name
    :param str share_name: The file share name.
    """
    __args__ = dict()
    __args__['deviceName'] = device_name
    __args__['fileServerName'] = file_server_name
    __args__['managerName'] = manager_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['shareName'] = share_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-nextgen:storsimple/latest:getFileShare', __args__, opts=opts, typ=GetFileShareResult).value

    return AwaitableGetFileShareResult(
        admin_user=__ret__.admin_user,
        data_policy=__ret__.data_policy,
        description=__ret__.description,
        id=__ret__.id,
        local_used_capacity_in_bytes=__ret__.local_used_capacity_in_bytes,
        monitoring_status=__ret__.monitoring_status,
        name=__ret__.name,
        provisioned_capacity_in_bytes=__ret__.provisioned_capacity_in_bytes,
        share_status=__ret__.share_status,
        type=__ret__.type,
        used_capacity_in_bytes=__ret__.used_capacity_in_bytes)
