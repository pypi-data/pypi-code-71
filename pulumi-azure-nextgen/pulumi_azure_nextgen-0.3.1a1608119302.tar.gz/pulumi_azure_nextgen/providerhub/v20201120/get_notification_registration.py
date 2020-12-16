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
    'GetNotificationRegistrationResult',
    'AwaitableGetNotificationRegistrationResult',
    'get_notification_registration',
]

@pulumi.output_type
class GetNotificationRegistrationResult:
    """
    The notification registration definition.
    """
    def __init__(__self__, id=None, name=None, properties=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.NotificationRegistrationResponseProperties':
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetNotificationRegistrationResult(GetNotificationRegistrationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNotificationRegistrationResult(
            id=self.id,
            name=self.name,
            properties=self.properties,
            type=self.type)


def get_notification_registration(notification_registration_name: Optional[str] = None,
                                  provider_namespace: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNotificationRegistrationResult:
    """
    Use this data source to access information about an existing resource.

    :param str notification_registration_name: The notification registration.
    :param str provider_namespace: The name of the resource provider hosted within ProviderHub.
    """
    __args__ = dict()
    __args__['notificationRegistrationName'] = notification_registration_name
    __args__['providerNamespace'] = provider_namespace
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-nextgen:providerhub/v20201120:getNotificationRegistration', __args__, opts=opts, typ=GetNotificationRegistrationResult).value

    return AwaitableGetNotificationRegistrationResult(
        id=__ret__.id,
        name=__ret__.name,
        properties=__ret__.properties,
        type=__ret__.type)
