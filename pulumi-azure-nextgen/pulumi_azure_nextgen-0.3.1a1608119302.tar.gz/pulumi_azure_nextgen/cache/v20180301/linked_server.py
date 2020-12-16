# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables
from ._enums import *

__all__ = ['LinkedServer']


class LinkedServer(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 linked_redis_cache_id: Optional[pulumi.Input[str]] = None,
                 linked_redis_cache_location: Optional[pulumi.Input[str]] = None,
                 linked_server_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_role: Optional[pulumi.Input['ReplicationRole']] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Response to put/get linked server (with properties) for Redis cache.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] linked_redis_cache_id: Fully qualified resourceId of the linked redis cache.
        :param pulumi.Input[str] linked_redis_cache_location: Location of the linked redis cache.
        :param pulumi.Input[str] linked_server_name: The name of the linked server that is being added to the Redis cache.
        :param pulumi.Input[str] name: The name of the Redis cache.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input['ReplicationRole'] server_role: Role of the linked server.
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

            if linked_redis_cache_id is None and not opts.urn:
                raise TypeError("Missing required property 'linked_redis_cache_id'")
            __props__['linked_redis_cache_id'] = linked_redis_cache_id
            if linked_redis_cache_location is None and not opts.urn:
                raise TypeError("Missing required property 'linked_redis_cache_location'")
            __props__['linked_redis_cache_location'] = linked_redis_cache_location
            if linked_server_name is None and not opts.urn:
                raise TypeError("Missing required property 'linked_server_name'")
            __props__['linked_server_name'] = linked_server_name
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__['name'] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            if server_role is None and not opts.urn:
                raise TypeError("Missing required property 'server_role'")
            __props__['server_role'] = server_role
            __props__['provisioning_state'] = None
            __props__['type'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:cache/latest:LinkedServer"), pulumi.Alias(type_="azure-nextgen:cache/v20170201:LinkedServer"), pulumi.Alias(type_="azure-nextgen:cache/v20171001:LinkedServer"), pulumi.Alias(type_="azure-nextgen:cache/v20190701:LinkedServer"), pulumi.Alias(type_="azure-nextgen:cache/v20200601:LinkedServer")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(LinkedServer, __self__).__init__(
            'azure-nextgen:cache/v20180301:LinkedServer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LinkedServer':
        """
        Get an existing LinkedServer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return LinkedServer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="linkedRedisCacheId")
    def linked_redis_cache_id(self) -> pulumi.Output[str]:
        """
        Fully qualified resourceId of the linked redis cache.
        """
        return pulumi.get(self, "linked_redis_cache_id")

    @property
    @pulumi.getter(name="linkedRedisCacheLocation")
    def linked_redis_cache_location(self) -> pulumi.Output[str]:
        """
        Location of the linked redis cache.
        """
        return pulumi.get(self, "linked_redis_cache_location")

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
        Terminal state of the link between primary and secondary redis cache.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="serverRole")
    def server_role(self) -> pulumi.Output[str]:
        """
        Role of the linked server.
        """
        return pulumi.get(self, "server_role")

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

