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

__all__ = ['FrontDoor']


class FrontDoor(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backend_pools: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BackendPoolArgs']]]]] = None,
                 backend_pools_settings: Optional[pulumi.Input[pulumi.InputType['BackendPoolsSettingsArgs']]] = None,
                 enabled_state: Optional[pulumi.Input[Union[str, 'FrontDoorEnabledState']]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 front_door_name: Optional[pulumi.Input[str]] = None,
                 frontend_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FrontendEndpointArgs']]]]] = None,
                 health_probe_settings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HealthProbeSettingsModelArgs']]]]] = None,
                 load_balancing_settings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LoadBalancingSettingsModelArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 routing_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoutingRuleArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Front Door represents a collection of backend endpoints to route traffic to along with rules that specify how traffic is sent there.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BackendPoolArgs']]]] backend_pools: Backend pools available to routing rules.
        :param pulumi.Input[pulumi.InputType['BackendPoolsSettingsArgs']] backend_pools_settings: Settings for all backendPools
        :param pulumi.Input[Union[str, 'FrontDoorEnabledState']] enabled_state: Operational status of the Front Door load balancer. Permitted values are 'Enabled' or 'Disabled'
        :param pulumi.Input[str] friendly_name: A friendly name for the frontDoor
        :param pulumi.Input[str] front_door_name: Name of the Front Door which is globally unique.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FrontendEndpointArgs']]]] frontend_endpoints: Frontend endpoints available to routing rules.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HealthProbeSettingsModelArgs']]]] health_probe_settings: Health probe settings associated with this Front Door instance.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LoadBalancingSettingsModelArgs']]]] load_balancing_settings: Load balancing settings associated with this Front Door instance.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoutingRuleArgs']]]] routing_rules: Routing rules associated with this Front Door.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
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

            __props__['backend_pools'] = backend_pools
            __props__['backend_pools_settings'] = backend_pools_settings
            __props__['enabled_state'] = enabled_state
            __props__['friendly_name'] = friendly_name
            if front_door_name is None and not opts.urn:
                raise TypeError("Missing required property 'front_door_name'")
            __props__['front_door_name'] = front_door_name
            __props__['frontend_endpoints'] = frontend_endpoints
            __props__['health_probe_settings'] = health_probe_settings
            __props__['load_balancing_settings'] = load_balancing_settings
            __props__['location'] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['routing_rules'] = routing_rules
            __props__['tags'] = tags
            __props__['cname'] = None
            __props__['frontdoor_id'] = None
            __props__['name'] = None
            __props__['provisioning_state'] = None
            __props__['resource_state'] = None
            __props__['rules_engines'] = None
            __props__['type'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:network/latest:FrontDoor"), pulumi.Alias(type_="azure-nextgen:network/v20180801:FrontDoor"), pulumi.Alias(type_="azure-nextgen:network/v20190401:FrontDoor"), pulumi.Alias(type_="azure-nextgen:network/v20190501:FrontDoor"), pulumi.Alias(type_="azure-nextgen:network/v20200101:FrontDoor"), pulumi.Alias(type_="azure-nextgen:network/v20200401:FrontDoor")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(FrontDoor, __self__).__init__(
            'azure-nextgen:network/v20200501:FrontDoor',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'FrontDoor':
        """
        Get an existing FrontDoor resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return FrontDoor(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="backendPools")
    def backend_pools(self) -> pulumi.Output[Optional[Sequence['outputs.BackendPoolResponse']]]:
        """
        Backend pools available to routing rules.
        """
        return pulumi.get(self, "backend_pools")

    @property
    @pulumi.getter(name="backendPoolsSettings")
    def backend_pools_settings(self) -> pulumi.Output[Optional['outputs.BackendPoolsSettingsResponse']]:
        """
        Settings for all backendPools
        """
        return pulumi.get(self, "backend_pools_settings")

    @property
    @pulumi.getter
    def cname(self) -> pulumi.Output[str]:
        """
        The host that each frontendEndpoint must CNAME to.
        """
        return pulumi.get(self, "cname")

    @property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> pulumi.Output[Optional[str]]:
        """
        Operational status of the Front Door load balancer. Permitted values are 'Enabled' or 'Disabled'
        """
        return pulumi.get(self, "enabled_state")

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> pulumi.Output[Optional[str]]:
        """
        A friendly name for the frontDoor
        """
        return pulumi.get(self, "friendly_name")

    @property
    @pulumi.getter(name="frontdoorId")
    def frontdoor_id(self) -> pulumi.Output[str]:
        """
        The Id of the frontdoor.
        """
        return pulumi.get(self, "frontdoor_id")

    @property
    @pulumi.getter(name="frontendEndpoints")
    def frontend_endpoints(self) -> pulumi.Output[Optional[Sequence['outputs.FrontendEndpointResponse']]]:
        """
        Frontend endpoints available to routing rules.
        """
        return pulumi.get(self, "frontend_endpoints")

    @property
    @pulumi.getter(name="healthProbeSettings")
    def health_probe_settings(self) -> pulumi.Output[Optional[Sequence['outputs.HealthProbeSettingsModelResponse']]]:
        """
        Health probe settings associated with this Front Door instance.
        """
        return pulumi.get(self, "health_probe_settings")

    @property
    @pulumi.getter(name="loadBalancingSettings")
    def load_balancing_settings(self) -> pulumi.Output[Optional[Sequence['outputs.LoadBalancingSettingsModelResponse']]]:
        """
        Load balancing settings associated with this Front Door instance.
        """
        return pulumi.get(self, "load_balancing_settings")

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
        Provisioning state of the Front Door.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> pulumi.Output[str]:
        """
        Resource status of the Front Door.
        """
        return pulumi.get(self, "resource_state")

    @property
    @pulumi.getter(name="routingRules")
    def routing_rules(self) -> pulumi.Output[Optional[Sequence['outputs.RoutingRuleResponse']]]:
        """
        Routing rules associated with this Front Door.
        """
        return pulumi.get(self, "routing_rules")

    @property
    @pulumi.getter(name="rulesEngines")
    def rules_engines(self) -> pulumi.Output[Sequence['outputs.RulesEngineResponse']]:
        """
        Rules Engine Configurations available to routing rules.
        """
        return pulumi.get(self, "rules_engines")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

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

