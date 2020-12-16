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

__all__ = ['InterfaceEndpoint']


class InterfaceEndpoint(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 endpoint_service: Optional[pulumi.Input[pulumi.InputType['EndpointServiceArgs']]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 fqdn: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 interface_endpoint_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 subnet: Optional[pulumi.Input[pulumi.InputType['SubnetArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Interface endpoint resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['EndpointServiceArgs']] endpoint_service: A reference to the service being brought into the virtual network.
        :param pulumi.Input[str] etag: Gets a unique read-only string that changes whenever the resource is updated.
        :param pulumi.Input[str] fqdn: A first-party service's FQDN that is mapped to the private IP allocated via this interface endpoint.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] interface_endpoint_name: The name of the interface endpoint.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[pulumi.InputType['SubnetArgs']] subnet: The ID of the subnet from which the private IP will be allocated.
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

            __props__['endpoint_service'] = endpoint_service
            __props__['etag'] = etag
            __props__['fqdn'] = fqdn
            __props__['id'] = id
            if interface_endpoint_name is None and not opts.urn:
                raise TypeError("Missing required property 'interface_endpoint_name'")
            __props__['interface_endpoint_name'] = interface_endpoint_name
            __props__['location'] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['subnet'] = subnet
            __props__['tags'] = tags
            __props__['name'] = None
            __props__['network_interfaces'] = None
            __props__['owner'] = None
            __props__['provisioning_state'] = None
            __props__['type'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:network/latest:InterfaceEndpoint"), pulumi.Alias(type_="azure-nextgen:network/v20181001:InterfaceEndpoint"), pulumi.Alias(type_="azure-nextgen:network/v20181101:InterfaceEndpoint"), pulumi.Alias(type_="azure-nextgen:network/v20181201:InterfaceEndpoint"), pulumi.Alias(type_="azure-nextgen:network/v20190201:InterfaceEndpoint")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(InterfaceEndpoint, __self__).__init__(
            'azure-nextgen:network/v20180801:InterfaceEndpoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'InterfaceEndpoint':
        """
        Get an existing InterfaceEndpoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return InterfaceEndpoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="endpointService")
    def endpoint_service(self) -> pulumi.Output[Optional['outputs.EndpointServiceResponse']]:
        """
        A reference to the service being brought into the virtual network.
        """
        return pulumi.get(self, "endpoint_service")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Gets a unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def fqdn(self) -> pulumi.Output[Optional[str]]:
        """
        A first-party service's FQDN that is mapped to the private IP allocated via this interface endpoint.
        """
        return pulumi.get(self, "fqdn")

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
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> pulumi.Output[Sequence['outputs.NetworkInterfaceResponse']]:
        """
        Gets an array of references to the network interfaces created for this interface endpoint.
        """
        return pulumi.get(self, "network_interfaces")

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Output[str]:
        """
        A read-only property that identifies who created this interface endpoint.
        """
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the interface endpoint. Possible values are: 'Updating', 'Deleting', and 'Failed'.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def subnet(self) -> pulumi.Output[Optional['outputs.SubnetResponse']]:
        """
        The ID of the subnet from which the private IP will be allocated.
        """
        return pulumi.get(self, "subnet")

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

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

