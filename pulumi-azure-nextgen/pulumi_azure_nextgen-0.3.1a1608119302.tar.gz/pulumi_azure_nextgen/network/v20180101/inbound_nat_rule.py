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

__all__ = ['InboundNatRule']


class InboundNatRule(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backend_port: Optional[pulumi.Input[int]] = None,
                 enable_floating_ip: Optional[pulumi.Input[bool]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 frontend_ip_configuration: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 frontend_port: Optional[pulumi.Input[int]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 idle_timeout_in_minutes: Optional[pulumi.Input[int]] = None,
                 inbound_nat_rule_name: Optional[pulumi.Input[str]] = None,
                 load_balancer_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[Union[str, 'TransportProtocol']]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Inbound NAT rule of the load balancer.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] backend_port: The port used for the internal endpoint. Acceptable values range from 1 to 65535.
        :param pulumi.Input[bool] enable_floating_ip: Configures a virtual machine's endpoint for the floating IP capability required to configure a SQL AlwaysOn Availability Group. This setting is required when using the SQL AlwaysOn Availability Groups in SQL server. This setting can't be changed after you create the endpoint.
        :param pulumi.Input[str] etag: A unique read-only string that changes whenever the resource is updated.
        :param pulumi.Input[pulumi.InputType['SubResourceArgs']] frontend_ip_configuration: A reference to frontend IP addresses.
        :param pulumi.Input[int] frontend_port: The port for the external endpoint. Port numbers for each rule must be unique within the Load Balancer. Acceptable values range from 1 to 65534.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[int] idle_timeout_in_minutes: The timeout for the TCP idle connection. The value can be set between 4 and 30 minutes. The default value is 4 minutes. This element is only used when the protocol is set to TCP.
        :param pulumi.Input[str] inbound_nat_rule_name: The name of the inbound nat rule.
        :param pulumi.Input[str] load_balancer_name: The name of the load balancer.
        :param pulumi.Input[str] name: Gets name of the resource that is unique within a resource group. This name can be used to access the resource.
        :param pulumi.Input[Union[str, 'TransportProtocol']] protocol: The transport protocol for the endpoint. Possible values are 'Udp' or 'Tcp' or 'All.'
        :param pulumi.Input[str] provisioning_state: Gets the provisioning state of the public IP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
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

            __props__['backend_port'] = backend_port
            __props__['enable_floating_ip'] = enable_floating_ip
            __props__['etag'] = etag
            __props__['frontend_ip_configuration'] = frontend_ip_configuration
            __props__['frontend_port'] = frontend_port
            __props__['id'] = id
            __props__['idle_timeout_in_minutes'] = idle_timeout_in_minutes
            if inbound_nat_rule_name is None and not opts.urn:
                raise TypeError("Missing required property 'inbound_nat_rule_name'")
            __props__['inbound_nat_rule_name'] = inbound_nat_rule_name
            if load_balancer_name is None and not opts.urn:
                raise TypeError("Missing required property 'load_balancer_name'")
            __props__['load_balancer_name'] = load_balancer_name
            __props__['name'] = name
            __props__['protocol'] = protocol
            __props__['provisioning_state'] = provisioning_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['backend_ip_configuration'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:network/latest:InboundNatRule"), pulumi.Alias(type_="azure-nextgen:network/v20170601:InboundNatRule"), pulumi.Alias(type_="azure-nextgen:network/v20170801:InboundNatRule"), pulumi.Alias(type_="azure-nextgen:network/v20170901:InboundNatRule"), pulumi.Alias(type_="azure-nextgen:network/v20171001:InboundNatRule"), pulumi.Alias(type_="azure-nextgen:network/v20171101:InboundNatRule"), pulumi.Alias(type_="azure-nextgen:network/v20180201:InboundNatRule"), pulumi.Alias(type_="azure-nextgen:network/v20180401:InboundNatRule"), pulumi.Alias(type_="azure-nextgen:network/v20180601:InboundNatRule"), pulumi.Alias(type_="azure-nextgen:network/v20180701:InboundNatRule"), pulumi.Alias(type_="azure-nextgen:network/v20180801:InboundNatRule"), pulumi.Alias(type_="azure-nextgen:network/v20181001:InboundNatRule"), pulumi.Alias(type_="azure-nextgen:network/v20181101:InboundNatRule"), pulumi.Alias(type_="azure-nextgen:network/v20181201:InboundNatRule"), pulumi.Alias(type_="azure-nextgen:network/v20190201:InboundNatRule"), pulumi.Alias(type_="azure-nextgen:network/v20190401:InboundNatRule"), pulumi.Alias(type_="azure-nextgen:network/v20190601:InboundNatRule"), pulumi.Alias(type_="azure-nextgen:network/v20190701:InboundNatRule"), pulumi.Alias(type_="azure-nextgen:network/v20190801:InboundNatRule"), pulumi.Alias(type_="azure-nextgen:network/v20190901:InboundNatRule"), pulumi.Alias(type_="azure-nextgen:network/v20191101:InboundNatRule"), pulumi.Alias(type_="azure-nextgen:network/v20191201:InboundNatRule"), pulumi.Alias(type_="azure-nextgen:network/v20200301:InboundNatRule"), pulumi.Alias(type_="azure-nextgen:network/v20200401:InboundNatRule"), pulumi.Alias(type_="azure-nextgen:network/v20200501:InboundNatRule"), pulumi.Alias(type_="azure-nextgen:network/v20200601:InboundNatRule"), pulumi.Alias(type_="azure-nextgen:network/v20200701:InboundNatRule")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(InboundNatRule, __self__).__init__(
            'azure-nextgen:network/v20180101:InboundNatRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'InboundNatRule':
        """
        Get an existing InboundNatRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return InboundNatRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="backendIPConfiguration")
    def backend_ip_configuration(self) -> pulumi.Output['outputs.NetworkInterfaceIPConfigurationResponse']:
        """
        A reference to a private IP address defined on a network interface of a VM. Traffic sent to the frontend port of each of the frontend IP configurations is forwarded to the backend IP.
        """
        return pulumi.get(self, "backend_ip_configuration")

    @property
    @pulumi.getter(name="backendPort")
    def backend_port(self) -> pulumi.Output[Optional[int]]:
        """
        The port used for the internal endpoint. Acceptable values range from 1 to 65535.
        """
        return pulumi.get(self, "backend_port")

    @property
    @pulumi.getter(name="enableFloatingIP")
    def enable_floating_ip(self) -> pulumi.Output[Optional[bool]]:
        """
        Configures a virtual machine's endpoint for the floating IP capability required to configure a SQL AlwaysOn Availability Group. This setting is required when using the SQL AlwaysOn Availability Groups in SQL server. This setting can't be changed after you create the endpoint.
        """
        return pulumi.get(self, "enable_floating_ip")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="frontendIPConfiguration")
    def frontend_ip_configuration(self) -> pulumi.Output[Optional['outputs.SubResourceResponse']]:
        """
        A reference to frontend IP addresses.
        """
        return pulumi.get(self, "frontend_ip_configuration")

    @property
    @pulumi.getter(name="frontendPort")
    def frontend_port(self) -> pulumi.Output[Optional[int]]:
        """
        The port for the external endpoint. Port numbers for each rule must be unique within the Load Balancer. Acceptable values range from 1 to 65534.
        """
        return pulumi.get(self, "frontend_port")

    @property
    @pulumi.getter(name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> pulumi.Output[Optional[int]]:
        """
        The timeout for the TCP idle connection. The value can be set between 4 and 30 minutes. The default value is 4 minutes. This element is only used when the protocol is set to TCP.
        """
        return pulumi.get(self, "idle_timeout_in_minutes")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        Gets name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[Optional[str]]:
        """
        The transport protocol for the endpoint. Possible values are 'Udp' or 'Tcp' or 'All.'
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        Gets the provisioning state of the public IP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
        """
        return pulumi.get(self, "provisioning_state")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

