# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables
from . import outputs

__all__ = [
    'GetDiskResult',
    'AwaitableGetDiskResult',
    'get_disk',
]

@pulumi.output_type
class GetDiskResult:
    """
    Disk resource.
    """
    def __init__(__self__, creation_data=None, disk_iops_read_only=None, disk_iops_read_write=None, disk_m_bps_read_only=None, disk_m_bps_read_write=None, disk_size_bytes=None, disk_size_gb=None, disk_state=None, encryption=None, encryption_settings_collection=None, hyper_v_generation=None, id=None, location=None, managed_by=None, managed_by_extended=None, max_shares=None, name=None, os_type=None, provisioning_state=None, share_info=None, sku=None, tags=None, time_created=None, type=None, unique_id=None, zones=None):
        if creation_data and not isinstance(creation_data, dict):
            raise TypeError("Expected argument 'creation_data' to be a dict")
        pulumi.set(__self__, "creation_data", creation_data)
        if disk_iops_read_only and not isinstance(disk_iops_read_only, int):
            raise TypeError("Expected argument 'disk_iops_read_only' to be a int")
        pulumi.set(__self__, "disk_iops_read_only", disk_iops_read_only)
        if disk_iops_read_write and not isinstance(disk_iops_read_write, int):
            raise TypeError("Expected argument 'disk_iops_read_write' to be a int")
        pulumi.set(__self__, "disk_iops_read_write", disk_iops_read_write)
        if disk_m_bps_read_only and not isinstance(disk_m_bps_read_only, int):
            raise TypeError("Expected argument 'disk_m_bps_read_only' to be a int")
        pulumi.set(__self__, "disk_m_bps_read_only", disk_m_bps_read_only)
        if disk_m_bps_read_write and not isinstance(disk_m_bps_read_write, int):
            raise TypeError("Expected argument 'disk_m_bps_read_write' to be a int")
        pulumi.set(__self__, "disk_m_bps_read_write", disk_m_bps_read_write)
        if disk_size_bytes and not isinstance(disk_size_bytes, int):
            raise TypeError("Expected argument 'disk_size_bytes' to be a int")
        pulumi.set(__self__, "disk_size_bytes", disk_size_bytes)
        if disk_size_gb and not isinstance(disk_size_gb, int):
            raise TypeError("Expected argument 'disk_size_gb' to be a int")
        pulumi.set(__self__, "disk_size_gb", disk_size_gb)
        if disk_state and not isinstance(disk_state, str):
            raise TypeError("Expected argument 'disk_state' to be a str")
        pulumi.set(__self__, "disk_state", disk_state)
        if encryption and not isinstance(encryption, dict):
            raise TypeError("Expected argument 'encryption' to be a dict")
        pulumi.set(__self__, "encryption", encryption)
        if encryption_settings_collection and not isinstance(encryption_settings_collection, dict):
            raise TypeError("Expected argument 'encryption_settings_collection' to be a dict")
        pulumi.set(__self__, "encryption_settings_collection", encryption_settings_collection)
        if hyper_v_generation and not isinstance(hyper_v_generation, str):
            raise TypeError("Expected argument 'hyper_v_generation' to be a str")
        pulumi.set(__self__, "hyper_v_generation", hyper_v_generation)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if managed_by and not isinstance(managed_by, str):
            raise TypeError("Expected argument 'managed_by' to be a str")
        pulumi.set(__self__, "managed_by", managed_by)
        if managed_by_extended and not isinstance(managed_by_extended, list):
            raise TypeError("Expected argument 'managed_by_extended' to be a list")
        pulumi.set(__self__, "managed_by_extended", managed_by_extended)
        if max_shares and not isinstance(max_shares, int):
            raise TypeError("Expected argument 'max_shares' to be a int")
        pulumi.set(__self__, "max_shares", max_shares)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if os_type and not isinstance(os_type, str):
            raise TypeError("Expected argument 'os_type' to be a str")
        pulumi.set(__self__, "os_type", os_type)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if share_info and not isinstance(share_info, list):
            raise TypeError("Expected argument 'share_info' to be a list")
        pulumi.set(__self__, "share_info", share_info)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if unique_id and not isinstance(unique_id, str):
            raise TypeError("Expected argument 'unique_id' to be a str")
        pulumi.set(__self__, "unique_id", unique_id)
        if zones and not isinstance(zones, list):
            raise TypeError("Expected argument 'zones' to be a list")
        pulumi.set(__self__, "zones", zones)

    @property
    @pulumi.getter(name="creationData")
    def creation_data(self) -> 'outputs.CreationDataResponse':
        """
        Disk source information. CreationData information cannot be changed after the disk has been created.
        """
        return pulumi.get(self, "creation_data")

    @property
    @pulumi.getter(name="diskIOPSReadOnly")
    def disk_iops_read_only(self) -> Optional[int]:
        """
        The total number of IOPS that will be allowed across all VMs mounting the shared disk as ReadOnly. One operation can transfer between 4k and 256k bytes.
        """
        return pulumi.get(self, "disk_iops_read_only")

    @property
    @pulumi.getter(name="diskIOPSReadWrite")
    def disk_iops_read_write(self) -> Optional[int]:
        """
        The number of IOPS allowed for this disk; only settable for UltraSSD disks. One operation can transfer between 4k and 256k bytes.
        """
        return pulumi.get(self, "disk_iops_read_write")

    @property
    @pulumi.getter(name="diskMBpsReadOnly")
    def disk_m_bps_read_only(self) -> Optional[int]:
        """
        The total throughput (MBps) that will be allowed across all VMs mounting the shared disk as ReadOnly. MBps means millions of bytes per second - MB here uses the ISO notation, of powers of 10.
        """
        return pulumi.get(self, "disk_m_bps_read_only")

    @property
    @pulumi.getter(name="diskMBpsReadWrite")
    def disk_m_bps_read_write(self) -> Optional[int]:
        """
        The bandwidth allowed for this disk; only settable for UltraSSD disks. MBps means millions of bytes per second - MB here uses the ISO notation, of powers of 10.
        """
        return pulumi.get(self, "disk_m_bps_read_write")

    @property
    @pulumi.getter(name="diskSizeBytes")
    def disk_size_bytes(self) -> int:
        """
        The size of the disk in bytes. This field is read only.
        """
        return pulumi.get(self, "disk_size_bytes")

    @property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> Optional[int]:
        """
        If creationData.createOption is Empty, this field is mandatory and it indicates the size of the disk to create. If this field is present for updates or creation with other options, it indicates a resize. Resizes are only allowed if the disk is not attached to a running VM, and can only increase the disk's size.
        """
        return pulumi.get(self, "disk_size_gb")

    @property
    @pulumi.getter(name="diskState")
    def disk_state(self) -> str:
        """
        The state of the disk.
        """
        return pulumi.get(self, "disk_state")

    @property
    @pulumi.getter
    def encryption(self) -> Optional['outputs.EncryptionResponse']:
        """
        Encryption property can be used to encrypt data at rest with customer managed keys or platform managed keys.
        """
        return pulumi.get(self, "encryption")

    @property
    @pulumi.getter(name="encryptionSettingsCollection")
    def encryption_settings_collection(self) -> Optional['outputs.EncryptionSettingsCollectionResponse']:
        """
        Encryption settings collection used for Azure Disk Encryption, can contain multiple encryption settings per disk or snapshot.
        """
        return pulumi.get(self, "encryption_settings_collection")

    @property
    @pulumi.getter(name="hyperVGeneration")
    def hyper_v_generation(self) -> Optional[str]:
        """
        The hypervisor generation of the Virtual Machine. Applicable to OS disks only.
        """
        return pulumi.get(self, "hyper_v_generation")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> str:
        """
        A relative URI containing the ID of the VM that has the disk attached.
        """
        return pulumi.get(self, "managed_by")

    @property
    @pulumi.getter(name="managedByExtended")
    def managed_by_extended(self) -> Sequence[str]:
        """
        List of relative URIs containing the IDs of the VMs that have the disk attached. maxShares should be set to a value greater than one for disks to allow attaching them to multiple VMs.
        """
        return pulumi.get(self, "managed_by_extended")

    @property
    @pulumi.getter(name="maxShares")
    def max_shares(self) -> Optional[int]:
        """
        The maximum number of VMs that can attach to the disk at the same time. Value greater than one indicates a disk that can be mounted on multiple VMs at the same time.
        """
        return pulumi.get(self, "max_shares")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[str]:
        """
        The Operating System type.
        """
        return pulumi.get(self, "os_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The disk provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="shareInfo")
    def share_info(self) -> Sequence['outputs.ShareInfoElementResponse']:
        """
        Details of the list of all VMs that have the disk attached. maxShares should be set to a value greater than one for disks to allow attaching them to multiple VMs.
        """
        return pulumi.get(self, "share_info")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.DiskSkuResponse']:
        """
        The disks sku name. Can be Standard_LRS, Premium_LRS, StandardSSD_LRS, or UltraSSD_LRS.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The time when the disk was created.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> str:
        """
        Unique Guid identifying the resource.
        """
        return pulumi.get(self, "unique_id")

    @property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[str]]:
        """
        The Logical zone list for Disk.
        """
        return pulumi.get(self, "zones")


class AwaitableGetDiskResult(GetDiskResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDiskResult(
            creation_data=self.creation_data,
            disk_iops_read_only=self.disk_iops_read_only,
            disk_iops_read_write=self.disk_iops_read_write,
            disk_m_bps_read_only=self.disk_m_bps_read_only,
            disk_m_bps_read_write=self.disk_m_bps_read_write,
            disk_size_bytes=self.disk_size_bytes,
            disk_size_gb=self.disk_size_gb,
            disk_state=self.disk_state,
            encryption=self.encryption,
            encryption_settings_collection=self.encryption_settings_collection,
            hyper_v_generation=self.hyper_v_generation,
            id=self.id,
            location=self.location,
            managed_by=self.managed_by,
            managed_by_extended=self.managed_by_extended,
            max_shares=self.max_shares,
            name=self.name,
            os_type=self.os_type,
            provisioning_state=self.provisioning_state,
            share_info=self.share_info,
            sku=self.sku,
            tags=self.tags,
            time_created=self.time_created,
            type=self.type,
            unique_id=self.unique_id,
            zones=self.zones)


def get_disk(disk_name: Optional[str] = None,
             resource_group_name: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDiskResult:
    """
    Use this data source to access information about an existing resource.

    :param str disk_name: The name of the managed disk that is being created. The name can't be changed after the disk is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['diskName'] = disk_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-nextgen:compute/v20191101:getDisk', __args__, opts=opts, typ=GetDiskResult).value

    return AwaitableGetDiskResult(
        creation_data=__ret__.creation_data,
        disk_iops_read_only=__ret__.disk_iops_read_only,
        disk_iops_read_write=__ret__.disk_iops_read_write,
        disk_m_bps_read_only=__ret__.disk_m_bps_read_only,
        disk_m_bps_read_write=__ret__.disk_m_bps_read_write,
        disk_size_bytes=__ret__.disk_size_bytes,
        disk_size_gb=__ret__.disk_size_gb,
        disk_state=__ret__.disk_state,
        encryption=__ret__.encryption,
        encryption_settings_collection=__ret__.encryption_settings_collection,
        hyper_v_generation=__ret__.hyper_v_generation,
        id=__ret__.id,
        location=__ret__.location,
        managed_by=__ret__.managed_by,
        managed_by_extended=__ret__.managed_by_extended,
        max_shares=__ret__.max_shares,
        name=__ret__.name,
        os_type=__ret__.os_type,
        provisioning_state=__ret__.provisioning_state,
        share_info=__ret__.share_info,
        sku=__ret__.sku,
        tags=__ret__.tags,
        time_created=__ret__.time_created,
        type=__ret__.type,
        unique_id=__ret__.unique_id,
        zones=__ret__.zones)
