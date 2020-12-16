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
    'GetManagementGroupSubscriptionResult',
    'AwaitableGetManagementGroupSubscriptionResult',
    'get_management_group_subscription',
]

@pulumi.output_type
class GetManagementGroupSubscriptionResult:
    """
    The details of subscription under management group.
    """
    def __init__(__self__, display_name=None, id=None, name=None, parent=None, state=None, tenant=None, type=None):
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if parent and not isinstance(parent, dict):
            raise TypeError("Expected argument 'parent' to be a dict")
        pulumi.set(__self__, "parent", parent)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if tenant and not isinstance(tenant, str):
            raise TypeError("Expected argument 'tenant' to be a str")
        pulumi.set(__self__, "tenant", tenant)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The friendly name of the subscription.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The fully qualified ID for the subscription.  For example, /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000/subscriptions/0000000-0000-0000-0000-000000000001
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The stringified id of the subscription. For example, 00000000-0000-0000-0000-000000000000
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parent(self) -> Optional['outputs.DescendantParentGroupInfoResponse']:
        """
        The ID of the parent management group.
        """
        return pulumi.get(self, "parent")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The state of the subscription.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tenant(self) -> Optional[str]:
        """
        The AAD Tenant ID associated with the subscription. For example, 00000000-0000-0000-0000-000000000000
        """
        return pulumi.get(self, "tenant")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource.  For example, Microsoft.Management/managementGroups/subscriptions
        """
        return pulumi.get(self, "type")


class AwaitableGetManagementGroupSubscriptionResult(GetManagementGroupSubscriptionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagementGroupSubscriptionResult(
            display_name=self.display_name,
            id=self.id,
            name=self.name,
            parent=self.parent,
            state=self.state,
            tenant=self.tenant,
            type=self.type)


def get_management_group_subscription(group_id: Optional[str] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagementGroupSubscriptionResult:
    """
    Use this data source to access information about an existing resource.

    :param str group_id: Management Group ID.
    """
    __args__ = dict()
    __args__['groupId'] = group_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-nextgen:management/latest:getManagementGroupSubscription', __args__, opts=opts, typ=GetManagementGroupSubscriptionResult).value

    return AwaitableGetManagementGroupSubscriptionResult(
        display_name=__ret__.display_name,
        id=__ret__.id,
        name=__ret__.name,
        parent=__ret__.parent,
        state=__ret__.state,
        tenant=__ret__.tenant,
        type=__ret__.type)
