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

__all__ = ['Disk']


class Disk(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 creation_data: Optional[pulumi.Input[pulumi.InputType['CreationDataArgs']]] = None,
                 disk_iops_read_only: Optional[pulumi.Input[int]] = None,
                 disk_iops_read_write: Optional[pulumi.Input[int]] = None,
                 disk_m_bps_read_only: Optional[pulumi.Input[int]] = None,
                 disk_m_bps_read_write: Optional[pulumi.Input[int]] = None,
                 disk_name: Optional[pulumi.Input[str]] = None,
                 disk_size_gb: Optional[pulumi.Input[int]] = None,
                 encryption: Optional[pulumi.Input[pulumi.InputType['EncryptionArgs']]] = None,
                 encryption_settings_collection: Optional[pulumi.Input[pulumi.InputType['EncryptionSettingsCollectionArgs']]] = None,
                 hyper_v_generation: Optional[pulumi.Input[Union[str, 'HyperVGeneration']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 max_shares: Optional[pulumi.Input[int]] = None,
                 os_type: Optional[pulumi.Input['OperatingSystemTypes']] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['DiskSkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Disk resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['CreationDataArgs']] creation_data: Disk source information. CreationData information cannot be changed after the disk has been created.
        :param pulumi.Input[int] disk_iops_read_only: The total number of IOPS that will be allowed across all VMs mounting the shared disk as ReadOnly. One operation can transfer between 4k and 256k bytes.
        :param pulumi.Input[int] disk_iops_read_write: The number of IOPS allowed for this disk; only settable for UltraSSD disks. One operation can transfer between 4k and 256k bytes.
        :param pulumi.Input[int] disk_m_bps_read_only: The total throughput (MBps) that will be allowed across all VMs mounting the shared disk as ReadOnly. MBps means millions of bytes per second - MB here uses the ISO notation, of powers of 10.
        :param pulumi.Input[int] disk_m_bps_read_write: The bandwidth allowed for this disk; only settable for UltraSSD disks. MBps means millions of bytes per second - MB here uses the ISO notation, of powers of 10.
        :param pulumi.Input[str] disk_name: The name of the managed disk that is being created. The name can't be changed after the disk is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters.
        :param pulumi.Input[int] disk_size_gb: If creationData.createOption is Empty, this field is mandatory and it indicates the size of the disk to create. If this field is present for updates or creation with other options, it indicates a resize. Resizes are only allowed if the disk is not attached to a running VM, and can only increase the disk's size.
        :param pulumi.Input[pulumi.InputType['EncryptionArgs']] encryption: Encryption property can be used to encrypt data at rest with customer managed keys or platform managed keys.
        :param pulumi.Input[pulumi.InputType['EncryptionSettingsCollectionArgs']] encryption_settings_collection: Encryption settings collection used for Azure Disk Encryption, can contain multiple encryption settings per disk or snapshot.
        :param pulumi.Input[Union[str, 'HyperVGeneration']] hyper_v_generation: The hypervisor generation of the Virtual Machine. Applicable to OS disks only.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[int] max_shares: The maximum number of VMs that can attach to the disk at the same time. Value greater than one indicates a disk that can be mounted on multiple VMs at the same time.
        :param pulumi.Input['OperatingSystemTypes'] os_type: The Operating System type.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[pulumi.InputType['DiskSkuArgs']] sku: The disks sku name. Can be Standard_LRS, Premium_LRS, StandardSSD_LRS, or UltraSSD_LRS.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[Sequence[pulumi.Input[str]]] zones: The Logical zone list for Disk.
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

            if creation_data is None and not opts.urn:
                raise TypeError("Missing required property 'creation_data'")
            __props__['creation_data'] = creation_data
            __props__['disk_iops_read_only'] = disk_iops_read_only
            __props__['disk_iops_read_write'] = disk_iops_read_write
            __props__['disk_m_bps_read_only'] = disk_m_bps_read_only
            __props__['disk_m_bps_read_write'] = disk_m_bps_read_write
            if disk_name is None and not opts.urn:
                raise TypeError("Missing required property 'disk_name'")
            __props__['disk_name'] = disk_name
            __props__['disk_size_gb'] = disk_size_gb
            __props__['encryption'] = encryption
            __props__['encryption_settings_collection'] = encryption_settings_collection
            __props__['hyper_v_generation'] = hyper_v_generation
            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__['location'] = location
            __props__['max_shares'] = max_shares
            __props__['os_type'] = os_type
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['sku'] = sku
            __props__['tags'] = tags
            __props__['zones'] = zones
            __props__['disk_size_bytes'] = None
            __props__['disk_state'] = None
            __props__['managed_by'] = None
            __props__['managed_by_extended'] = None
            __props__['name'] = None
            __props__['provisioning_state'] = None
            __props__['share_info'] = None
            __props__['time_created'] = None
            __props__['type'] = None
            __props__['unique_id'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:compute/latest:Disk"), pulumi.Alias(type_="azure-nextgen:compute/v20160430preview:Disk"), pulumi.Alias(type_="azure-nextgen:compute/v20170330:Disk"), pulumi.Alias(type_="azure-nextgen:compute/v20180401:Disk"), pulumi.Alias(type_="azure-nextgen:compute/v20180601:Disk"), pulumi.Alias(type_="azure-nextgen:compute/v20180930:Disk"), pulumi.Alias(type_="azure-nextgen:compute/v20190301:Disk"), pulumi.Alias(type_="azure-nextgen:compute/v20190701:Disk"), pulumi.Alias(type_="azure-nextgen:compute/v20200501:Disk"), pulumi.Alias(type_="azure-nextgen:compute/v20200630:Disk")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Disk, __self__).__init__(
            'azure-nextgen:compute/v20191101:Disk',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Disk':
        """
        Get an existing Disk resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return Disk(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationData")
    def creation_data(self) -> pulumi.Output['outputs.CreationDataResponse']:
        """
        Disk source information. CreationData information cannot be changed after the disk has been created.
        """
        return pulumi.get(self, "creation_data")

    @property
    @pulumi.getter(name="diskIOPSReadOnly")
    def disk_iops_read_only(self) -> pulumi.Output[Optional[int]]:
        """
        The total number of IOPS that will be allowed across all VMs mounting the shared disk as ReadOnly. One operation can transfer between 4k and 256k bytes.
        """
        return pulumi.get(self, "disk_iops_read_only")

    @property
    @pulumi.getter(name="diskIOPSReadWrite")
    def disk_iops_read_write(self) -> pulumi.Output[Optional[int]]:
        """
        The number of IOPS allowed for this disk; only settable for UltraSSD disks. One operation can transfer between 4k and 256k bytes.
        """
        return pulumi.get(self, "disk_iops_read_write")

    @property
    @pulumi.getter(name="diskMBpsReadOnly")
    def disk_m_bps_read_only(self) -> pulumi.Output[Optional[int]]:
        """
        The total throughput (MBps) that will be allowed across all VMs mounting the shared disk as ReadOnly. MBps means millions of bytes per second - MB here uses the ISO notation, of powers of 10.
        """
        return pulumi.get(self, "disk_m_bps_read_only")

    @property
    @pulumi.getter(name="diskMBpsReadWrite")
    def disk_m_bps_read_write(self) -> pulumi.Output[Optional[int]]:
        """
        The bandwidth allowed for this disk; only settable for UltraSSD disks. MBps means millions of bytes per second - MB here uses the ISO notation, of powers of 10.
        """
        return pulumi.get(self, "disk_m_bps_read_write")

    @property
    @pulumi.getter(name="diskSizeBytes")
    def disk_size_bytes(self) -> pulumi.Output[int]:
        """
        The size of the disk in bytes. This field is read only.
        """
        return pulumi.get(self, "disk_size_bytes")

    @property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> pulumi.Output[Optional[int]]:
        """
        If creationData.createOption is Empty, this field is mandatory and it indicates the size of the disk to create. If this field is present for updates or creation with other options, it indicates a resize. Resizes are only allowed if the disk is not attached to a running VM, and can only increase the disk's size.
        """
        return pulumi.get(self, "disk_size_gb")

    @property
    @pulumi.getter(name="diskState")
    def disk_state(self) -> pulumi.Output[str]:
        """
        The state of the disk.
        """
        return pulumi.get(self, "disk_state")

    @property
    @pulumi.getter
    def encryption(self) -> pulumi.Output[Optional['outputs.EncryptionResponse']]:
        """
        Encryption property can be used to encrypt data at rest with customer managed keys or platform managed keys.
        """
        return pulumi.get(self, "encryption")

    @property
    @pulumi.getter(name="encryptionSettingsCollection")
    def encryption_settings_collection(self) -> pulumi.Output[Optional['outputs.EncryptionSettingsCollectionResponse']]:
        """
        Encryption settings collection used for Azure Disk Encryption, can contain multiple encryption settings per disk or snapshot.
        """
        return pulumi.get(self, "encryption_settings_collection")

    @property
    @pulumi.getter(name="hyperVGeneration")
    def hyper_v_generation(self) -> pulumi.Output[Optional[str]]:
        """
        The hypervisor generation of the Virtual Machine. Applicable to OS disks only.
        """
        return pulumi.get(self, "hyper_v_generation")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> pulumi.Output[str]:
        """
        A relative URI containing the ID of the VM that has the disk attached.
        """
        return pulumi.get(self, "managed_by")

    @property
    @pulumi.getter(name="managedByExtended")
    def managed_by_extended(self) -> pulumi.Output[Sequence[str]]:
        """
        List of relative URIs containing the IDs of the VMs that have the disk attached. maxShares should be set to a value greater than one for disks to allow attaching them to multiple VMs.
        """
        return pulumi.get(self, "managed_by_extended")

    @property
    @pulumi.getter(name="maxShares")
    def max_shares(self) -> pulumi.Output[Optional[int]]:
        """
        The maximum number of VMs that can attach to the disk at the same time. Value greater than one indicates a disk that can be mounted on multiple VMs at the same time.
        """
        return pulumi.get(self, "max_shares")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> pulumi.Output[Optional[str]]:
        """
        The Operating System type.
        """
        return pulumi.get(self, "os_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The disk provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="shareInfo")
    def share_info(self) -> pulumi.Output[Sequence['outputs.ShareInfoElementResponse']]:
        """
        Details of the list of all VMs that have the disk attached. maxShares should be set to a value greater than one for disks to allow attaching them to multiple VMs.
        """
        return pulumi.get(self, "share_info")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.DiskSkuResponse']]:
        """
        The disks sku name. Can be Standard_LRS, Premium_LRS, StandardSSD_LRS, or UltraSSD_LRS.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[str]:
        """
        The time when the disk was created.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> pulumi.Output[str]:
        """
        Unique Guid identifying the resource.
        """
        return pulumi.get(self, "unique_id")

    @property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The Logical zone list for Disk.
        """
        return pulumi.get(self, "zones")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

