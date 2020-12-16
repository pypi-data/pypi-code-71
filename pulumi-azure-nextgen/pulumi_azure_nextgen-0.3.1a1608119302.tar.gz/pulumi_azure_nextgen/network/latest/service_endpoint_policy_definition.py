# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables

__all__ = ['ServiceEndpointPolicyDefinition']


class ServiceEndpointPolicyDefinition(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service: Optional[pulumi.Input[str]] = None,
                 service_endpoint_policy_definition_name: Optional[pulumi.Input[str]] = None,
                 service_endpoint_policy_name: Optional[pulumi.Input[str]] = None,
                 service_resources: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Service Endpoint policy definitions.
        Latest API Version: 2020-07-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description for this rule. Restricted to 140 chars.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] name: The name of the resource that is unique within a resource group. This name can be used to access the resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service: Service endpoint name.
        :param pulumi.Input[str] service_endpoint_policy_definition_name: The name of the service endpoint policy definition name.
        :param pulumi.Input[str] service_endpoint_policy_name: The name of the service endpoint policy.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] service_resources: A list of service resources.
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

            __props__['description'] = description
            __props__['id'] = id
            __props__['name'] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['service'] = service
            if service_endpoint_policy_definition_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_endpoint_policy_definition_name'")
            __props__['service_endpoint_policy_definition_name'] = service_endpoint_policy_definition_name
            if service_endpoint_policy_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_endpoint_policy_name'")
            __props__['service_endpoint_policy_name'] = service_endpoint_policy_name
            __props__['service_resources'] = service_resources
            __props__['etag'] = None
            __props__['provisioning_state'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:network/v20180701:ServiceEndpointPolicyDefinition"), pulumi.Alias(type_="azure-nextgen:network/v20180801:ServiceEndpointPolicyDefinition"), pulumi.Alias(type_="azure-nextgen:network/v20181001:ServiceEndpointPolicyDefinition"), pulumi.Alias(type_="azure-nextgen:network/v20181101:ServiceEndpointPolicyDefinition"), pulumi.Alias(type_="azure-nextgen:network/v20181201:ServiceEndpointPolicyDefinition"), pulumi.Alias(type_="azure-nextgen:network/v20190201:ServiceEndpointPolicyDefinition"), pulumi.Alias(type_="azure-nextgen:network/v20190401:ServiceEndpointPolicyDefinition"), pulumi.Alias(type_="azure-nextgen:network/v20190601:ServiceEndpointPolicyDefinition"), pulumi.Alias(type_="azure-nextgen:network/v20190701:ServiceEndpointPolicyDefinition"), pulumi.Alias(type_="azure-nextgen:network/v20190801:ServiceEndpointPolicyDefinition"), pulumi.Alias(type_="azure-nextgen:network/v20190901:ServiceEndpointPolicyDefinition"), pulumi.Alias(type_="azure-nextgen:network/v20191101:ServiceEndpointPolicyDefinition"), pulumi.Alias(type_="azure-nextgen:network/v20191201:ServiceEndpointPolicyDefinition"), pulumi.Alias(type_="azure-nextgen:network/v20200301:ServiceEndpointPolicyDefinition"), pulumi.Alias(type_="azure-nextgen:network/v20200401:ServiceEndpointPolicyDefinition"), pulumi.Alias(type_="azure-nextgen:network/v20200501:ServiceEndpointPolicyDefinition"), pulumi.Alias(type_="azure-nextgen:network/v20200601:ServiceEndpointPolicyDefinition"), pulumi.Alias(type_="azure-nextgen:network/v20200701:ServiceEndpointPolicyDefinition")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ServiceEndpointPolicyDefinition, __self__).__init__(
            'azure-nextgen:network/latest:ServiceEndpointPolicyDefinition',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ServiceEndpointPolicyDefinition':
        """
        Get an existing ServiceEndpointPolicyDefinition resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return ServiceEndpointPolicyDefinition(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description for this rule. Restricted to 140 chars.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the service endpoint policy definition resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def service(self) -> pulumi.Output[Optional[str]]:
        """
        Service endpoint name.
        """
        return pulumi.get(self, "service")

    @property
    @pulumi.getter(name="serviceResources")
    def service_resources(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of service resources.
        """
        return pulumi.get(self, "service_resources")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

