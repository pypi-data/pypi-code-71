# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables
from ._enums import *

__all__ = ['HybridLink']


class HybridLink(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 distributed_availability_group_name: Optional[pulumi.Input[str]] = None,
                 managed_instance_name: Optional[pulumi.Input[str]] = None,
                 primary_availability_group_name: Optional[pulumi.Input[str]] = None,
                 replication_mode: Optional[pulumi.Input[Union[str, 'ReplicationMode']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 secondary_availability_group_name: Optional[pulumi.Input[str]] = None,
                 source_endpoint: Optional[pulumi.Input[str]] = None,
                 target_database: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Hybrid link between box and Sql Managed Instance.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] distributed_availability_group_name: The distributed availability group name.
        :param pulumi.Input[str] managed_instance_name: The name of the managed instance.
        :param pulumi.Input[str] primary_availability_group_name: The primary availability group name
        :param pulumi.Input[Union[str, 'ReplicationMode']] replication_mode: The replication mode of hybrid link. Parameter will be ignored during link creation.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] secondary_availability_group_name: The secondary availability group name
        :param pulumi.Input[str] source_endpoint: The source endpoint
        :param pulumi.Input[str] target_database: The name of the target database
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

            if distributed_availability_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'distributed_availability_group_name'")
            __props__['distributed_availability_group_name'] = distributed_availability_group_name
            if managed_instance_name is None and not opts.urn:
                raise TypeError("Missing required property 'managed_instance_name'")
            __props__['managed_instance_name'] = managed_instance_name
            __props__['primary_availability_group_name'] = primary_availability_group_name
            __props__['replication_mode'] = replication_mode
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['secondary_availability_group_name'] = secondary_availability_group_name
            __props__['source_endpoint'] = source_endpoint
            __props__['target_database'] = target_database
            __props__['distributed_availability_group_id'] = None
            __props__['name'] = None
            __props__['source_replica_id'] = None
            __props__['target_replica_id'] = None
            __props__['type'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:sql/v20200202preview:HybridLink")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(HybridLink, __self__).__init__(
            'azure-nextgen:sql/v20200801preview:HybridLink',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'HybridLink':
        """
        Get an existing HybridLink resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return HybridLink(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="distributedAvailabilityGroupId")
    def distributed_availability_group_id(self) -> pulumi.Output[str]:
        """
        The distributed availability group id
        """
        return pulumi.get(self, "distributed_availability_group_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="primaryAvailabilityGroupName")
    def primary_availability_group_name(self) -> pulumi.Output[Optional[str]]:
        """
        The primary availability group name
        """
        return pulumi.get(self, "primary_availability_group_name")

    @property
    @pulumi.getter(name="replicationMode")
    def replication_mode(self) -> pulumi.Output[Optional[str]]:
        """
        The replication mode of hybrid link. Parameter will be ignored during link creation.
        """
        return pulumi.get(self, "replication_mode")

    @property
    @pulumi.getter(name="secondaryAvailabilityGroupName")
    def secondary_availability_group_name(self) -> pulumi.Output[Optional[str]]:
        """
        The secondary availability group name
        """
        return pulumi.get(self, "secondary_availability_group_name")

    @property
    @pulumi.getter(name="sourceEndpoint")
    def source_endpoint(self) -> pulumi.Output[Optional[str]]:
        """
        The source endpoint
        """
        return pulumi.get(self, "source_endpoint")

    @property
    @pulumi.getter(name="sourceReplicaId")
    def source_replica_id(self) -> pulumi.Output[str]:
        """
        The source replica id
        """
        return pulumi.get(self, "source_replica_id")

    @property
    @pulumi.getter(name="targetDatabase")
    def target_database(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the target database
        """
        return pulumi.get(self, "target_database")

    @property
    @pulumi.getter(name="targetReplicaId")
    def target_replica_id(self) -> pulumi.Output[str]:
        """
        The target replica id
        """
        return pulumi.get(self, "target_replica_id")

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

