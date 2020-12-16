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

__all__ = ['ExpressRouteGateway']


class ExpressRouteGateway(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_scale_configuration: Optional[pulumi.Input[pulumi.InputType['ExpressRouteGatewayPropertiesAutoScaleConfigurationArgs']]] = None,
                 express_route_gateway_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_hub: Optional[pulumi.Input[pulumi.InputType['VirtualHubIdArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        ExpressRoute gateway resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ExpressRouteGatewayPropertiesAutoScaleConfigurationArgs']] auto_scale_configuration: Configuration for auto scaling.
        :param pulumi.Input[str] express_route_gateway_name: The name of the ExpressRoute gateway.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[pulumi.InputType['VirtualHubIdArgs']] virtual_hub: The Virtual Hub where the ExpressRoute gateway is or will be deployed.
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

            __props__['auto_scale_configuration'] = auto_scale_configuration
            if express_route_gateway_name is None and not opts.urn:
                raise TypeError("Missing required property 'express_route_gateway_name'")
            __props__['express_route_gateway_name'] = express_route_gateway_name
            __props__['id'] = id
            __props__['location'] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['tags'] = tags
            if virtual_hub is None and not opts.urn:
                raise TypeError("Missing required property 'virtual_hub'")
            __props__['virtual_hub'] = virtual_hub
            __props__['etag'] = None
            __props__['express_route_connections'] = None
            __props__['name'] = None
            __props__['provisioning_state'] = None
            __props__['type'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:network/latest:ExpressRouteGateway"), pulumi.Alias(type_="azure-nextgen:network/v20180801:ExpressRouteGateway"), pulumi.Alias(type_="azure-nextgen:network/v20181001:ExpressRouteGateway"), pulumi.Alias(type_="azure-nextgen:network/v20181101:ExpressRouteGateway"), pulumi.Alias(type_="azure-nextgen:network/v20181201:ExpressRouteGateway"), pulumi.Alias(type_="azure-nextgen:network/v20190201:ExpressRouteGateway"), pulumi.Alias(type_="azure-nextgen:network/v20190401:ExpressRouteGateway"), pulumi.Alias(type_="azure-nextgen:network/v20190601:ExpressRouteGateway"), pulumi.Alias(type_="azure-nextgen:network/v20190701:ExpressRouteGateway"), pulumi.Alias(type_="azure-nextgen:network/v20190801:ExpressRouteGateway"), pulumi.Alias(type_="azure-nextgen:network/v20190901:ExpressRouteGateway"), pulumi.Alias(type_="azure-nextgen:network/v20191101:ExpressRouteGateway"), pulumi.Alias(type_="azure-nextgen:network/v20191201:ExpressRouteGateway"), pulumi.Alias(type_="azure-nextgen:network/v20200301:ExpressRouteGateway"), pulumi.Alias(type_="azure-nextgen:network/v20200401:ExpressRouteGateway"), pulumi.Alias(type_="azure-nextgen:network/v20200501:ExpressRouteGateway"), pulumi.Alias(type_="azure-nextgen:network/v20200701:ExpressRouteGateway")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ExpressRouteGateway, __self__).__init__(
            'azure-nextgen:network/v20200601:ExpressRouteGateway',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ExpressRouteGateway':
        """
        Get an existing ExpressRouteGateway resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return ExpressRouteGateway(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autoScaleConfiguration")
    def auto_scale_configuration(self) -> pulumi.Output[Optional['outputs.ExpressRouteGatewayPropertiesResponseAutoScaleConfiguration']]:
        """
        Configuration for auto scaling.
        """
        return pulumi.get(self, "auto_scale_configuration")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="expressRouteConnections")
    def express_route_connections(self) -> pulumi.Output[Sequence['outputs.ExpressRouteConnectionResponse']]:
        """
        List of ExpressRoute connections to the ExpressRoute gateway.
        """
        return pulumi.get(self, "express_route_connections")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

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
        The provisioning state of the express route gateway resource.
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
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualHub")
    def virtual_hub(self) -> pulumi.Output['outputs.VirtualHubIdResponse']:
        """
        The Virtual Hub where the ExpressRoute gateway is or will be deployed.
        """
        return pulumi.get(self, "virtual_hub")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

