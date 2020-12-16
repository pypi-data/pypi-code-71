# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables

__all__ = ['PrivateZone']


class PrivateZone(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 private_zone_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Describes a Private DNS zone.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] etag: The ETag of the zone.
        :param pulumi.Input[str] location: The Azure Region where the resource lives
        :param pulumi.Input[str] private_zone_name: The name of the Private DNS zone (without a terminating dot).
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
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

            __props__['etag'] = etag
            __props__['location'] = location
            if private_zone_name is None and not opts.urn:
                raise TypeError("Missing required property 'private_zone_name'")
            __props__['private_zone_name'] = private_zone_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['tags'] = tags
            __props__['max_number_of_record_sets'] = None
            __props__['max_number_of_virtual_network_links'] = None
            __props__['max_number_of_virtual_network_links_with_registration'] = None
            __props__['name'] = None
            __props__['number_of_record_sets'] = None
            __props__['number_of_virtual_network_links'] = None
            __props__['number_of_virtual_network_links_with_registration'] = None
            __props__['provisioning_state'] = None
            __props__['type'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:network/latest:PrivateZone"), pulumi.Alias(type_="azure-nextgen:network/v20200101:PrivateZone"), pulumi.Alias(type_="azure-nextgen:network/v20200601:PrivateZone")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PrivateZone, __self__).__init__(
            'azure-nextgen:network/v20180901:PrivateZone',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PrivateZone':
        """
        Get an existing PrivateZone resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return PrivateZone(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        The ETag of the zone.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The Azure Region where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maxNumberOfRecordSets")
    def max_number_of_record_sets(self) -> pulumi.Output[int]:
        """
        The maximum number of record sets that can be created in this Private DNS zone. This is a read-only property and any attempt to set this value will be ignored.
        """
        return pulumi.get(self, "max_number_of_record_sets")

    @property
    @pulumi.getter(name="maxNumberOfVirtualNetworkLinks")
    def max_number_of_virtual_network_links(self) -> pulumi.Output[int]:
        """
        The maximum number of virtual networks that can be linked to this Private DNS zone. This is a read-only property and any attempt to set this value will be ignored.
        """
        return pulumi.get(self, "max_number_of_virtual_network_links")

    @property
    @pulumi.getter(name="maxNumberOfVirtualNetworkLinksWithRegistration")
    def max_number_of_virtual_network_links_with_registration(self) -> pulumi.Output[int]:
        """
        The maximum number of virtual networks that can be linked to this Private DNS zone with registration enabled. This is a read-only property and any attempt to set this value will be ignored.
        """
        return pulumi.get(self, "max_number_of_virtual_network_links_with_registration")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="numberOfRecordSets")
    def number_of_record_sets(self) -> pulumi.Output[int]:
        """
        The current number of record sets in this Private DNS zone. This is a read-only property and any attempt to set this value will be ignored.
        """
        return pulumi.get(self, "number_of_record_sets")

    @property
    @pulumi.getter(name="numberOfVirtualNetworkLinks")
    def number_of_virtual_network_links(self) -> pulumi.Output[int]:
        """
        The current number of virtual networks that are linked to this Private DNS zone. This is a read-only property and any attempt to set this value will be ignored.
        """
        return pulumi.get(self, "number_of_virtual_network_links")

    @property
    @pulumi.getter(name="numberOfVirtualNetworkLinksWithRegistration")
    def number_of_virtual_network_links_with_registration(self) -> pulumi.Output[int]:
        """
        The current number of virtual networks that are linked to this Private DNS zone with registration enabled. This is a read-only property and any attempt to set this value will be ignored.
        """
        return pulumi.get(self, "number_of_virtual_network_links_with_registration")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the resource. This is a read-only property and any attempt to set this value will be ignored.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. Example - 'Microsoft.Network/privateDnsZones'.
        """
        return pulumi.get(self, "type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

