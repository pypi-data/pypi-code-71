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

__all__ = [
    'ListSiteBackupStatusSecretsSlotResult',
    'AwaitableListSiteBackupStatusSecretsSlotResult',
    'list_site_backup_status_secrets_slot',
]

@pulumi.output_type
class ListSiteBackupStatusSecretsSlotResult:
    """
    Backup description
    """
    def __init__(__self__, blob_name=None, correlation_id=None, created=None, databases=None, finished_time_stamp=None, id=None, kind=None, last_restore_time_stamp=None, location=None, log=None, name=None, scheduled=None, size_in_bytes=None, status=None, storage_account_url=None, tags=None, type=None, website_size_in_bytes=None):
        if blob_name and not isinstance(blob_name, str):
            raise TypeError("Expected argument 'blob_name' to be a str")
        pulumi.set(__self__, "blob_name", blob_name)
        if correlation_id and not isinstance(correlation_id, str):
            raise TypeError("Expected argument 'correlation_id' to be a str")
        pulumi.set(__self__, "correlation_id", correlation_id)
        if created and not isinstance(created, str):
            raise TypeError("Expected argument 'created' to be a str")
        pulumi.set(__self__, "created", created)
        if databases and not isinstance(databases, list):
            raise TypeError("Expected argument 'databases' to be a list")
        pulumi.set(__self__, "databases", databases)
        if finished_time_stamp and not isinstance(finished_time_stamp, str):
            raise TypeError("Expected argument 'finished_time_stamp' to be a str")
        pulumi.set(__self__, "finished_time_stamp", finished_time_stamp)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if last_restore_time_stamp and not isinstance(last_restore_time_stamp, str):
            raise TypeError("Expected argument 'last_restore_time_stamp' to be a str")
        pulumi.set(__self__, "last_restore_time_stamp", last_restore_time_stamp)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if log and not isinstance(log, str):
            raise TypeError("Expected argument 'log' to be a str")
        pulumi.set(__self__, "log", log)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if scheduled and not isinstance(scheduled, bool):
            raise TypeError("Expected argument 'scheduled' to be a bool")
        pulumi.set(__self__, "scheduled", scheduled)
        if size_in_bytes and not isinstance(size_in_bytes, int):
            raise TypeError("Expected argument 'size_in_bytes' to be a int")
        pulumi.set(__self__, "size_in_bytes", size_in_bytes)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if storage_account_url and not isinstance(storage_account_url, str):
            raise TypeError("Expected argument 'storage_account_url' to be a str")
        pulumi.set(__self__, "storage_account_url", storage_account_url)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if website_size_in_bytes and not isinstance(website_size_in_bytes, int):
            raise TypeError("Expected argument 'website_size_in_bytes' to be a int")
        pulumi.set(__self__, "website_size_in_bytes", website_size_in_bytes)

    @property
    @pulumi.getter(name="blobName")
    def blob_name(self) -> Optional[str]:
        """
        Name of the blob which contains data for this backup
        """
        return pulumi.get(self, "blob_name")

    @property
    @pulumi.getter(name="correlationId")
    def correlation_id(self) -> Optional[str]:
        """
        Unique correlation identifier. Please use this along with the timestamp while communicating with Azure support.
        """
        return pulumi.get(self, "correlation_id")

    @property
    @pulumi.getter
    def created(self) -> Optional[str]:
        """
        Timestamp of the backup creation
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter
    def databases(self) -> Optional[Sequence['outputs.DatabaseBackupSettingResponseResult']]:
        """
        List of databases included in the backup
        """
        return pulumi.get(self, "databases")

    @property
    @pulumi.getter(name="finishedTimeStamp")
    def finished_time_stamp(self) -> Optional[str]:
        """
        Timestamp when this backup finished.
        """
        return pulumi.get(self, "finished_time_stamp")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind of resource
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="lastRestoreTimeStamp")
    def last_restore_time_stamp(self) -> Optional[str]:
        """
        Timestamp of a last restore operation which used this backup.
        """
        return pulumi.get(self, "last_restore_time_stamp")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource Location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def log(self) -> Optional[str]:
        """
        Details regarding this backup. Might contain an error message.
        """
        return pulumi.get(self, "log")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Resource Name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def scheduled(self) -> Optional[bool]:
        """
        True if this backup has been created due to a schedule being triggered.
        """
        return pulumi.get(self, "scheduled")

    @property
    @pulumi.getter(name="sizeInBytes")
    def size_in_bytes(self) -> Optional[int]:
        """
        Size of the backup in bytes
        """
        return pulumi.get(self, "size_in_bytes")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Backup status
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="storageAccountUrl")
    def storage_account_url(self) -> Optional[str]:
        """
        SAS URL for the storage account container which contains this backup
        """
        return pulumi.get(self, "storage_account_url")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="websiteSizeInBytes")
    def website_size_in_bytes(self) -> Optional[int]:
        """
        Size of the original web app which has been backed up
        """
        return pulumi.get(self, "website_size_in_bytes")


class AwaitableListSiteBackupStatusSecretsSlotResult(ListSiteBackupStatusSecretsSlotResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListSiteBackupStatusSecretsSlotResult(
            blob_name=self.blob_name,
            correlation_id=self.correlation_id,
            created=self.created,
            databases=self.databases,
            finished_time_stamp=self.finished_time_stamp,
            id=self.id,
            kind=self.kind,
            last_restore_time_stamp=self.last_restore_time_stamp,
            location=self.location,
            log=self.log,
            name=self.name,
            scheduled=self.scheduled,
            size_in_bytes=self.size_in_bytes,
            status=self.status,
            storage_account_url=self.storage_account_url,
            tags=self.tags,
            type=self.type,
            website_size_in_bytes=self.website_size_in_bytes)


def list_site_backup_status_secrets_slot(backup_id: Optional[str] = None,
                                         backup_schedule: Optional[pulumi.InputType['BackupScheduleArgs']] = None,
                                         databases: Optional[Sequence[pulumi.InputType['DatabaseBackupSettingArgs']]] = None,
                                         enabled: Optional[bool] = None,
                                         id: Optional[str] = None,
                                         kind: Optional[str] = None,
                                         location: Optional[str] = None,
                                         name: Optional[str] = None,
                                         resource_group_name: Optional[str] = None,
                                         slot: Optional[str] = None,
                                         storage_account_url: Optional[str] = None,
                                         tags: Optional[Mapping[str, str]] = None,
                                         type: Optional[str] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListSiteBackupStatusSecretsSlotResult:
    """
    Use this data source to access information about an existing resource.

    :param str backup_id: Id of backup
    :param pulumi.InputType['BackupScheduleArgs'] backup_schedule: Schedule for the backup if it is executed periodically
    :param Sequence[pulumi.InputType['DatabaseBackupSettingArgs']] databases: Databases included in the backup
    :param bool enabled: True if the backup schedule is enabled (must be included in that case), false if the backup schedule should be disabled
    :param str id: Resource Id
    :param str kind: Kind of resource
    :param str location: Resource Location
    :param str name: Resource Name
    :param str resource_group_name: Name of resource group
    :param str slot: Name of web app slot. If not specified then will default to production slot.
    :param str storage_account_url: SAS URL to the container
    :param Mapping[str, str] tags: Resource tags
    :param str type: Resource type
    """
    __args__ = dict()
    __args__['backupId'] = backup_id
    __args__['backupSchedule'] = backup_schedule
    __args__['databases'] = databases
    __args__['enabled'] = enabled
    __args__['id'] = id
    __args__['kind'] = kind
    __args__['location'] = location
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    __args__['slot'] = slot
    __args__['storageAccountUrl'] = storage_account_url
    __args__['tags'] = tags
    __args__['type'] = type
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-nextgen:web/v20150801:listSiteBackupStatusSecretsSlot', __args__, opts=opts, typ=ListSiteBackupStatusSecretsSlotResult).value

    return AwaitableListSiteBackupStatusSecretsSlotResult(
        blob_name=__ret__.blob_name,
        correlation_id=__ret__.correlation_id,
        created=__ret__.created,
        databases=__ret__.databases,
        finished_time_stamp=__ret__.finished_time_stamp,
        id=__ret__.id,
        kind=__ret__.kind,
        last_restore_time_stamp=__ret__.last_restore_time_stamp,
        location=__ret__.location,
        log=__ret__.log,
        name=__ret__.name,
        scheduled=__ret__.scheduled,
        size_in_bytes=__ret__.size_in_bytes,
        status=__ret__.status,
        storage_account_url=__ret__.storage_account_url,
        tags=__ret__.tags,
        type=__ret__.type,
        website_size_in_bytes=__ret__.website_size_in_bytes)
