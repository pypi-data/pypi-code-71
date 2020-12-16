# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['ConnectionMonitor']


class ConnectionMonitor(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_start: Optional[pulumi.Input[bool]] = None,
                 connection_monitor_name: Optional[pulumi.Input[str]] = None,
                 destination: Optional[pulumi.Input[pulumi.InputType['ConnectionMonitorDestinationArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 monitoring_interval_in_seconds: Optional[pulumi.Input[int]] = None,
                 network_watcher_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[pulumi.InputType['ConnectionMonitorSourceArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Information about the connection monitor.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] auto_start: Determines if the connection monitor will start automatically once created.
        :param pulumi.Input[str] connection_monitor_name: The name of the connection monitor.
        :param pulumi.Input[pulumi.InputType['ConnectionMonitorDestinationArgs']] destination: Describes the destination of connection monitor.
        :param pulumi.Input[str] location: Connection monitor location.
        :param pulumi.Input[int] monitoring_interval_in_seconds: Monitoring interval in seconds.
        :param pulumi.Input[str] network_watcher_name: The name of the Network Watcher resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group containing Network Watcher.
        :param pulumi.Input[pulumi.InputType['ConnectionMonitorSourceArgs']] source: Describes the source of connection monitor.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Connection monitor tags.
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

            __props__['auto_start'] = auto_start
            if connection_monitor_name is None and not opts.urn:
                raise TypeError("Missing required property 'connection_monitor_name'")
            __props__['connection_monitor_name'] = connection_monitor_name
            if destination is None and not opts.urn:
                raise TypeError("Missing required property 'destination'")
            __props__['destination'] = destination
            __props__['location'] = location
            __props__['monitoring_interval_in_seconds'] = monitoring_interval_in_seconds
            if network_watcher_name is None and not opts.urn:
                raise TypeError("Missing required property 'network_watcher_name'")
            __props__['network_watcher_name'] = network_watcher_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            if source is None and not opts.urn:
                raise TypeError("Missing required property 'source'")
            __props__['source'] = source
            __props__['tags'] = tags
            __props__['etag'] = None
            __props__['monitoring_status'] = None
            __props__['name'] = None
            __props__['provisioning_state'] = None
            __props__['start_time'] = None
            __props__['type'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:network/latest:ConnectionMonitor"), pulumi.Alias(type_="azure-nextgen:network/v20171001:ConnectionMonitor"), pulumi.Alias(type_="azure-nextgen:network/v20171101:ConnectionMonitor"), pulumi.Alias(type_="azure-nextgen:network/v20180101:ConnectionMonitor"), pulumi.Alias(type_="azure-nextgen:network/v20180201:ConnectionMonitor"), pulumi.Alias(type_="azure-nextgen:network/v20180401:ConnectionMonitor"), pulumi.Alias(type_="azure-nextgen:network/v20180701:ConnectionMonitor"), pulumi.Alias(type_="azure-nextgen:network/v20180801:ConnectionMonitor"), pulumi.Alias(type_="azure-nextgen:network/v20181001:ConnectionMonitor"), pulumi.Alias(type_="azure-nextgen:network/v20181101:ConnectionMonitor"), pulumi.Alias(type_="azure-nextgen:network/v20181201:ConnectionMonitor"), pulumi.Alias(type_="azure-nextgen:network/v20190201:ConnectionMonitor"), pulumi.Alias(type_="azure-nextgen:network/v20190401:ConnectionMonitor"), pulumi.Alias(type_="azure-nextgen:network/v20190601:ConnectionMonitor"), pulumi.Alias(type_="azure-nextgen:network/v20190701:ConnectionMonitor"), pulumi.Alias(type_="azure-nextgen:network/v20190801:ConnectionMonitor"), pulumi.Alias(type_="azure-nextgen:network/v20190901:ConnectionMonitor"), pulumi.Alias(type_="azure-nextgen:network/v20191101:ConnectionMonitor"), pulumi.Alias(type_="azure-nextgen:network/v20191201:ConnectionMonitor"), pulumi.Alias(type_="azure-nextgen:network/v20200301:ConnectionMonitor"), pulumi.Alias(type_="azure-nextgen:network/v20200401:ConnectionMonitor"), pulumi.Alias(type_="azure-nextgen:network/v20200501:ConnectionMonitor"), pulumi.Alias(type_="azure-nextgen:network/v20200601:ConnectionMonitor"), pulumi.Alias(type_="azure-nextgen:network/v20200701:ConnectionMonitor")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ConnectionMonitor, __self__).__init__(
            'azure-nextgen:network/v20180601:ConnectionMonitor',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ConnectionMonitor':
        """
        Get an existing ConnectionMonitor resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return ConnectionMonitor(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autoStart")
    def auto_start(self) -> pulumi.Output[Optional[bool]]:
        """
        Determines if the connection monitor will start automatically once created.
        """
        return pulumi.get(self, "auto_start")

    @property
    @pulumi.getter
    def destination(self) -> pulumi.Output['outputs.ConnectionMonitorDestinationResponse']:
        """
        Describes the destination of connection monitor.
        """
        return pulumi.get(self, "destination")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Connection monitor location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="monitoringIntervalInSeconds")
    def monitoring_interval_in_seconds(self) -> pulumi.Output[Optional[int]]:
        """
        Monitoring interval in seconds.
        """
        return pulumi.get(self, "monitoring_interval_in_seconds")

    @property
    @pulumi.getter(name="monitoringStatus")
    def monitoring_status(self) -> pulumi.Output[Optional[str]]:
        """
        The monitoring status of the connection monitor.
        """
        return pulumi.get(self, "monitoring_status")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the connection monitor.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        The provisioning state of the connection monitor.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output['outputs.ConnectionMonitorSourceResponse']:
        """
        Describes the source of connection monitor.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Output[Optional[str]]:
        """
        The date and time when the connection monitor was started.
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Connection monitor tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Connection monitor type.
        """
        return pulumi.get(self, "type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

