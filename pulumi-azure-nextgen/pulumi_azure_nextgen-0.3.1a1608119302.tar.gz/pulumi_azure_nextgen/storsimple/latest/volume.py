# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables
from ._enums import *

__all__ = ['Volume']


class Volume(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_control_record_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 device_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input['Kind']] = None,
                 manager_name: Optional[pulumi.Input[str]] = None,
                 monitoring_status: Optional[pulumi.Input['MonitoringStatus']] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 size_in_bytes: Optional[pulumi.Input[int]] = None,
                 volume_container_name: Optional[pulumi.Input[str]] = None,
                 volume_name: Optional[pulumi.Input[str]] = None,
                 volume_status: Optional[pulumi.Input['VolumeStatus']] = None,
                 volume_type: Optional[pulumi.Input['VolumeType']] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        The volume.
        Latest API Version: 2017-06-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] access_control_record_ids: The IDs of the access control records, associated with the volume.
        :param pulumi.Input[str] device_name: The device name
        :param pulumi.Input['Kind'] kind: The Kind of the object. Currently only Series8000 is supported
        :param pulumi.Input[str] manager_name: The manager name
        :param pulumi.Input['MonitoringStatus'] monitoring_status: The monitoring status of the volume.
        :param pulumi.Input[str] resource_group_name: The resource group name
        :param pulumi.Input[int] size_in_bytes: The size of the volume in bytes.
        :param pulumi.Input[str] volume_container_name: The volume container name.
        :param pulumi.Input[str] volume_name: The volume name.
        :param pulumi.Input['VolumeStatus'] volume_status: The volume status.
        :param pulumi.Input['VolumeType'] volume_type: The type of the volume.
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

            if access_control_record_ids is None and not opts.urn:
                raise TypeError("Missing required property 'access_control_record_ids'")
            __props__['access_control_record_ids'] = access_control_record_ids
            if device_name is None and not opts.urn:
                raise TypeError("Missing required property 'device_name'")
            __props__['device_name'] = device_name
            __props__['kind'] = kind
            if manager_name is None and not opts.urn:
                raise TypeError("Missing required property 'manager_name'")
            __props__['manager_name'] = manager_name
            if monitoring_status is None and not opts.urn:
                raise TypeError("Missing required property 'monitoring_status'")
            __props__['monitoring_status'] = monitoring_status
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            if size_in_bytes is None and not opts.urn:
                raise TypeError("Missing required property 'size_in_bytes'")
            __props__['size_in_bytes'] = size_in_bytes
            if volume_container_name is None and not opts.urn:
                raise TypeError("Missing required property 'volume_container_name'")
            __props__['volume_container_name'] = volume_container_name
            if volume_name is None and not opts.urn:
                raise TypeError("Missing required property 'volume_name'")
            __props__['volume_name'] = volume_name
            if volume_status is None and not opts.urn:
                raise TypeError("Missing required property 'volume_status'")
            __props__['volume_status'] = volume_status
            if volume_type is None and not opts.urn:
                raise TypeError("Missing required property 'volume_type'")
            __props__['volume_type'] = volume_type
            __props__['backup_policy_ids'] = None
            __props__['backup_status'] = None
            __props__['name'] = None
            __props__['operation_status'] = None
            __props__['type'] = None
            __props__['volume_container_id'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:storsimple/v20170601:Volume")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Volume, __self__).__init__(
            'azure-nextgen:storsimple/latest:Volume',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Volume':
        """
        Get an existing Volume resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return Volume(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessControlRecordIds")
    def access_control_record_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        The IDs of the access control records, associated with the volume.
        """
        return pulumi.get(self, "access_control_record_ids")

    @property
    @pulumi.getter(name="backupPolicyIds")
    def backup_policy_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        The IDs of the backup policies, in which this volume is part of.
        """
        return pulumi.get(self, "backup_policy_ids")

    @property
    @pulumi.getter(name="backupStatus")
    def backup_status(self) -> pulumi.Output[str]:
        """
        The backup status of the volume.
        """
        return pulumi.get(self, "backup_status")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        The Kind of the object. Currently only Series8000 is supported
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="monitoringStatus")
    def monitoring_status(self) -> pulumi.Output[str]:
        """
        The monitoring status of the volume.
        """
        return pulumi.get(self, "monitoring_status")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the object.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="operationStatus")
    def operation_status(self) -> pulumi.Output[str]:
        """
        The operation status on the volume.
        """
        return pulumi.get(self, "operation_status")

    @property
    @pulumi.getter(name="sizeInBytes")
    def size_in_bytes(self) -> pulumi.Output[int]:
        """
        The size of the volume in bytes.
        """
        return pulumi.get(self, "size_in_bytes")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The hierarchical type of the object.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="volumeContainerId")
    def volume_container_id(self) -> pulumi.Output[str]:
        """
        The ID of the volume container, in which this volume is created.
        """
        return pulumi.get(self, "volume_container_id")

    @property
    @pulumi.getter(name="volumeStatus")
    def volume_status(self) -> pulumi.Output[str]:
        """
        The volume status.
        """
        return pulumi.get(self, "volume_status")

    @property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> pulumi.Output[str]:
        """
        The type of the volume.
        """
        return pulumi.get(self, "volume_type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

