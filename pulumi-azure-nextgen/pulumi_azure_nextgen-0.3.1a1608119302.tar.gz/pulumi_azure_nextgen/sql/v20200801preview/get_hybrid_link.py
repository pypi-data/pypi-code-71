# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables

__all__ = [
    'GetHybridLinkResult',
    'AwaitableGetHybridLinkResult',
    'get_hybrid_link',
]

@pulumi.output_type
class GetHybridLinkResult:
    """
    Hybrid link between box and Sql Managed Instance.
    """
    def __init__(__self__, distributed_availability_group_id=None, id=None, name=None, primary_availability_group_name=None, replication_mode=None, secondary_availability_group_name=None, source_endpoint=None, source_replica_id=None, target_database=None, target_replica_id=None, type=None):
        if distributed_availability_group_id and not isinstance(distributed_availability_group_id, str):
            raise TypeError("Expected argument 'distributed_availability_group_id' to be a str")
        pulumi.set(__self__, "distributed_availability_group_id", distributed_availability_group_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if primary_availability_group_name and not isinstance(primary_availability_group_name, str):
            raise TypeError("Expected argument 'primary_availability_group_name' to be a str")
        pulumi.set(__self__, "primary_availability_group_name", primary_availability_group_name)
        if replication_mode and not isinstance(replication_mode, str):
            raise TypeError("Expected argument 'replication_mode' to be a str")
        pulumi.set(__self__, "replication_mode", replication_mode)
        if secondary_availability_group_name and not isinstance(secondary_availability_group_name, str):
            raise TypeError("Expected argument 'secondary_availability_group_name' to be a str")
        pulumi.set(__self__, "secondary_availability_group_name", secondary_availability_group_name)
        if source_endpoint and not isinstance(source_endpoint, str):
            raise TypeError("Expected argument 'source_endpoint' to be a str")
        pulumi.set(__self__, "source_endpoint", source_endpoint)
        if source_replica_id and not isinstance(source_replica_id, str):
            raise TypeError("Expected argument 'source_replica_id' to be a str")
        pulumi.set(__self__, "source_replica_id", source_replica_id)
        if target_database and not isinstance(target_database, str):
            raise TypeError("Expected argument 'target_database' to be a str")
        pulumi.set(__self__, "target_database", target_database)
        if target_replica_id and not isinstance(target_replica_id, str):
            raise TypeError("Expected argument 'target_replica_id' to be a str")
        pulumi.set(__self__, "target_replica_id", target_replica_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="distributedAvailabilityGroupId")
    def distributed_availability_group_id(self) -> str:
        """
        The distributed availability group id
        """
        return pulumi.get(self, "distributed_availability_group_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="primaryAvailabilityGroupName")
    def primary_availability_group_name(self) -> Optional[str]:
        """
        The primary availability group name
        """
        return pulumi.get(self, "primary_availability_group_name")

    @property
    @pulumi.getter(name="replicationMode")
    def replication_mode(self) -> Optional[str]:
        """
        The replication mode of hybrid link. Parameter will be ignored during link creation.
        """
        return pulumi.get(self, "replication_mode")

    @property
    @pulumi.getter(name="secondaryAvailabilityGroupName")
    def secondary_availability_group_name(self) -> Optional[str]:
        """
        The secondary availability group name
        """
        return pulumi.get(self, "secondary_availability_group_name")

    @property
    @pulumi.getter(name="sourceEndpoint")
    def source_endpoint(self) -> Optional[str]:
        """
        The source endpoint
        """
        return pulumi.get(self, "source_endpoint")

    @property
    @pulumi.getter(name="sourceReplicaId")
    def source_replica_id(self) -> str:
        """
        The source replica id
        """
        return pulumi.get(self, "source_replica_id")

    @property
    @pulumi.getter(name="targetDatabase")
    def target_database(self) -> Optional[str]:
        """
        The name of the target database
        """
        return pulumi.get(self, "target_database")

    @property
    @pulumi.getter(name="targetReplicaId")
    def target_replica_id(self) -> str:
        """
        The target replica id
        """
        return pulumi.get(self, "target_replica_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetHybridLinkResult(GetHybridLinkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetHybridLinkResult(
            distributed_availability_group_id=self.distributed_availability_group_id,
            id=self.id,
            name=self.name,
            primary_availability_group_name=self.primary_availability_group_name,
            replication_mode=self.replication_mode,
            secondary_availability_group_name=self.secondary_availability_group_name,
            source_endpoint=self.source_endpoint,
            source_replica_id=self.source_replica_id,
            target_database=self.target_database,
            target_replica_id=self.target_replica_id,
            type=self.type)


def get_hybrid_link(distributed_availability_group_name: Optional[str] = None,
                    managed_instance_name: Optional[str] = None,
                    resource_group_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetHybridLinkResult:
    """
    Use this data source to access information about an existing resource.

    :param str distributed_availability_group_name: The distributed availability group name.
    :param str managed_instance_name: The name of the managed instance.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    """
    __args__ = dict()
    __args__['distributedAvailabilityGroupName'] = distributed_availability_group_name
    __args__['managedInstanceName'] = managed_instance_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-nextgen:sql/v20200801preview:getHybridLink', __args__, opts=opts, typ=GetHybridLinkResult).value

    return AwaitableGetHybridLinkResult(
        distributed_availability_group_id=__ret__.distributed_availability_group_id,
        id=__ret__.id,
        name=__ret__.name,
        primary_availability_group_name=__ret__.primary_availability_group_name,
        replication_mode=__ret__.replication_mode,
        secondary_availability_group_name=__ret__.secondary_availability_group_name,
        source_endpoint=__ret__.source_endpoint,
        source_replica_id=__ret__.source_replica_id,
        target_database=__ret__.target_database,
        target_replica_id=__ret__.target_replica_id,
        type=__ret__.type)
