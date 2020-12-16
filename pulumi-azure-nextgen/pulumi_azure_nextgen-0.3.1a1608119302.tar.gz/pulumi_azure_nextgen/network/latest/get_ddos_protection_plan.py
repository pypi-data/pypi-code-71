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
    'GetDdosProtectionPlanResult',
    'AwaitableGetDdosProtectionPlanResult',
    'get_ddos_protection_plan',
]

@pulumi.output_type
class GetDdosProtectionPlanResult:
    """
    A DDoS protection plan in a resource group.
    """
    def __init__(__self__, etag=None, id=None, location=None, name=None, provisioning_state=None, resource_guid=None, tags=None, type=None, virtual_networks=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if resource_guid and not isinstance(resource_guid, str):
            raise TypeError("Expected argument 'resource_guid' to be a str")
        pulumi.set(__self__, "resource_guid", resource_guid)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if virtual_networks and not isinstance(virtual_networks, list):
            raise TypeError("Expected argument 'virtual_networks' to be a list")
        pulumi.set(__self__, "virtual_networks", virtual_networks)

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

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
        The provisioning state of the DDoS protection plan resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> str:
        """
        The resource GUID property of the DDoS protection plan resource. It uniquely identifies the resource, even if the user changes its name or migrate the resource across subscriptions or resource groups.
        """
        return pulumi.get(self, "resource_guid")

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

    @property
    @pulumi.getter(name="virtualNetworks")
    def virtual_networks(self) -> Sequence['outputs.SubResourceResponse']:
        """
        The list of virtual networks associated with the DDoS protection plan resource. This list is read-only.
        """
        return pulumi.get(self, "virtual_networks")


class AwaitableGetDdosProtectionPlanResult(GetDdosProtectionPlanResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDdosProtectionPlanResult(
            etag=self.etag,
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            resource_guid=self.resource_guid,
            tags=self.tags,
            type=self.type,
            virtual_networks=self.virtual_networks)


def get_ddos_protection_plan(ddos_protection_plan_name: Optional[str] = None,
                             resource_group_name: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDdosProtectionPlanResult:
    """
    Use this data source to access information about an existing resource.

    :param str ddos_protection_plan_name: The name of the DDoS protection plan.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['ddosProtectionPlanName'] = ddos_protection_plan_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-nextgen:network/latest:getDdosProtectionPlan', __args__, opts=opts, typ=GetDdosProtectionPlanResult).value

    return AwaitableGetDdosProtectionPlanResult(
        etag=__ret__.etag,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        resource_guid=__ret__.resource_guid,
        tags=__ret__.tags,
        type=__ret__.type,
        virtual_networks=__ret__.virtual_networks)
