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
    'GetBlobInventoryPolicyResult',
    'AwaitableGetBlobInventoryPolicyResult',
    'get_blob_inventory_policy',
]

@pulumi.output_type
class GetBlobInventoryPolicyResult:
    """
    The storage account blob inventory policy.
    """
    def __init__(__self__, id=None, last_modified_time=None, name=None, policy=None, system_data=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_modified_time and not isinstance(last_modified_time, str):
            raise TypeError("Expected argument 'last_modified_time' to be a str")
        pulumi.set(__self__, "last_modified_time", last_modified_time)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if policy and not isinstance(policy, dict):
            raise TypeError("Expected argument 'policy' to be a dict")
        pulumi.set(__self__, "policy", policy)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
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
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> str:
        """
        Returns the last modified date and time of the blob inventory policy.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def policy(self) -> 'outputs.BlobInventoryPolicySchemaResponse':
        """
        The storage account blob inventory policy object. It is composed of policy rules.
        """
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetBlobInventoryPolicyResult(GetBlobInventoryPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBlobInventoryPolicyResult(
            id=self.id,
            last_modified_time=self.last_modified_time,
            name=self.name,
            policy=self.policy,
            system_data=self.system_data,
            type=self.type)


def get_blob_inventory_policy(account_name: Optional[str] = None,
                              blob_inventory_policy_name: Optional[str] = None,
                              resource_group_name: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBlobInventoryPolicyResult:
    """
    Use this data source to access information about an existing resource.

    :param str account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :param str blob_inventory_policy_name: The name of the storage account blob inventory policy. It should always be 'default'
    :param str resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['blobInventoryPolicyName'] = blob_inventory_policy_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-nextgen:storage/v20200801preview:getBlobInventoryPolicy', __args__, opts=opts, typ=GetBlobInventoryPolicyResult).value

    return AwaitableGetBlobInventoryPolicyResult(
        id=__ret__.id,
        last_modified_time=__ret__.last_modified_time,
        name=__ret__.name,
        policy=__ret__.policy,
        system_data=__ret__.system_data,
        type=__ret__.type)
