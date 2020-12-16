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

__all__ = ['PacketCapture']


class PacketCapture(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bytes_to_capture_per_packet: Optional[pulumi.Input[int]] = None,
                 filters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PacketCaptureFilterArgs']]]]] = None,
                 network_watcher_name: Optional[pulumi.Input[str]] = None,
                 packet_capture_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_location: Optional[pulumi.Input[pulumi.InputType['PacketCaptureStorageLocationArgs']]] = None,
                 target: Optional[pulumi.Input[str]] = None,
                 time_limit_in_seconds: Optional[pulumi.Input[int]] = None,
                 total_bytes_per_session: Optional[pulumi.Input[int]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Information about packet capture session.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] bytes_to_capture_per_packet: Number of bytes captured per packet, the remaining bytes are truncated.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PacketCaptureFilterArgs']]]] filters: A list of packet capture filters.
        :param pulumi.Input[str] network_watcher_name: The name of the network watcher.
        :param pulumi.Input[str] packet_capture_name: The name of the packet capture session.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[pulumi.InputType['PacketCaptureStorageLocationArgs']] storage_location: The storage location for a packet capture session.
        :param pulumi.Input[str] target: The ID of the targeted resource, only VM is currently supported.
        :param pulumi.Input[int] time_limit_in_seconds: Maximum duration of the capture session in seconds.
        :param pulumi.Input[int] total_bytes_per_session: Maximum size of the capture output.
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

            __props__['bytes_to_capture_per_packet'] = bytes_to_capture_per_packet
            __props__['filters'] = filters
            if network_watcher_name is None and not opts.urn:
                raise TypeError("Missing required property 'network_watcher_name'")
            __props__['network_watcher_name'] = network_watcher_name
            if packet_capture_name is None and not opts.urn:
                raise TypeError("Missing required property 'packet_capture_name'")
            __props__['packet_capture_name'] = packet_capture_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            if storage_location is None and not opts.urn:
                raise TypeError("Missing required property 'storage_location'")
            __props__['storage_location'] = storage_location
            if target is None and not opts.urn:
                raise TypeError("Missing required property 'target'")
            __props__['target'] = target
            __props__['time_limit_in_seconds'] = time_limit_in_seconds
            __props__['total_bytes_per_session'] = total_bytes_per_session
            __props__['etag'] = None
            __props__['name'] = None
            __props__['provisioning_state'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:network/latest:PacketCapture"), pulumi.Alias(type_="azure-nextgen:network/v20160901:PacketCapture"), pulumi.Alias(type_="azure-nextgen:network/v20161201:PacketCapture"), pulumi.Alias(type_="azure-nextgen:network/v20170301:PacketCapture"), pulumi.Alias(type_="azure-nextgen:network/v20170601:PacketCapture"), pulumi.Alias(type_="azure-nextgen:network/v20170801:PacketCapture"), pulumi.Alias(type_="azure-nextgen:network/v20170901:PacketCapture"), pulumi.Alias(type_="azure-nextgen:network/v20171001:PacketCapture"), pulumi.Alias(type_="azure-nextgen:network/v20171101:PacketCapture"), pulumi.Alias(type_="azure-nextgen:network/v20180101:PacketCapture"), pulumi.Alias(type_="azure-nextgen:network/v20180201:PacketCapture"), pulumi.Alias(type_="azure-nextgen:network/v20180401:PacketCapture"), pulumi.Alias(type_="azure-nextgen:network/v20180601:PacketCapture"), pulumi.Alias(type_="azure-nextgen:network/v20180701:PacketCapture"), pulumi.Alias(type_="azure-nextgen:network/v20180801:PacketCapture"), pulumi.Alias(type_="azure-nextgen:network/v20181001:PacketCapture"), pulumi.Alias(type_="azure-nextgen:network/v20181101:PacketCapture"), pulumi.Alias(type_="azure-nextgen:network/v20181201:PacketCapture"), pulumi.Alias(type_="azure-nextgen:network/v20190201:PacketCapture"), pulumi.Alias(type_="azure-nextgen:network/v20190401:PacketCapture"), pulumi.Alias(type_="azure-nextgen:network/v20190601:PacketCapture"), pulumi.Alias(type_="azure-nextgen:network/v20190701:PacketCapture"), pulumi.Alias(type_="azure-nextgen:network/v20190801:PacketCapture"), pulumi.Alias(type_="azure-nextgen:network/v20190901:PacketCapture"), pulumi.Alias(type_="azure-nextgen:network/v20191101:PacketCapture"), pulumi.Alias(type_="azure-nextgen:network/v20191201:PacketCapture"), pulumi.Alias(type_="azure-nextgen:network/v20200301:PacketCapture"), pulumi.Alias(type_="azure-nextgen:network/v20200401:PacketCapture"), pulumi.Alias(type_="azure-nextgen:network/v20200501:PacketCapture"), pulumi.Alias(type_="azure-nextgen:network/v20200701:PacketCapture")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PacketCapture, __self__).__init__(
            'azure-nextgen:network/v20200601:PacketCapture',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PacketCapture':
        """
        Get an existing PacketCapture resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return PacketCapture(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bytesToCapturePerPacket")
    def bytes_to_capture_per_packet(self) -> pulumi.Output[Optional[int]]:
        """
        Number of bytes captured per packet, the remaining bytes are truncated.
        """
        return pulumi.get(self, "bytes_to_capture_per_packet")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def filters(self) -> pulumi.Output[Optional[Sequence['outputs.PacketCaptureFilterResponse']]]:
        """
        A list of packet capture filters.
        """
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the packet capture session.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the packet capture session.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="storageLocation")
    def storage_location(self) -> pulumi.Output['outputs.PacketCaptureStorageLocationResponse']:
        """
        The storage location for a packet capture session.
        """
        return pulumi.get(self, "storage_location")

    @property
    @pulumi.getter
    def target(self) -> pulumi.Output[str]:
        """
        The ID of the targeted resource, only VM is currently supported.
        """
        return pulumi.get(self, "target")

    @property
    @pulumi.getter(name="timeLimitInSeconds")
    def time_limit_in_seconds(self) -> pulumi.Output[Optional[int]]:
        """
        Maximum duration of the capture session in seconds.
        """
        return pulumi.get(self, "time_limit_in_seconds")

    @property
    @pulumi.getter(name="totalBytesPerSession")
    def total_bytes_per_session(self) -> pulumi.Output[Optional[int]]:
        """
        Maximum size of the capture output.
        """
        return pulumi.get(self, "total_bytes_per_session")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

