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
    'GetFrontDoorResult',
    'AwaitableGetFrontDoorResult',
    'get_front_door',
]

@pulumi.output_type
class GetFrontDoorResult:
    """
    Front Door represents a collection of backend endpoints to route traffic to along with rules that specify how traffic is sent there.
    """
    def __init__(__self__, backend_pools=None, backend_pools_settings=None, cname=None, enabled_state=None, friendly_name=None, frontdoor_id=None, frontend_endpoints=None, health_probe_settings=None, id=None, load_balancing_settings=None, location=None, name=None, provisioning_state=None, resource_state=None, routing_rules=None, rules_engines=None, tags=None, type=None):
        if backend_pools and not isinstance(backend_pools, list):
            raise TypeError("Expected argument 'backend_pools' to be a list")
        pulumi.set(__self__, "backend_pools", backend_pools)
        if backend_pools_settings and not isinstance(backend_pools_settings, dict):
            raise TypeError("Expected argument 'backend_pools_settings' to be a dict")
        pulumi.set(__self__, "backend_pools_settings", backend_pools_settings)
        if cname and not isinstance(cname, str):
            raise TypeError("Expected argument 'cname' to be a str")
        pulumi.set(__self__, "cname", cname)
        if enabled_state and not isinstance(enabled_state, str):
            raise TypeError("Expected argument 'enabled_state' to be a str")
        pulumi.set(__self__, "enabled_state", enabled_state)
        if friendly_name and not isinstance(friendly_name, str):
            raise TypeError("Expected argument 'friendly_name' to be a str")
        pulumi.set(__self__, "friendly_name", friendly_name)
        if frontdoor_id and not isinstance(frontdoor_id, str):
            raise TypeError("Expected argument 'frontdoor_id' to be a str")
        pulumi.set(__self__, "frontdoor_id", frontdoor_id)
        if frontend_endpoints and not isinstance(frontend_endpoints, list):
            raise TypeError("Expected argument 'frontend_endpoints' to be a list")
        pulumi.set(__self__, "frontend_endpoints", frontend_endpoints)
        if health_probe_settings and not isinstance(health_probe_settings, list):
            raise TypeError("Expected argument 'health_probe_settings' to be a list")
        pulumi.set(__self__, "health_probe_settings", health_probe_settings)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if load_balancing_settings and not isinstance(load_balancing_settings, list):
            raise TypeError("Expected argument 'load_balancing_settings' to be a list")
        pulumi.set(__self__, "load_balancing_settings", load_balancing_settings)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if resource_state and not isinstance(resource_state, str):
            raise TypeError("Expected argument 'resource_state' to be a str")
        pulumi.set(__self__, "resource_state", resource_state)
        if routing_rules and not isinstance(routing_rules, list):
            raise TypeError("Expected argument 'routing_rules' to be a list")
        pulumi.set(__self__, "routing_rules", routing_rules)
        if rules_engines and not isinstance(rules_engines, list):
            raise TypeError("Expected argument 'rules_engines' to be a list")
        pulumi.set(__self__, "rules_engines", rules_engines)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="backendPools")
    def backend_pools(self) -> Optional[Sequence['outputs.BackendPoolResponse']]:
        """
        Backend pools available to routing rules.
        """
        return pulumi.get(self, "backend_pools")

    @property
    @pulumi.getter(name="backendPoolsSettings")
    def backend_pools_settings(self) -> Optional['outputs.BackendPoolsSettingsResponse']:
        """
        Settings for all backendPools
        """
        return pulumi.get(self, "backend_pools_settings")

    @property
    @pulumi.getter
    def cname(self) -> str:
        """
        The host that each frontendEndpoint must CNAME to.
        """
        return pulumi.get(self, "cname")

    @property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> Optional[str]:
        """
        Operational status of the Front Door load balancer. Permitted values are 'Enabled' or 'Disabled'
        """
        return pulumi.get(self, "enabled_state")

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[str]:
        """
        A friendly name for the frontDoor
        """
        return pulumi.get(self, "friendly_name")

    @property
    @pulumi.getter(name="frontdoorId")
    def frontdoor_id(self) -> str:
        """
        The Id of the frontdoor.
        """
        return pulumi.get(self, "frontdoor_id")

    @property
    @pulumi.getter(name="frontendEndpoints")
    def frontend_endpoints(self) -> Optional[Sequence['outputs.FrontendEndpointResponse']]:
        """
        Frontend endpoints available to routing rules.
        """
        return pulumi.get(self, "frontend_endpoints")

    @property
    @pulumi.getter(name="healthProbeSettings")
    def health_probe_settings(self) -> Optional[Sequence['outputs.HealthProbeSettingsModelResponse']]:
        """
        Health probe settings associated with this Front Door instance.
        """
        return pulumi.get(self, "health_probe_settings")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="loadBalancingSettings")
    def load_balancing_settings(self) -> Optional[Sequence['outputs.LoadBalancingSettingsModelResponse']]:
        """
        Load balancing settings associated with this Front Door instance.
        """
        return pulumi.get(self, "load_balancing_settings")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the Front Door.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> str:
        """
        Resource status of the Front Door.
        """
        return pulumi.get(self, "resource_state")

    @property
    @pulumi.getter(name="routingRules")
    def routing_rules(self) -> Optional[Sequence['outputs.RoutingRuleResponse']]:
        """
        Routing rules associated with this Front Door.
        """
        return pulumi.get(self, "routing_rules")

    @property
    @pulumi.getter(name="rulesEngines")
    def rules_engines(self) -> Sequence['outputs.RulesEngineResponse']:
        """
        Rules Engine Configurations available to routing rules.
        """
        return pulumi.get(self, "rules_engines")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetFrontDoorResult(GetFrontDoorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFrontDoorResult(
            backend_pools=self.backend_pools,
            backend_pools_settings=self.backend_pools_settings,
            cname=self.cname,
            enabled_state=self.enabled_state,
            friendly_name=self.friendly_name,
            frontdoor_id=self.frontdoor_id,
            frontend_endpoints=self.frontend_endpoints,
            health_probe_settings=self.health_probe_settings,
            id=self.id,
            load_balancing_settings=self.load_balancing_settings,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            resource_state=self.resource_state,
            routing_rules=self.routing_rules,
            rules_engines=self.rules_engines,
            tags=self.tags,
            type=self.type)


def get_front_door(front_door_name: Optional[str] = None,
                   resource_group_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFrontDoorResult:
    """
    Use this data source to access information about an existing resource.

    :param str front_door_name: Name of the Front Door which is globally unique.
    :param str resource_group_name: Name of the Resource group within the Azure subscription.
    """
    __args__ = dict()
    __args__['frontDoorName'] = front_door_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-nextgen:network/v20200501:getFrontDoor', __args__, opts=opts, typ=GetFrontDoorResult).value

    return AwaitableGetFrontDoorResult(
        backend_pools=__ret__.backend_pools,
        backend_pools_settings=__ret__.backend_pools_settings,
        cname=__ret__.cname,
        enabled_state=__ret__.enabled_state,
        friendly_name=__ret__.friendly_name,
        frontdoor_id=__ret__.frontdoor_id,
        frontend_endpoints=__ret__.frontend_endpoints,
        health_probe_settings=__ret__.health_probe_settings,
        id=__ret__.id,
        load_balancing_settings=__ret__.load_balancing_settings,
        location=__ret__.location,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        resource_state=__ret__.resource_state,
        routing_rules=__ret__.routing_rules,
        rules_engines=__ret__.rules_engines,
        tags=__ret__.tags,
        type=__ret__.type)
