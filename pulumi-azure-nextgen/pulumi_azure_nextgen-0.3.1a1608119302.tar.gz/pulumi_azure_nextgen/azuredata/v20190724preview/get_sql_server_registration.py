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
    'GetSqlServerRegistrationResult',
    'AwaitableGetSqlServerRegistrationResult',
    'get_sql_server_registration',
]

@pulumi.output_type
class GetSqlServerRegistrationResult:
    """
    A SQL server registration.
    """
    def __init__(__self__, id=None, location=None, name=None, property_bag=None, resource_group=None, subscription_id=None, system_data=None, tags=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if property_bag and not isinstance(property_bag, str):
            raise TypeError("Expected argument 'property_bag' to be a str")
        pulumi.set(__self__, "property_bag", property_bag)
        if resource_group and not isinstance(resource_group, str):
            raise TypeError("Expected argument 'resource_group' to be a str")
        pulumi.set(__self__, "resource_group", resource_group)
        if subscription_id and not isinstance(subscription_id, str):
            raise TypeError("Expected argument 'subscription_id' to be a str")
        pulumi.set(__self__, "subscription_id", subscription_id)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource Id for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="propertyBag")
    def property_bag(self) -> Optional[str]:
        """
        Optional Properties as JSON string
        """
        return pulumi.get(self, "property_bag")

    @property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[str]:
        """
        Resource Group Name
        """
        return pulumi.get(self, "resource_group")

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[str]:
        """
        Subscription Id
        """
        return pulumi.get(self, "subscription_id")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Read only system data
        """
        return pulumi.get(self, "system_data")

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
        The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
        """
        return pulumi.get(self, "type")


class AwaitableGetSqlServerRegistrationResult(GetSqlServerRegistrationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSqlServerRegistrationResult(
            id=self.id,
            location=self.location,
            name=self.name,
            property_bag=self.property_bag,
            resource_group=self.resource_group,
            subscription_id=self.subscription_id,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_sql_server_registration(resource_group_name: Optional[str] = None,
                                sql_server_registration_name: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSqlServerRegistrationResult:
    """
    Use this data source to access information about an existing resource.

    :param str resource_group_name: Name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str sql_server_registration_name: Name of the SQL Server registration.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['sqlServerRegistrationName'] = sql_server_registration_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-nextgen:azuredata/v20190724preview:getSqlServerRegistration', __args__, opts=opts, typ=GetSqlServerRegistrationResult).value

    return AwaitableGetSqlServerRegistrationResult(
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        property_bag=__ret__.property_bag,
        resource_group=__ret__.resource_group,
        subscription_id=__ret__.subscription_id,
        system_data=__ret__.system_data,
        tags=__ret__.tags,
        type=__ret__.type)
