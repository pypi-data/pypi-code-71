# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['PrivateDnsZoneGroup']


class PrivateDnsZoneGroup(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 private_dns_zone_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivateDnsZoneConfigArgs']]]]] = None,
                 private_dns_zone_group_name: Optional[pulumi.Input[str]] = None,
                 private_endpoint_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Private dns zone group resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] name: Name of the resource that is unique within a resource group. This name can be used to access the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivateDnsZoneConfigArgs']]]] private_dns_zone_configs: A collection of private dns zone configurations of the private dns zone group.
        :param pulumi.Input[str] private_dns_zone_group_name: The name of the private dns zone group.
        :param pulumi.Input[str] private_endpoint_name: The name of the private endpoint.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
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

            __props__['id'] = id
            __props__['name'] = name
            __props__['private_dns_zone_configs'] = private_dns_zone_configs
            if private_dns_zone_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'private_dns_zone_group_name'")
            __props__['private_dns_zone_group_name'] = private_dns_zone_group_name
            if private_endpoint_name is None and not opts.urn:
                raise TypeError("Missing required property 'private_endpoint_name'")
            __props__['private_endpoint_name'] = private_endpoint_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['etag'] = None
            __props__['provisioning_state'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:network/latest:PrivateDnsZoneGroup"), pulumi.Alias(type_="azure-nextgen:network/v20200301:PrivateDnsZoneGroup"), pulumi.Alias(type_="azure-nextgen:network/v20200501:PrivateDnsZoneGroup"), pulumi.Alias(type_="azure-nextgen:network/v20200601:PrivateDnsZoneGroup"), pulumi.Alias(type_="azure-nextgen:network/v20200701:PrivateDnsZoneGroup")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PrivateDnsZoneGroup, __self__).__init__(
            'azure-nextgen:network/v20200401:PrivateDnsZoneGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PrivateDnsZoneGroup':
        """
        Get an existing PrivateDnsZoneGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return PrivateDnsZoneGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        Name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateDnsZoneConfigs")
    def private_dns_zone_configs(self) -> pulumi.Output[Optional[Sequence['outputs.PrivateDnsZoneConfigResponse']]]:
        """
        A collection of private dns zone configurations of the private dns zone group.
        """
        return pulumi.get(self, "private_dns_zone_configs")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the private dns zone group resource.
        """
        return pulumi.get(self, "provisioning_state")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

