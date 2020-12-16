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

__all__ = ['FlowLog']


class FlowLog(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 flow_analytics_configuration: Optional[pulumi.Input[pulumi.InputType['TrafficAnalyticsPropertiesArgs']]] = None,
                 flow_log_name: Optional[pulumi.Input[str]] = None,
                 format: Optional[pulumi.Input[pulumi.InputType['FlowLogFormatParametersArgs']]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_watcher_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 retention_policy: Optional[pulumi.Input[pulumi.InputType['RetentionPolicyParametersArgs']]] = None,
                 storage_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_resource_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        A flow log resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enabled: Flag to enable/disable flow logging.
        :param pulumi.Input[pulumi.InputType['TrafficAnalyticsPropertiesArgs']] flow_analytics_configuration: Parameters that define the configuration of traffic analytics.
        :param pulumi.Input[str] flow_log_name: The name of the flow log.
        :param pulumi.Input[pulumi.InputType['FlowLogFormatParametersArgs']] format: Parameters that define the flow log format.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] network_watcher_name: The name of the network watcher.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[pulumi.InputType['RetentionPolicyParametersArgs']] retention_policy: Parameters that define the retention policy for flow log.
        :param pulumi.Input[str] storage_id: ID of the storage account which is used to store the flow log.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] target_resource_id: ID of network security group to which flow log will be applied.
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

            __props__['enabled'] = enabled
            __props__['flow_analytics_configuration'] = flow_analytics_configuration
            if flow_log_name is None and not opts.urn:
                raise TypeError("Missing required property 'flow_log_name'")
            __props__['flow_log_name'] = flow_log_name
            __props__['format'] = format
            __props__['id'] = id
            __props__['location'] = location
            if network_watcher_name is None and not opts.urn:
                raise TypeError("Missing required property 'network_watcher_name'")
            __props__['network_watcher_name'] = network_watcher_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['retention_policy'] = retention_policy
            if storage_id is None and not opts.urn:
                raise TypeError("Missing required property 'storage_id'")
            __props__['storage_id'] = storage_id
            __props__['tags'] = tags
            if target_resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'target_resource_id'")
            __props__['target_resource_id'] = target_resource_id
            __props__['etag'] = None
            __props__['name'] = None
            __props__['provisioning_state'] = None
            __props__['target_resource_guid'] = None
            __props__['type'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:network/latest:FlowLog"), pulumi.Alias(type_="azure-nextgen:network/v20191201:FlowLog"), pulumi.Alias(type_="azure-nextgen:network/v20200301:FlowLog"), pulumi.Alias(type_="azure-nextgen:network/v20200401:FlowLog"), pulumi.Alias(type_="azure-nextgen:network/v20200501:FlowLog"), pulumi.Alias(type_="azure-nextgen:network/v20200601:FlowLog"), pulumi.Alias(type_="azure-nextgen:network/v20200701:FlowLog")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(FlowLog, __self__).__init__(
            'azure-nextgen:network/v20191101:FlowLog',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'FlowLog':
        """
        Get an existing FlowLog resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return FlowLog(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Flag to enable/disable flow logging.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="flowAnalyticsConfiguration")
    def flow_analytics_configuration(self) -> pulumi.Output[Optional['outputs.TrafficAnalyticsPropertiesResponse']]:
        """
        Parameters that define the configuration of traffic analytics.
        """
        return pulumi.get(self, "flow_analytics_configuration")

    @property
    @pulumi.getter
    def format(self) -> pulumi.Output[Optional['outputs.FlowLogFormatParametersResponse']]:
        """
        Parameters that define the flow log format.
        """
        return pulumi.get(self, "format")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the flow log.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(self) -> pulumi.Output[Optional['outputs.RetentionPolicyParametersResponse']]:
        """
        Parameters that define the retention policy for flow log.
        """
        return pulumi.get(self, "retention_policy")

    @property
    @pulumi.getter(name="storageId")
    def storage_id(self) -> pulumi.Output[str]:
        """
        ID of the storage account which is used to store the flow log.
        """
        return pulumi.get(self, "storage_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetResourceGuid")
    def target_resource_guid(self) -> pulumi.Output[str]:
        """
        Guid of network security group to which flow log will be applied.
        """
        return pulumi.get(self, "target_resource_guid")

    @property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> pulumi.Output[str]:
        """
        ID of network security group to which flow log will be applied.
        """
        return pulumi.get(self, "target_resource_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

