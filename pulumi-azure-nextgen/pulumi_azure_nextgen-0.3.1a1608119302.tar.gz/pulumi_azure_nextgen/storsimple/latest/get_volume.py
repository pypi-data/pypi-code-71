# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables

__all__ = [
    'GetVolumeResult',
    'AwaitableGetVolumeResult',
    'get_volume',
]

@pulumi.output_type
class GetVolumeResult:
    """
    The volume.
    """
    def __init__(__self__, access_control_record_ids=None, backup_policy_ids=None, backup_status=None, id=None, kind=None, monitoring_status=None, name=None, operation_status=None, size_in_bytes=None, type=None, volume_container_id=None, volume_status=None, volume_type=None):
        if access_control_record_ids and not isinstance(access_control_record_ids, list):
            raise TypeError("Expected argument 'access_control_record_ids' to be a list")
        pulumi.set(__self__, "access_control_record_ids", access_control_record_ids)
        if backup_policy_ids and not isinstance(backup_policy_ids, list):
            raise TypeError("Expected argument 'backup_policy_ids' to be a list")
        pulumi.set(__self__, "backup_policy_ids", backup_policy_ids)
        if backup_status and not isinstance(backup_status, str):
            raise TypeError("Expected argument 'backup_status' to be a str")
        pulumi.set(__self__, "backup_status", backup_status)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if monitoring_status and not isinstance(monitoring_status, str):
            raise TypeError("Expected argument 'monitoring_status' to be a str")
        pulumi.set(__self__, "monitoring_status", monitoring_status)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if operation_status and not isinstance(operation_status, str):
            raise TypeError("Expected argument 'operation_status' to be a str")
        pulumi.set(__self__, "operation_status", operation_status)
        if size_in_bytes and not isinstance(size_in_bytes, int):
            raise TypeError("Expected argument 'size_in_bytes' to be a int")
        pulumi.set(__self__, "size_in_bytes", size_in_bytes)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if volume_container_id and not isinstance(volume_container_id, str):
            raise TypeError("Expected argument 'volume_container_id' to be a str")
        pulumi.set(__self__, "volume_container_id", volume_container_id)
        if volume_status and not isinstance(volume_status, str):
            raise TypeError("Expected argument 'volume_status' to be a str")
        pulumi.set(__self__, "volume_status", volume_status)
        if volume_type and not isinstance(volume_type, str):
            raise TypeError("Expected argument 'volume_type' to be a str")
        pulumi.set(__self__, "volume_type", volume_type)

    @property
    @pulumi.getter(name="accessControlRecordIds")
    def access_control_record_ids(self) -> Sequence[str]:
        """
        The IDs of the access control records, associated with the volume.
        """
        return pulumi.get(self, "access_control_record_ids")

    @property
    @pulumi.getter(name="backupPolicyIds")
    def backup_policy_ids(self) -> Sequence[str]:
        """
        The IDs of the backup policies, in which this volume is part of.
        """
        return pulumi.get(self, "backup_policy_ids")

    @property
    @pulumi.getter(name="backupStatus")
    def backup_status(self) -> str:
        """
        The backup status of the volume.
        """
        return pulumi.get(self, "backup_status")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The path ID that uniquely identifies the object.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        The Kind of the object. Currently only Series8000 is supported
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="monitoringStatus")
    def monitoring_status(self) -> str:
        """
        The monitoring status of the volume.
        """
        return pulumi.get(self, "monitoring_status")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the object.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="operationStatus")
    def operation_status(self) -> str:
        """
        The operation status on the volume.
        """
        return pulumi.get(self, "operation_status")

    @property
    @pulumi.getter(name="sizeInBytes")
    def size_in_bytes(self) -> int:
        """
        The size of the volume in bytes.
        """
        return pulumi.get(self, "size_in_bytes")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The hierarchical type of the object.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="volumeContainerId")
    def volume_container_id(self) -> str:
        """
        The ID of the volume container, in which this volume is created.
        """
        return pulumi.get(self, "volume_container_id")

    @property
    @pulumi.getter(name="volumeStatus")
    def volume_status(self) -> str:
        """
        The volume status.
        """
        return pulumi.get(self, "volume_status")

    @property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> str:
        """
        The type of the volume.
        """
        return pulumi.get(self, "volume_type")


class AwaitableGetVolumeResult(GetVolumeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVolumeResult(
            access_control_record_ids=self.access_control_record_ids,
            backup_policy_ids=self.backup_policy_ids,
            backup_status=self.backup_status,
            id=self.id,
            kind=self.kind,
            monitoring_status=self.monitoring_status,
            name=self.name,
            operation_status=self.operation_status,
            size_in_bytes=self.size_in_bytes,
            type=self.type,
            volume_container_id=self.volume_container_id,
            volume_status=self.volume_status,
            volume_type=self.volume_type)


def get_volume(device_name: Optional[str] = None,
               manager_name: Optional[str] = None,
               resource_group_name: Optional[str] = None,
               volume_container_name: Optional[str] = None,
               volume_name: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVolumeResult:
    """
    Use this data source to access information about an existing resource.

    :param str device_name: The device name
    :param str manager_name: The manager name
    :param str resource_group_name: The resource group name
    :param str volume_container_name: The volume container name.
    :param str volume_name: The volume name.
    """
    __args__ = dict()
    __args__['deviceName'] = device_name
    __args__['managerName'] = manager_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['volumeContainerName'] = volume_container_name
    __args__['volumeName'] = volume_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-nextgen:storsimple/latest:getVolume', __args__, opts=opts, typ=GetVolumeResult).value

    return AwaitableGetVolumeResult(
        access_control_record_ids=__ret__.access_control_record_ids,
        backup_policy_ids=__ret__.backup_policy_ids,
        backup_status=__ret__.backup_status,
        id=__ret__.id,
        kind=__ret__.kind,
        monitoring_status=__ret__.monitoring_status,
        name=__ret__.name,
        operation_status=__ret__.operation_status,
        size_in_bytes=__ret__.size_in_bytes,
        type=__ret__.type,
        volume_container_id=__ret__.volume_container_id,
        volume_status=__ret__.volume_status,
        volume_type=__ret__.volume_type)
