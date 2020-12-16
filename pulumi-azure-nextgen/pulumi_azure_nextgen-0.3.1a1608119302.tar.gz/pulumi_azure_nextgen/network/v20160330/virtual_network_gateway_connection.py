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

__all__ = ['VirtualNetworkGatewayConnection']


class VirtualNetworkGatewayConnection(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorization_key: Optional[pulumi.Input[str]] = None,
                 connection_status: Optional[pulumi.Input[Union[str, 'VirtualNetworkGatewayConnectionStatus']]] = None,
                 connection_type: Optional[pulumi.Input[Union[str, 'VirtualNetworkGatewayConnectionType']]] = None,
                 egress_bytes_transferred: Optional[pulumi.Input[int]] = None,
                 enable_bgp: Optional[pulumi.Input[bool]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 ingress_bytes_transferred: Optional[pulumi.Input[int]] = None,
                 local_network_gateway2: Optional[pulumi.Input[pulumi.InputType['LocalNetworkGatewayArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 peer: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_guid: Optional[pulumi.Input[str]] = None,
                 routing_weight: Optional[pulumi.Input[int]] = None,
                 shared_key: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_network_gateway1: Optional[pulumi.Input[pulumi.InputType['VirtualNetworkGatewayArgs']]] = None,
                 virtual_network_gateway2: Optional[pulumi.Input[pulumi.InputType['VirtualNetworkGatewayArgs']]] = None,
                 virtual_network_gateway_connection_name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        A common class for general resource information

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] authorization_key: The authorizationKey.
        :param pulumi.Input[Union[str, 'VirtualNetworkGatewayConnectionStatus']] connection_status: Virtual network Gateway connection status
        :param pulumi.Input[Union[str, 'VirtualNetworkGatewayConnectionType']] connection_type: Gateway connection type IPsec/Dedicated/VpnClient/Vnet2Vnet
        :param pulumi.Input[int] egress_bytes_transferred: The Egress Bytes Transferred in this connection
        :param pulumi.Input[bool] enable_bgp: EnableBgp Flag
        :param pulumi.Input[str] etag: Gets a unique read-only string that changes whenever the resource is updated
        :param pulumi.Input[str] id: Resource Id
        :param pulumi.Input[int] ingress_bytes_transferred: The Ingress Bytes Transferred in this connection
        :param pulumi.Input[pulumi.InputType['LocalNetworkGatewayArgs']] local_network_gateway2: A common class for general resource information
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[pulumi.InputType['SubResourceArgs']] peer: The reference to peerings resource.
        :param pulumi.Input[str] provisioning_state: Gets or sets Provisioning state of the VirtualNetworkGatewayConnection resource Updating/Deleting/Failed
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] resource_guid: Gets or sets resource GUID property of the VirtualNetworkGatewayConnection resource
        :param pulumi.Input[int] routing_weight: The Routing weight.
        :param pulumi.Input[str] shared_key: The IPsec share key.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[pulumi.InputType['VirtualNetworkGatewayArgs']] virtual_network_gateway1: A common class for general resource information
        :param pulumi.Input[pulumi.InputType['VirtualNetworkGatewayArgs']] virtual_network_gateway2: A common class for general resource information
        :param pulumi.Input[str] virtual_network_gateway_connection_name: The name of the virtual network gateway connection.
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

            __props__['authorization_key'] = authorization_key
            __props__['connection_status'] = connection_status
            __props__['connection_type'] = connection_type
            __props__['egress_bytes_transferred'] = egress_bytes_transferred
            __props__['enable_bgp'] = enable_bgp
            __props__['etag'] = etag
            __props__['id'] = id
            __props__['ingress_bytes_transferred'] = ingress_bytes_transferred
            __props__['local_network_gateway2'] = local_network_gateway2
            __props__['location'] = location
            __props__['peer'] = peer
            __props__['provisioning_state'] = provisioning_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['resource_guid'] = resource_guid
            __props__['routing_weight'] = routing_weight
            __props__['shared_key'] = shared_key
            __props__['tags'] = tags
            __props__['virtual_network_gateway1'] = virtual_network_gateway1
            __props__['virtual_network_gateway2'] = virtual_network_gateway2
            if virtual_network_gateway_connection_name is None and not opts.urn:
                raise TypeError("Missing required property 'virtual_network_gateway_connection_name'")
            __props__['virtual_network_gateway_connection_name'] = virtual_network_gateway_connection_name
            __props__['name'] = None
            __props__['type'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:network/latest:VirtualNetworkGatewayConnection"), pulumi.Alias(type_="azure-nextgen:network/v20150615:VirtualNetworkGatewayConnection"), pulumi.Alias(type_="azure-nextgen:network/v20160601:VirtualNetworkGatewayConnection"), pulumi.Alias(type_="azure-nextgen:network/v20160901:VirtualNetworkGatewayConnection"), pulumi.Alias(type_="azure-nextgen:network/v20161201:VirtualNetworkGatewayConnection"), pulumi.Alias(type_="azure-nextgen:network/v20170301:VirtualNetworkGatewayConnection"), pulumi.Alias(type_="azure-nextgen:network/v20170601:VirtualNetworkGatewayConnection"), pulumi.Alias(type_="azure-nextgen:network/v20170801:VirtualNetworkGatewayConnection"), pulumi.Alias(type_="azure-nextgen:network/v20170901:VirtualNetworkGatewayConnection"), pulumi.Alias(type_="azure-nextgen:network/v20171001:VirtualNetworkGatewayConnection"), pulumi.Alias(type_="azure-nextgen:network/v20171101:VirtualNetworkGatewayConnection"), pulumi.Alias(type_="azure-nextgen:network/v20180101:VirtualNetworkGatewayConnection"), pulumi.Alias(type_="azure-nextgen:network/v20180201:VirtualNetworkGatewayConnection"), pulumi.Alias(type_="azure-nextgen:network/v20180401:VirtualNetworkGatewayConnection"), pulumi.Alias(type_="azure-nextgen:network/v20180601:VirtualNetworkGatewayConnection"), pulumi.Alias(type_="azure-nextgen:network/v20180701:VirtualNetworkGatewayConnection"), pulumi.Alias(type_="azure-nextgen:network/v20180801:VirtualNetworkGatewayConnection"), pulumi.Alias(type_="azure-nextgen:network/v20181001:VirtualNetworkGatewayConnection"), pulumi.Alias(type_="azure-nextgen:network/v20181101:VirtualNetworkGatewayConnection"), pulumi.Alias(type_="azure-nextgen:network/v20181201:VirtualNetworkGatewayConnection"), pulumi.Alias(type_="azure-nextgen:network/v20190201:VirtualNetworkGatewayConnection"), pulumi.Alias(type_="azure-nextgen:network/v20190401:VirtualNetworkGatewayConnection"), pulumi.Alias(type_="azure-nextgen:network/v20190601:VirtualNetworkGatewayConnection"), pulumi.Alias(type_="azure-nextgen:network/v20190701:VirtualNetworkGatewayConnection"), pulumi.Alias(type_="azure-nextgen:network/v20190801:VirtualNetworkGatewayConnection"), pulumi.Alias(type_="azure-nextgen:network/v20190901:VirtualNetworkGatewayConnection"), pulumi.Alias(type_="azure-nextgen:network/v20191101:VirtualNetworkGatewayConnection"), pulumi.Alias(type_="azure-nextgen:network/v20191201:VirtualNetworkGatewayConnection"), pulumi.Alias(type_="azure-nextgen:network/v20200301:VirtualNetworkGatewayConnection"), pulumi.Alias(type_="azure-nextgen:network/v20200401:VirtualNetworkGatewayConnection"), pulumi.Alias(type_="azure-nextgen:network/v20200501:VirtualNetworkGatewayConnection"), pulumi.Alias(type_="azure-nextgen:network/v20200601:VirtualNetworkGatewayConnection"), pulumi.Alias(type_="azure-nextgen:network/v20200701:VirtualNetworkGatewayConnection")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VirtualNetworkGatewayConnection, __self__).__init__(
            'azure-nextgen:network/v20160330:VirtualNetworkGatewayConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VirtualNetworkGatewayConnection':
        """
        Get an existing VirtualNetworkGatewayConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return VirtualNetworkGatewayConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authorizationKey")
    def authorization_key(self) -> pulumi.Output[Optional[str]]:
        """
        The authorizationKey.
        """
        return pulumi.get(self, "authorization_key")

    @property
    @pulumi.getter(name="connectionStatus")
    def connection_status(self) -> pulumi.Output[Optional[str]]:
        """
        Virtual network Gateway connection status
        """
        return pulumi.get(self, "connection_status")

    @property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> pulumi.Output[Optional[str]]:
        """
        Gateway connection type IPsec/Dedicated/VpnClient/Vnet2Vnet
        """
        return pulumi.get(self, "connection_type")

    @property
    @pulumi.getter(name="egressBytesTransferred")
    def egress_bytes_transferred(self) -> pulumi.Output[Optional[int]]:
        """
        The Egress Bytes Transferred in this connection
        """
        return pulumi.get(self, "egress_bytes_transferred")

    @property
    @pulumi.getter(name="enableBgp")
    def enable_bgp(self) -> pulumi.Output[Optional[bool]]:
        """
        EnableBgp Flag
        """
        return pulumi.get(self, "enable_bgp")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Gets a unique read-only string that changes whenever the resource is updated
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="ingressBytesTransferred")
    def ingress_bytes_transferred(self) -> pulumi.Output[Optional[int]]:
        """
        The Ingress Bytes Transferred in this connection
        """
        return pulumi.get(self, "ingress_bytes_transferred")

    @property
    @pulumi.getter(name="localNetworkGateway2")
    def local_network_gateway2(self) -> pulumi.Output[Optional['outputs.LocalNetworkGatewayResponse']]:
        """
        A common class for general resource information
        """
        return pulumi.get(self, "local_network_gateway2")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def peer(self) -> pulumi.Output[Optional['outputs.SubResourceResponse']]:
        """
        The reference to peerings resource.
        """
        return pulumi.get(self, "peer")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets Provisioning state of the VirtualNetworkGatewayConnection resource Updating/Deleting/Failed
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets resource GUID property of the VirtualNetworkGatewayConnection resource
        """
        return pulumi.get(self, "resource_guid")

    @property
    @pulumi.getter(name="routingWeight")
    def routing_weight(self) -> pulumi.Output[Optional[int]]:
        """
        The Routing weight.
        """
        return pulumi.get(self, "routing_weight")

    @property
    @pulumi.getter(name="sharedKey")
    def shared_key(self) -> pulumi.Output[Optional[str]]:
        """
        The IPsec share key.
        """
        return pulumi.get(self, "shared_key")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualNetworkGateway1")
    def virtual_network_gateway1(self) -> pulumi.Output[Optional['outputs.VirtualNetworkGatewayResponse']]:
        """
        A common class for general resource information
        """
        return pulumi.get(self, "virtual_network_gateway1")

    @property
    @pulumi.getter(name="virtualNetworkGateway2")
    def virtual_network_gateway2(self) -> pulumi.Output[Optional['outputs.VirtualNetworkGatewayResponse']]:
        """
        A common class for general resource information
        """
        return pulumi.get(self, "virtual_network_gateway2")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

