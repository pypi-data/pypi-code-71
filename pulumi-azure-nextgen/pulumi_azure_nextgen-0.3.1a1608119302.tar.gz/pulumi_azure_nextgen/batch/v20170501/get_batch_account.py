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
    'GetBatchAccountResult',
    'AwaitableGetBatchAccountResult',
    'get_batch_account',
]

@pulumi.output_type
class GetBatchAccountResult:
    """
    Contains information about an Azure Batch account.
    """
    def __init__(__self__, account_endpoint=None, active_job_and_job_schedule_quota=None, auto_storage=None, dedicated_core_quota=None, id=None, key_vault_reference=None, location=None, low_priority_core_quota=None, name=None, pool_allocation_mode=None, pool_quota=None, provisioning_state=None, tags=None, type=None):
        if account_endpoint and not isinstance(account_endpoint, str):
            raise TypeError("Expected argument 'account_endpoint' to be a str")
        pulumi.set(__self__, "account_endpoint", account_endpoint)
        if active_job_and_job_schedule_quota and not isinstance(active_job_and_job_schedule_quota, int):
            raise TypeError("Expected argument 'active_job_and_job_schedule_quota' to be a int")
        pulumi.set(__self__, "active_job_and_job_schedule_quota", active_job_and_job_schedule_quota)
        if auto_storage and not isinstance(auto_storage, dict):
            raise TypeError("Expected argument 'auto_storage' to be a dict")
        pulumi.set(__self__, "auto_storage", auto_storage)
        if dedicated_core_quota and not isinstance(dedicated_core_quota, int):
            raise TypeError("Expected argument 'dedicated_core_quota' to be a int")
        pulumi.set(__self__, "dedicated_core_quota", dedicated_core_quota)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if key_vault_reference and not isinstance(key_vault_reference, dict):
            raise TypeError("Expected argument 'key_vault_reference' to be a dict")
        pulumi.set(__self__, "key_vault_reference", key_vault_reference)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if low_priority_core_quota and not isinstance(low_priority_core_quota, int):
            raise TypeError("Expected argument 'low_priority_core_quota' to be a int")
        pulumi.set(__self__, "low_priority_core_quota", low_priority_core_quota)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if pool_allocation_mode and not isinstance(pool_allocation_mode, str):
            raise TypeError("Expected argument 'pool_allocation_mode' to be a str")
        pulumi.set(__self__, "pool_allocation_mode", pool_allocation_mode)
        if pool_quota and not isinstance(pool_quota, int):
            raise TypeError("Expected argument 'pool_quota' to be a int")
        pulumi.set(__self__, "pool_quota", pool_quota)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="accountEndpoint")
    def account_endpoint(self) -> str:
        """
        The account endpoint used to interact with the Batch service.
        """
        return pulumi.get(self, "account_endpoint")

    @property
    @pulumi.getter(name="activeJobAndJobScheduleQuota")
    def active_job_and_job_schedule_quota(self) -> int:
        return pulumi.get(self, "active_job_and_job_schedule_quota")

    @property
    @pulumi.getter(name="autoStorage")
    def auto_storage(self) -> 'outputs.AutoStoragePropertiesResponse':
        """
        Contains information about the auto-storage account associated with a Batch account.
        """
        return pulumi.get(self, "auto_storage")

    @property
    @pulumi.getter(name="dedicatedCoreQuota")
    def dedicated_core_quota(self) -> int:
        return pulumi.get(self, "dedicated_core_quota")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="keyVaultReference")
    def key_vault_reference(self) -> 'outputs.KeyVaultReferenceResponse':
        """
        Identifies the Azure key vault associated with a Batch account.
        """
        return pulumi.get(self, "key_vault_reference")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="lowPriorityCoreQuota")
    def low_priority_core_quota(self) -> int:
        return pulumi.get(self, "low_priority_core_quota")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="poolAllocationMode")
    def pool_allocation_mode(self) -> str:
        """
        The allocation mode for creating pools in the Batch account.
        """
        return pulumi.get(self, "pool_allocation_mode")

    @property
    @pulumi.getter(name="poolQuota")
    def pool_quota(self) -> int:
        return pulumi.get(self, "pool_quota")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioned state of the resource
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetBatchAccountResult(GetBatchAccountResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBatchAccountResult(
            account_endpoint=self.account_endpoint,
            active_job_and_job_schedule_quota=self.active_job_and_job_schedule_quota,
            auto_storage=self.auto_storage,
            dedicated_core_quota=self.dedicated_core_quota,
            id=self.id,
            key_vault_reference=self.key_vault_reference,
            location=self.location,
            low_priority_core_quota=self.low_priority_core_quota,
            name=self.name,
            pool_allocation_mode=self.pool_allocation_mode,
            pool_quota=self.pool_quota,
            provisioning_state=self.provisioning_state,
            tags=self.tags,
            type=self.type)


def get_batch_account(account_name: Optional[str] = None,
                      resource_group_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBatchAccountResult:
    """
    Use this data source to access information about an existing resource.

    :param str account_name: The name of the Batch account.
    :param str resource_group_name: The name of the resource group that contains the Batch account.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-nextgen:batch/v20170501:getBatchAccount', __args__, opts=opts, typ=GetBatchAccountResult).value

    return AwaitableGetBatchAccountResult(
        account_endpoint=__ret__.account_endpoint,
        active_job_and_job_schedule_quota=__ret__.active_job_and_job_schedule_quota,
        auto_storage=__ret__.auto_storage,
        dedicated_core_quota=__ret__.dedicated_core_quota,
        id=__ret__.id,
        key_vault_reference=__ret__.key_vault_reference,
        location=__ret__.location,
        low_priority_core_quota=__ret__.low_priority_core_quota,
        name=__ret__.name,
        pool_allocation_mode=__ret__.pool_allocation_mode,
        pool_quota=__ret__.pool_quota,
        provisioning_state=__ret__.provisioning_state,
        tags=__ret__.tags,
        type=__ret__.type)
