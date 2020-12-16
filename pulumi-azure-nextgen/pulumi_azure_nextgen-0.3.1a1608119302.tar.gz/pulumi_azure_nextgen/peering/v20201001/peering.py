# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['Peering']


class Peering(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 direct: Optional[pulumi.Input[pulumi.InputType['PeeringPropertiesDirectArgs']]] = None,
                 exchange: Optional[pulumi.Input[pulumi.InputType['PeeringPropertiesExchangeArgs']]] = None,
                 kind: Optional[pulumi.Input[Union[str, 'Kind']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 peering_location: Optional[pulumi.Input[str]] = None,
                 peering_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['PeeringSkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Peering is a logical representation of a set of connections to the Microsoft Cloud Edge at a location.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['PeeringPropertiesDirectArgs']] direct: The properties that define a direct peering.
        :param pulumi.Input[pulumi.InputType['PeeringPropertiesExchangeArgs']] exchange: The properties that define an exchange peering.
        :param pulumi.Input[Union[str, 'Kind']] kind: The kind of the peering.
        :param pulumi.Input[str] location: The location of the resource.
        :param pulumi.Input[str] peering_location: The location of the peering.
        :param pulumi.Input[str] peering_name: The name of the peering.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[pulumi.InputType['PeeringSkuArgs']] sku: The SKU that defines the tier and kind of the peering.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
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

            __props__['direct'] = direct
            __props__['exchange'] = exchange
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__['kind'] = kind
            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__['location'] = location
            __props__['peering_location'] = peering_location
            if peering_name is None and not opts.urn:
                raise TypeError("Missing required property 'peering_name'")
            __props__['peering_name'] = peering_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            if sku is None and not opts.urn:
                raise TypeError("Missing required property 'sku'")
            __props__['sku'] = sku
            __props__['tags'] = tags
            __props__['name'] = None
            __props__['provisioning_state'] = None
            __props__['type'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:peering/latest:Peering"), pulumi.Alias(type_="azure-nextgen:peering/v20190801preview:Peering"), pulumi.Alias(type_="azure-nextgen:peering/v20190901preview:Peering"), pulumi.Alias(type_="azure-nextgen:peering/v20200101preview:Peering"), pulumi.Alias(type_="azure-nextgen:peering/v20200401:Peering")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Peering, __self__).__init__(
            'azure-nextgen:peering/v20201001:Peering',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Peering':
        """
        Get an existing Peering resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return Peering(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def direct(self) -> pulumi.Output[Optional['outputs.PeeringPropertiesDirectResponse']]:
        """
        The properties that define a direct peering.
        """
        return pulumi.get(self, "direct")

    @property
    @pulumi.getter
    def exchange(self) -> pulumi.Output[Optional['outputs.PeeringPropertiesExchangeResponse']]:
        """
        The properties that define an exchange peering.
        """
        return pulumi.get(self, "exchange")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        The kind of the peering.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="peeringLocation")
    def peering_location(self) -> pulumi.Output[Optional[str]]:
        """
        The location of the peering.
        """
        return pulumi.get(self, "peering_location")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output['outputs.PeeringSkuResponse']:
        """
        The SKU that defines the tier and kind of the peering.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

