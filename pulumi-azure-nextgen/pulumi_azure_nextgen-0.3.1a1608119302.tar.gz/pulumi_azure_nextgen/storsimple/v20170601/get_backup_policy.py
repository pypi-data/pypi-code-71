# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables

__all__ = [
    'GetBackupPolicyResult',
    'AwaitableGetBackupPolicyResult',
    'get_backup_policy',
]

@pulumi.output_type
class GetBackupPolicyResult:
    """
    The backup policy.
    """
    def __init__(__self__, backup_policy_creation_type=None, id=None, kind=None, last_backup_time=None, name=None, next_backup_time=None, scheduled_backup_status=None, schedules_count=None, ssm_host_name=None, type=None, volume_ids=None):
        if backup_policy_creation_type and not isinstance(backup_policy_creation_type, str):
            raise TypeError("Expected argument 'backup_policy_creation_type' to be a str")
        pulumi.set(__self__, "backup_policy_creation_type", backup_policy_creation_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if last_backup_time and not isinstance(last_backup_time, str):
            raise TypeError("Expected argument 'last_backup_time' to be a str")
        pulumi.set(__self__, "last_backup_time", last_backup_time)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if next_backup_time and not isinstance(next_backup_time, str):
            raise TypeError("Expected argument 'next_backup_time' to be a str")
        pulumi.set(__self__, "next_backup_time", next_backup_time)
        if scheduled_backup_status and not isinstance(scheduled_backup_status, str):
            raise TypeError("Expected argument 'scheduled_backup_status' to be a str")
        pulumi.set(__self__, "scheduled_backup_status", scheduled_backup_status)
        if schedules_count and not isinstance(schedules_count, int):
            raise TypeError("Expected argument 'schedules_count' to be a int")
        pulumi.set(__self__, "schedules_count", schedules_count)
        if ssm_host_name and not isinstance(ssm_host_name, str):
            raise TypeError("Expected argument 'ssm_host_name' to be a str")
        pulumi.set(__self__, "ssm_host_name", ssm_host_name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if volume_ids and not isinstance(volume_ids, list):
            raise TypeError("Expected argument 'volume_ids' to be a list")
        pulumi.set(__self__, "volume_ids", volume_ids)

    @property
    @pulumi.getter(name="backupPolicyCreationType")
    def backup_policy_creation_type(self) -> str:
        """
        The backup policy creation type. Indicates whether this was created through SaaS or through StorSimple Snapshot Manager.
        """
        return pulumi.get(self, "backup_policy_creation_type")

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
    @pulumi.getter(name="lastBackupTime")
    def last_backup_time(self) -> str:
        """
        The time of the last backup for the backup policy.
        """
        return pulumi.get(self, "last_backup_time")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the object.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nextBackupTime")
    def next_backup_time(self) -> str:
        """
        The time of the next backup for the backup policy.
        """
        return pulumi.get(self, "next_backup_time")

    @property
    @pulumi.getter(name="scheduledBackupStatus")
    def scheduled_backup_status(self) -> str:
        """
        Indicates whether at least one of the schedules in the backup policy is active or not.
        """
        return pulumi.get(self, "scheduled_backup_status")

    @property
    @pulumi.getter(name="schedulesCount")
    def schedules_count(self) -> int:
        """
        The count of schedules the backup policy contains.
        """
        return pulumi.get(self, "schedules_count")

    @property
    @pulumi.getter(name="ssmHostName")
    def ssm_host_name(self) -> str:
        """
        If the backup policy was created by StorSimple Snapshot Manager, then this field indicates the hostname of the StorSimple Snapshot Manager.
        """
        return pulumi.get(self, "ssm_host_name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The hierarchical type of the object.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="volumeIds")
    def volume_ids(self) -> Sequence[str]:
        """
        The path IDs of the volumes which are part of the backup policy.
        """
        return pulumi.get(self, "volume_ids")


class AwaitableGetBackupPolicyResult(GetBackupPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBackupPolicyResult(
            backup_policy_creation_type=self.backup_policy_creation_type,
            id=self.id,
            kind=self.kind,
            last_backup_time=self.last_backup_time,
            name=self.name,
            next_backup_time=self.next_backup_time,
            scheduled_backup_status=self.scheduled_backup_status,
            schedules_count=self.schedules_count,
            ssm_host_name=self.ssm_host_name,
            type=self.type,
            volume_ids=self.volume_ids)


def get_backup_policy(backup_policy_name: Optional[str] = None,
                      device_name: Optional[str] = None,
                      manager_name: Optional[str] = None,
                      resource_group_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBackupPolicyResult:
    """
    Use this data source to access information about an existing resource.

    :param str backup_policy_name: The name of backup policy to be fetched.
    :param str device_name: The device name
    :param str manager_name: The manager name
    :param str resource_group_name: The resource group name
    """
    __args__ = dict()
    __args__['backupPolicyName'] = backup_policy_name
    __args__['deviceName'] = device_name
    __args__['managerName'] = manager_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-nextgen:storsimple/v20170601:getBackupPolicy', __args__, opts=opts, typ=GetBackupPolicyResult).value

    return AwaitableGetBackupPolicyResult(
        backup_policy_creation_type=__ret__.backup_policy_creation_type,
        id=__ret__.id,
        kind=__ret__.kind,
        last_backup_time=__ret__.last_backup_time,
        name=__ret__.name,
        next_backup_time=__ret__.next_backup_time,
        scheduled_backup_status=__ret__.scheduled_backup_status,
        schedules_count=__ret__.schedules_count,
        ssm_host_name=__ret__.ssm_host_name,
        type=__ret__.type,
        volume_ids=__ret__.volume_ids)
