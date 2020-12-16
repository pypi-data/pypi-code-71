# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables
from . import outputs

__all__ = ['VirtualWAN']


class VirtualWAN(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 disable_vpn_encryption: Optional[pulumi.Input[bool]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_wan_name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        VirtualWAN Resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] disable_vpn_encryption: Vpn encryption to be disabled or not.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] resource_group_name: The resource group name of the VirtualWan.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] virtual_wan_name: The name of the VirtualWAN being created or updated.
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

            __props__['disable_vpn_encryption'] = disable_vpn_encryption
            __props__['id'] = id
            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__['location'] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['tags'] = tags
            if virtual_wan_name is None and not opts.urn:
                raise TypeError("Missing required property 'virtual_wan_name'")
            __props__['virtual_wan_name'] = virtual_wan_name
            __props__['etag'] = None
            __props__['name'] = None
            __props__['provisioning_state'] = None
            __props__['type'] = None
            __props__['virtual_hubs'] = None
            __props__['vpn_sites'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:network/latest:VirtualWAN"), pulumi.Alias(type_="azure-nextgen:network/v20180601:VirtualWAN"), pulumi.Alias(type_="azure-nextgen:network/v20180701:VirtualWAN"), pulumi.Alias(type_="azure-nextgen:network/v20180801:VirtualWAN"), pulumi.Alias(type_="azure-nextgen:network/v20181001:VirtualWAN"), pulumi.Alias(type_="azure-nextgen:network/v20181101:VirtualWAN"), pulumi.Alias(type_="azure-nextgen:network/v20181201:VirtualWAN"), pulumi.Alias(type_="azure-nextgen:network/v20190201:VirtualWAN"), pulumi.Alias(type_="azure-nextgen:network/v20190401:VirtualWAN"), pulumi.Alias(type_="azure-nextgen:network/v20190601:VirtualWAN"), pulumi.Alias(type_="azure-nextgen:network/v20190701:VirtualWAN"), pulumi.Alias(type_="azure-nextgen:network/v20190801:VirtualWAN"), pulumi.Alias(type_="azure-nextgen:network/v20190901:VirtualWAN"), pulumi.Alias(type_="azure-nextgen:network/v20191101:VirtualWAN"), pulumi.Alias(type_="azure-nextgen:network/v20191201:VirtualWAN"), pulumi.Alias(type_="azure-nextgen:network/v20200301:VirtualWAN"), pulumi.Alias(type_="azure-nextgen:network/v20200401:VirtualWAN"), pulumi.Alias(type_="azure-nextgen:network/v20200501:VirtualWAN"), pulumi.Alias(type_="azure-nextgen:network/v20200601:VirtualWAN"), pulumi.Alias(type_="azure-nextgen:network/v20200701:VirtualWAN")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VirtualWAN, __self__).__init__(
            'azure-nextgen:network/v20180401:VirtualWAN',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VirtualWAN':
        """
        Get an existing VirtualWAN resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return VirtualWAN(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="disableVpnEncryption")
    def disable_vpn_encryption(self) -> pulumi.Output[Optional[bool]]:
        """
        Vpn encryption to be disabled or not.
        """
        return pulumi.get(self, "disable_vpn_encryption")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        Gets a unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
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
        The provisioning state of the resource.
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
    @pulumi.getter(name="virtualHubs")
    def virtual_hubs(self) -> pulumi.Output[Sequence['outputs.SubResourceResponse']]:
        """
        List of VirtualHubs in the VirtualWAN.
        """
        return pulumi.get(self, "virtual_hubs")

    @property
    @pulumi.getter(name="vpnSites")
    def vpn_sites(self) -> pulumi.Output[Sequence['outputs.SubResourceResponse']]:
        return pulumi.get(self, "vpn_sites")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

