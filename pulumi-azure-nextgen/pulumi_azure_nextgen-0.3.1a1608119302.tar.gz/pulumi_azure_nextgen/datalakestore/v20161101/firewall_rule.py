# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables

__all__ = ['FirewallRule']


class FirewallRule(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 end_ip_address: Optional[pulumi.Input[str]] = None,
                 firewall_rule_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 start_ip_address: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Data Lake Store firewall rule information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the Data Lake Store account.
        :param pulumi.Input[str] end_ip_address: The end IP address for the firewall rule. This can be either ipv4 or ipv6. Start and End should be in the same protocol.
        :param pulumi.Input[str] firewall_rule_name: The name of the firewall rule to create or update.
        :param pulumi.Input[str] resource_group_name: The name of the Azure resource group.
        :param pulumi.Input[str] start_ip_address: The start IP address for the firewall rule. This can be either ipv4 or ipv6. Start and End should be in the same protocol.
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

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__['account_name'] = account_name
            if end_ip_address is None and not opts.urn:
                raise TypeError("Missing required property 'end_ip_address'")
            __props__['end_ip_address'] = end_ip_address
            if firewall_rule_name is None and not opts.urn:
                raise TypeError("Missing required property 'firewall_rule_name'")
            __props__['firewall_rule_name'] = firewall_rule_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            if start_ip_address is None and not opts.urn:
                raise TypeError("Missing required property 'start_ip_address'")
            __props__['start_ip_address'] = start_ip_address
            __props__['name'] = None
            __props__['type'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:datalakestore/latest:FirewallRule")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(FirewallRule, __self__).__init__(
            'azure-nextgen:datalakestore/v20161101:FirewallRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'FirewallRule':
        """
        Get an existing FirewallRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return FirewallRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="endIpAddress")
    def end_ip_address(self) -> pulumi.Output[str]:
        """
        The end IP address for the firewall rule. This can be either ipv4 or ipv6. Start and End should be in the same protocol.
        """
        return pulumi.get(self, "end_ip_address")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="startIpAddress")
    def start_ip_address(self) -> pulumi.Output[str]:
        """
        The start IP address for the firewall rule. This can be either ipv4 or ipv6. Start and End should be in the same protocol.
        """
        return pulumi.get(self, "start_ip_address")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The resource type.
        """
        return pulumi.get(self, "type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

