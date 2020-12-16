# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables

__all__ = ['WorkloadNetworkDnsZone']


class WorkloadNetworkDnsZone(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 dns_server_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 dns_services: Optional[pulumi.Input[int]] = None,
                 dns_zone_id: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 private_cloud_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 revision: Optional[pulumi.Input[int]] = None,
                 source_ip: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        NSX DNS Zone

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] display_name: Display name of the DNS Zone.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dns_server_ips: DNS Server IP array of the DNS Zone.
        :param pulumi.Input[int] dns_services: Number of DNS Services using the DNS zone.
        :param pulumi.Input[str] dns_zone_id: NSX DNS Zone identifier. Generally the same as the DNS Zone's display name
        :param pulumi.Input[Sequence[pulumi.Input[str]]] domain: Domain names of the DNS Zone.
        :param pulumi.Input[str] private_cloud_name: Name of the private cloud
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[int] revision: NSX revision number.
        :param pulumi.Input[str] source_ip: Source IP of the DNS Zone.
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

            __props__['display_name'] = display_name
            __props__['dns_server_ips'] = dns_server_ips
            __props__['dns_services'] = dns_services
            if dns_zone_id is None and not opts.urn:
                raise TypeError("Missing required property 'dns_zone_id'")
            __props__['dns_zone_id'] = dns_zone_id
            __props__['domain'] = domain
            if private_cloud_name is None and not opts.urn:
                raise TypeError("Missing required property 'private_cloud_name'")
            __props__['private_cloud_name'] = private_cloud_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['revision'] = revision
            __props__['source_ip'] = source_ip
            __props__['name'] = None
            __props__['provisioning_state'] = None
            __props__['type'] = None
        super(WorkloadNetworkDnsZone, __self__).__init__(
            'azure-nextgen:avs/v20200717preview:WorkloadNetworkDnsZone',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WorkloadNetworkDnsZone':
        """
        Get an existing WorkloadNetworkDnsZone resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return WorkloadNetworkDnsZone(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        Display name of the DNS Zone.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="dnsServerIps")
    def dns_server_ips(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        DNS Server IP array of the DNS Zone.
        """
        return pulumi.get(self, "dns_server_ips")

    @property
    @pulumi.getter(name="dnsServices")
    def dns_services(self) -> pulumi.Output[Optional[int]]:
        """
        Number of DNS Services using the DNS zone.
        """
        return pulumi.get(self, "dns_services")

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Domain names of the DNS Zone.
        """
        return pulumi.get(self, "domain")

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
        The provisioning state
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def revision(self) -> pulumi.Output[Optional[int]]:
        """
        NSX revision number.
        """
        return pulumi.get(self, "revision")

    @property
    @pulumi.getter(name="sourceIp")
    def source_ip(self) -> pulumi.Output[Optional[str]]:
        """
        Source IP of the DNS Zone.
        """
        return pulumi.get(self, "source_ip")

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

