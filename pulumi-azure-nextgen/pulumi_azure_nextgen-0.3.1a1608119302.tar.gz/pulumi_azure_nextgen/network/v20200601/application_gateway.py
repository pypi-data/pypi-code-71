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

__all__ = ['ApplicationGateway']


class ApplicationGateway(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_gateway_name: Optional[pulumi.Input[str]] = None,
                 authentication_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayAuthenticationCertificateArgs']]]]] = None,
                 autoscale_configuration: Optional[pulumi.Input[pulumi.InputType['ApplicationGatewayAutoscaleConfigurationArgs']]] = None,
                 backend_address_pools: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayBackendAddressPoolArgs']]]]] = None,
                 backend_http_settings_collection: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayBackendHttpSettingsArgs']]]]] = None,
                 custom_error_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayCustomErrorArgs']]]]] = None,
                 enable_fips: Optional[pulumi.Input[bool]] = None,
                 enable_http2: Optional[pulumi.Input[bool]] = None,
                 firewall_policy: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 force_firewall_policy_association: Optional[pulumi.Input[bool]] = None,
                 frontend_ip_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayFrontendIPConfigurationArgs']]]]] = None,
                 frontend_ports: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayFrontendPortArgs']]]]] = None,
                 gateway_ip_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayIPConfigurationArgs']]]]] = None,
                 http_listeners: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayHttpListenerArgs']]]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ManagedServiceIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 private_link_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayPrivateLinkConfigurationArgs']]]]] = None,
                 probes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayProbeArgs']]]]] = None,
                 redirect_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayRedirectConfigurationArgs']]]]] = None,
                 request_routing_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayRequestRoutingRuleArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rewrite_rule_sets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayRewriteRuleSetArgs']]]]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['ApplicationGatewaySkuArgs']]] = None,
                 ssl_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewaySslCertificateArgs']]]]] = None,
                 ssl_policy: Optional[pulumi.Input[pulumi.InputType['ApplicationGatewaySslPolicyArgs']]] = None,
                 ssl_profiles: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewaySslProfileArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 trusted_client_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayTrustedClientCertificateArgs']]]]] = None,
                 trusted_root_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayTrustedRootCertificateArgs']]]]] = None,
                 url_path_maps: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayUrlPathMapArgs']]]]] = None,
                 web_application_firewall_configuration: Optional[pulumi.Input[pulumi.InputType['ApplicationGatewayWebApplicationFirewallConfigurationArgs']]] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Application gateway resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_gateway_name: The name of the application gateway.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayAuthenticationCertificateArgs']]]] authentication_certificates: Authentication certificates of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        :param pulumi.Input[pulumi.InputType['ApplicationGatewayAutoscaleConfigurationArgs']] autoscale_configuration: Autoscale Configuration.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayBackendAddressPoolArgs']]]] backend_address_pools: Backend address pool of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayBackendHttpSettingsArgs']]]] backend_http_settings_collection: Backend http settings of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayCustomErrorArgs']]]] custom_error_configurations: Custom error configurations of the application gateway resource.
        :param pulumi.Input[bool] enable_fips: Whether FIPS is enabled on the application gateway resource.
        :param pulumi.Input[bool] enable_http2: Whether HTTP2 is enabled on the application gateway resource.
        :param pulumi.Input[pulumi.InputType['SubResourceArgs']] firewall_policy: Reference to the FirewallPolicy resource.
        :param pulumi.Input[bool] force_firewall_policy_association: If true, associates a firewall policy with an application gateway regardless whether the policy differs from the WAF Config.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayFrontendIPConfigurationArgs']]]] frontend_ip_configurations: Frontend IP addresses of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayFrontendPortArgs']]]] frontend_ports: Frontend ports of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayIPConfigurationArgs']]]] gateway_ip_configurations: Subnets of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayHttpListenerArgs']]]] http_listeners: Http listeners of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[pulumi.InputType['ManagedServiceIdentityArgs']] identity: The identity of the application gateway, if configured.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayPrivateLinkConfigurationArgs']]]] private_link_configurations: PrivateLink configurations on application gateway.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayProbeArgs']]]] probes: Probes of the application gateway resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayRedirectConfigurationArgs']]]] redirect_configurations: Redirect configurations of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayRequestRoutingRuleArgs']]]] request_routing_rules: Request routing rules of the application gateway resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayRewriteRuleSetArgs']]]] rewrite_rule_sets: Rewrite rules for the application gateway resource.
        :param pulumi.Input[pulumi.InputType['ApplicationGatewaySkuArgs']] sku: SKU of the application gateway resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewaySslCertificateArgs']]]] ssl_certificates: SSL certificates of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        :param pulumi.Input[pulumi.InputType['ApplicationGatewaySslPolicyArgs']] ssl_policy: SSL policy of the application gateway resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewaySslProfileArgs']]]] ssl_profiles: SSL profiles of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayTrustedClientCertificateArgs']]]] trusted_client_certificates: Trusted client certificates of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayTrustedRootCertificateArgs']]]] trusted_root_certificates: Trusted Root certificates of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayUrlPathMapArgs']]]] url_path_maps: URL path map of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        :param pulumi.Input[pulumi.InputType['ApplicationGatewayWebApplicationFirewallConfigurationArgs']] web_application_firewall_configuration: Web application firewall configuration.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] zones: A list of availability zones denoting where the resource needs to come from.
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

            if application_gateway_name is None and not opts.urn:
                raise TypeError("Missing required property 'application_gateway_name'")
            __props__['application_gateway_name'] = application_gateway_name
            __props__['authentication_certificates'] = authentication_certificates
            __props__['autoscale_configuration'] = autoscale_configuration
            __props__['backend_address_pools'] = backend_address_pools
            __props__['backend_http_settings_collection'] = backend_http_settings_collection
            __props__['custom_error_configurations'] = custom_error_configurations
            __props__['enable_fips'] = enable_fips
            __props__['enable_http2'] = enable_http2
            __props__['firewall_policy'] = firewall_policy
            __props__['force_firewall_policy_association'] = force_firewall_policy_association
            __props__['frontend_ip_configurations'] = frontend_ip_configurations
            __props__['frontend_ports'] = frontend_ports
            __props__['gateway_ip_configurations'] = gateway_ip_configurations
            __props__['http_listeners'] = http_listeners
            __props__['id'] = id
            __props__['identity'] = identity
            __props__['location'] = location
            __props__['private_link_configurations'] = private_link_configurations
            __props__['probes'] = probes
            __props__['redirect_configurations'] = redirect_configurations
            __props__['request_routing_rules'] = request_routing_rules
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['rewrite_rule_sets'] = rewrite_rule_sets
            __props__['sku'] = sku
            __props__['ssl_certificates'] = ssl_certificates
            __props__['ssl_policy'] = ssl_policy
            __props__['ssl_profiles'] = ssl_profiles
            __props__['tags'] = tags
            __props__['trusted_client_certificates'] = trusted_client_certificates
            __props__['trusted_root_certificates'] = trusted_root_certificates
            __props__['url_path_maps'] = url_path_maps
            __props__['web_application_firewall_configuration'] = web_application_firewall_configuration
            __props__['zones'] = zones
            __props__['etag'] = None
            __props__['name'] = None
            __props__['operational_state'] = None
            __props__['private_endpoint_connections'] = None
            __props__['provisioning_state'] = None
            __props__['resource_guid'] = None
            __props__['type'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:network/latest:ApplicationGateway"), pulumi.Alias(type_="azure-nextgen:network/v20150501preview:ApplicationGateway"), pulumi.Alias(type_="azure-nextgen:network/v20150615:ApplicationGateway"), pulumi.Alias(type_="azure-nextgen:network/v20160330:ApplicationGateway"), pulumi.Alias(type_="azure-nextgen:network/v20160601:ApplicationGateway"), pulumi.Alias(type_="azure-nextgen:network/v20160901:ApplicationGateway"), pulumi.Alias(type_="azure-nextgen:network/v20161201:ApplicationGateway"), pulumi.Alias(type_="azure-nextgen:network/v20170301:ApplicationGateway"), pulumi.Alias(type_="azure-nextgen:network/v20170601:ApplicationGateway"), pulumi.Alias(type_="azure-nextgen:network/v20170801:ApplicationGateway"), pulumi.Alias(type_="azure-nextgen:network/v20170901:ApplicationGateway"), pulumi.Alias(type_="azure-nextgen:network/v20171001:ApplicationGateway"), pulumi.Alias(type_="azure-nextgen:network/v20171101:ApplicationGateway"), pulumi.Alias(type_="azure-nextgen:network/v20180101:ApplicationGateway"), pulumi.Alias(type_="azure-nextgen:network/v20180201:ApplicationGateway"), pulumi.Alias(type_="azure-nextgen:network/v20180401:ApplicationGateway"), pulumi.Alias(type_="azure-nextgen:network/v20180601:ApplicationGateway"), pulumi.Alias(type_="azure-nextgen:network/v20180701:ApplicationGateway"), pulumi.Alias(type_="azure-nextgen:network/v20180801:ApplicationGateway"), pulumi.Alias(type_="azure-nextgen:network/v20181001:ApplicationGateway"), pulumi.Alias(type_="azure-nextgen:network/v20181101:ApplicationGateway"), pulumi.Alias(type_="azure-nextgen:network/v20181201:ApplicationGateway"), pulumi.Alias(type_="azure-nextgen:network/v20190201:ApplicationGateway"), pulumi.Alias(type_="azure-nextgen:network/v20190401:ApplicationGateway"), pulumi.Alias(type_="azure-nextgen:network/v20190601:ApplicationGateway"), pulumi.Alias(type_="azure-nextgen:network/v20190701:ApplicationGateway"), pulumi.Alias(type_="azure-nextgen:network/v20190801:ApplicationGateway"), pulumi.Alias(type_="azure-nextgen:network/v20190901:ApplicationGateway"), pulumi.Alias(type_="azure-nextgen:network/v20191101:ApplicationGateway"), pulumi.Alias(type_="azure-nextgen:network/v20191201:ApplicationGateway"), pulumi.Alias(type_="azure-nextgen:network/v20200301:ApplicationGateway"), pulumi.Alias(type_="azure-nextgen:network/v20200401:ApplicationGateway"), pulumi.Alias(type_="azure-nextgen:network/v20200501:ApplicationGateway"), pulumi.Alias(type_="azure-nextgen:network/v20200701:ApplicationGateway")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ApplicationGateway, __self__).__init__(
            'azure-nextgen:network/v20200601:ApplicationGateway',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ApplicationGateway':
        """
        Get an existing ApplicationGateway resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return ApplicationGateway(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authenticationCertificates")
    def authentication_certificates(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayAuthenticationCertificateResponse']]]:
        """
        Authentication certificates of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        """
        return pulumi.get(self, "authentication_certificates")

    @property
    @pulumi.getter(name="autoscaleConfiguration")
    def autoscale_configuration(self) -> pulumi.Output[Optional['outputs.ApplicationGatewayAutoscaleConfigurationResponse']]:
        """
        Autoscale Configuration.
        """
        return pulumi.get(self, "autoscale_configuration")

    @property
    @pulumi.getter(name="backendAddressPools")
    def backend_address_pools(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayBackendAddressPoolResponse']]]:
        """
        Backend address pool of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        """
        return pulumi.get(self, "backend_address_pools")

    @property
    @pulumi.getter(name="backendHttpSettingsCollection")
    def backend_http_settings_collection(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayBackendHttpSettingsResponse']]]:
        """
        Backend http settings of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        """
        return pulumi.get(self, "backend_http_settings_collection")

    @property
    @pulumi.getter(name="customErrorConfigurations")
    def custom_error_configurations(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayCustomErrorResponse']]]:
        """
        Custom error configurations of the application gateway resource.
        """
        return pulumi.get(self, "custom_error_configurations")

    @property
    @pulumi.getter(name="enableFips")
    def enable_fips(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether FIPS is enabled on the application gateway resource.
        """
        return pulumi.get(self, "enable_fips")

    @property
    @pulumi.getter(name="enableHttp2")
    def enable_http2(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether HTTP2 is enabled on the application gateway resource.
        """
        return pulumi.get(self, "enable_http2")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="firewallPolicy")
    def firewall_policy(self) -> pulumi.Output[Optional['outputs.SubResourceResponse']]:
        """
        Reference to the FirewallPolicy resource.
        """
        return pulumi.get(self, "firewall_policy")

    @property
    @pulumi.getter(name="forceFirewallPolicyAssociation")
    def force_firewall_policy_association(self) -> pulumi.Output[Optional[bool]]:
        """
        If true, associates a firewall policy with an application gateway regardless whether the policy differs from the WAF Config.
        """
        return pulumi.get(self, "force_firewall_policy_association")

    @property
    @pulumi.getter(name="frontendIPConfigurations")
    def frontend_ip_configurations(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayFrontendIPConfigurationResponse']]]:
        """
        Frontend IP addresses of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        """
        return pulumi.get(self, "frontend_ip_configurations")

    @property
    @pulumi.getter(name="frontendPorts")
    def frontend_ports(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayFrontendPortResponse']]]:
        """
        Frontend ports of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        """
        return pulumi.get(self, "frontend_ports")

    @property
    @pulumi.getter(name="gatewayIPConfigurations")
    def gateway_ip_configurations(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayIPConfigurationResponse']]]:
        """
        Subnets of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        """
        return pulumi.get(self, "gateway_ip_configurations")

    @property
    @pulumi.getter(name="httpListeners")
    def http_listeners(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayHttpListenerResponse']]]:
        """
        Http listeners of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        """
        return pulumi.get(self, "http_listeners")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ManagedServiceIdentityResponse']]:
        """
        The identity of the application gateway, if configured.
        """
        return pulumi.get(self, "identity")

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
    @pulumi.getter(name="operationalState")
    def operational_state(self) -> pulumi.Output[str]:
        """
        Operational state of the application gateway resource.
        """
        return pulumi.get(self, "operational_state")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> pulumi.Output[Sequence['outputs.ApplicationGatewayPrivateEndpointConnectionResponse']]:
        """
        Private Endpoint connections on application gateway.
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="privateLinkConfigurations")
    def private_link_configurations(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayPrivateLinkConfigurationResponse']]]:
        """
        PrivateLink configurations on application gateway.
        """
        return pulumi.get(self, "private_link_configurations")

    @property
    @pulumi.getter
    def probes(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayProbeResponse']]]:
        """
        Probes of the application gateway resource.
        """
        return pulumi.get(self, "probes")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the application gateway resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="redirectConfigurations")
    def redirect_configurations(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayRedirectConfigurationResponse']]]:
        """
        Redirect configurations of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        """
        return pulumi.get(self, "redirect_configurations")

    @property
    @pulumi.getter(name="requestRoutingRules")
    def request_routing_rules(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayRequestRoutingRuleResponse']]]:
        """
        Request routing rules of the application gateway resource.
        """
        return pulumi.get(self, "request_routing_rules")

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> pulumi.Output[str]:
        """
        The resource GUID property of the application gateway resource.
        """
        return pulumi.get(self, "resource_guid")

    @property
    @pulumi.getter(name="rewriteRuleSets")
    def rewrite_rule_sets(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayRewriteRuleSetResponse']]]:
        """
        Rewrite rules for the application gateway resource.
        """
        return pulumi.get(self, "rewrite_rule_sets")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.ApplicationGatewaySkuResponse']]:
        """
        SKU of the application gateway resource.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="sslCertificates")
    def ssl_certificates(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewaySslCertificateResponse']]]:
        """
        SSL certificates of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        """
        return pulumi.get(self, "ssl_certificates")

    @property
    @pulumi.getter(name="sslPolicy")
    def ssl_policy(self) -> pulumi.Output[Optional['outputs.ApplicationGatewaySslPolicyResponse']]:
        """
        SSL policy of the application gateway resource.
        """
        return pulumi.get(self, "ssl_policy")

    @property
    @pulumi.getter(name="sslProfiles")
    def ssl_profiles(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewaySslProfileResponse']]]:
        """
        SSL profiles of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        """
        return pulumi.get(self, "ssl_profiles")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="trustedClientCertificates")
    def trusted_client_certificates(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayTrustedClientCertificateResponse']]]:
        """
        Trusted client certificates of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        """
        return pulumi.get(self, "trusted_client_certificates")

    @property
    @pulumi.getter(name="trustedRootCertificates")
    def trusted_root_certificates(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayTrustedRootCertificateResponse']]]:
        """
        Trusted Root certificates of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        """
        return pulumi.get(self, "trusted_root_certificates")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="urlPathMaps")
    def url_path_maps(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayUrlPathMapResponse']]]:
        """
        URL path map of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        """
        return pulumi.get(self, "url_path_maps")

    @property
    @pulumi.getter(name="webApplicationFirewallConfiguration")
    def web_application_firewall_configuration(self) -> pulumi.Output[Optional['outputs.ApplicationGatewayWebApplicationFirewallConfigurationResponse']]:
        """
        Web application firewall configuration.
        """
        return pulumi.get(self, "web_application_firewall_configuration")

    @property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of availability zones denoting where the resource needs to come from.
        """
        return pulumi.get(self, "zones")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

