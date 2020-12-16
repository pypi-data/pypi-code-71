# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables

__all__ = ['Origin']


class Origin(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 endpoint_name: Optional[pulumi.Input[str]] = None,
                 host_name: Optional[pulumi.Input[str]] = None,
                 http_port: Optional[pulumi.Input[int]] = None,
                 https_port: Optional[pulumi.Input[int]] = None,
                 origin_host_header: Optional[pulumi.Input[str]] = None,
                 origin_name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 private_link_alias: Optional[pulumi.Input[str]] = None,
                 private_link_approval_message: Optional[pulumi.Input[str]] = None,
                 private_link_location: Optional[pulumi.Input[str]] = None,
                 private_link_resource_id: Optional[pulumi.Input[str]] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 weight: Optional[pulumi.Input[int]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        CDN origin is the source of the content being delivered via CDN. When the edge nodes represented by an endpoint do not have the requested content cached, they attempt to fetch it from one or more of the configured origins.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enabled: Origin is enabled for load balancing or not
        :param pulumi.Input[str] endpoint_name: Name of the endpoint under the profile which is unique globally.
        :param pulumi.Input[str] host_name: The address of the origin. Domain names, IPv4 addresses, and IPv6 addresses are supported.This should be unique across all origins in an endpoint.
        :param pulumi.Input[int] http_port: The value of the HTTP port. Must be between 1 and 65535.
        :param pulumi.Input[int] https_port: The value of the HTTPS port. Must be between 1 and 65535.
        :param pulumi.Input[str] origin_host_header: The host header value sent to the origin with each request. If you leave this blank, the request hostname determines this value. Azure CDN origins, such as Web Apps, Blob Storage, and Cloud Services require this host header value to match the origin hostname by default. This overrides the host header defined at Endpoint
        :param pulumi.Input[str] origin_name: Name of the origin that is unique within the endpoint.
        :param pulumi.Input[int] priority: Priority of origin in given origin group for load balancing. Higher priorities will not be used for load balancing if any lower priority origin is healthy.Must be between 1 and 5
        :param pulumi.Input[str] private_link_alias: The Alias of the Private Link resource. Populating this optional field indicates that this origin is 'Private'
        :param pulumi.Input[str] private_link_approval_message: A custom message to be included in the approval request to connect to the Private Link.
        :param pulumi.Input[str] private_link_location: The location of the Private Link resource. Required only if 'privateLinkResourceId' is populated
        :param pulumi.Input[str] private_link_resource_id: The Resource Id of the Private Link resource. Populating this optional field indicates that this backend is 'Private'
        :param pulumi.Input[str] profile_name: Name of the CDN profile which is unique within the resource group.
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input[int] weight: Weight of the origin in given origin group for load balancing. Must be between 1 and 1000
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

            __props__['enabled'] = enabled
            if endpoint_name is None and not opts.urn:
                raise TypeError("Missing required property 'endpoint_name'")
            __props__['endpoint_name'] = endpoint_name
            if host_name is None and not opts.urn:
                raise TypeError("Missing required property 'host_name'")
            __props__['host_name'] = host_name
            __props__['http_port'] = http_port
            __props__['https_port'] = https_port
            __props__['origin_host_header'] = origin_host_header
            if origin_name is None and not opts.urn:
                raise TypeError("Missing required property 'origin_name'")
            __props__['origin_name'] = origin_name
            __props__['priority'] = priority
            __props__['private_link_alias'] = private_link_alias
            __props__['private_link_approval_message'] = private_link_approval_message
            __props__['private_link_location'] = private_link_location
            __props__['private_link_resource_id'] = private_link_resource_id
            if profile_name is None and not opts.urn:
                raise TypeError("Missing required property 'profile_name'")
            __props__['profile_name'] = profile_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['weight'] = weight
            __props__['name'] = None
            __props__['private_endpoint_status'] = None
            __props__['provisioning_state'] = None
            __props__['resource_state'] = None
            __props__['type'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:cdn/latest:Origin"), pulumi.Alias(type_="azure-nextgen:cdn/v20150601:Origin"), pulumi.Alias(type_="azure-nextgen:cdn/v20160402:Origin"), pulumi.Alias(type_="azure-nextgen:cdn/v20191231:Origin"), pulumi.Alias(type_="azure-nextgen:cdn/v20200331:Origin"), pulumi.Alias(type_="azure-nextgen:cdn/v20200901:Origin")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Origin, __self__).__init__(
            'azure-nextgen:cdn/v20200415:Origin',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Origin':
        """
        Get an existing Origin resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return Origin(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Origin is enabled for load balancing or not
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> pulumi.Output[str]:
        """
        The address of the origin. Domain names, IPv4 addresses, and IPv6 addresses are supported.This should be unique across all origins in an endpoint.
        """
        return pulumi.get(self, "host_name")

    @property
    @pulumi.getter(name="httpPort")
    def http_port(self) -> pulumi.Output[Optional[int]]:
        """
        The value of the HTTP port. Must be between 1 and 65535.
        """
        return pulumi.get(self, "http_port")

    @property
    @pulumi.getter(name="httpsPort")
    def https_port(self) -> pulumi.Output[Optional[int]]:
        """
        The value of the HTTPS port. Must be between 1 and 65535.
        """
        return pulumi.get(self, "https_port")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="originHostHeader")
    def origin_host_header(self) -> pulumi.Output[Optional[str]]:
        """
        The host header value sent to the origin with each request. If you leave this blank, the request hostname determines this value. Azure CDN origins, such as Web Apps, Blob Storage, and Cloud Services require this host header value to match the origin hostname by default. This overrides the host header defined at Endpoint
        """
        return pulumi.get(self, "origin_host_header")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[int]]:
        """
        Priority of origin in given origin group for load balancing. Higher priorities will not be used for load balancing if any lower priority origin is healthy.Must be between 1 and 5
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="privateEndpointStatus")
    def private_endpoint_status(self) -> pulumi.Output[str]:
        """
        The approval status for the connection to the Private Link
        """
        return pulumi.get(self, "private_endpoint_status")

    @property
    @pulumi.getter(name="privateLinkAlias")
    def private_link_alias(self) -> pulumi.Output[Optional[str]]:
        """
        The Alias of the Private Link resource. Populating this optional field indicates that this origin is 'Private'
        """
        return pulumi.get(self, "private_link_alias")

    @property
    @pulumi.getter(name="privateLinkApprovalMessage")
    def private_link_approval_message(self) -> pulumi.Output[Optional[str]]:
        """
        A custom message to be included in the approval request to connect to the Private Link.
        """
        return pulumi.get(self, "private_link_approval_message")

    @property
    @pulumi.getter(name="privateLinkLocation")
    def private_link_location(self) -> pulumi.Output[Optional[str]]:
        """
        The location of the Private Link resource. Required only if 'privateLinkResourceId' is populated
        """
        return pulumi.get(self, "private_link_location")

    @property
    @pulumi.getter(name="privateLinkResourceId")
    def private_link_resource_id(self) -> pulumi.Output[Optional[str]]:
        """
        The Resource Id of the Private Link resource. Populating this optional field indicates that this backend is 'Private'
        """
        return pulumi.get(self, "private_link_resource_id")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning status of the origin.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> pulumi.Output[str]:
        """
        Resource status of the origin.
        """
        return pulumi.get(self, "resource_state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def weight(self) -> pulumi.Output[Optional[int]]:
        """
        Weight of the origin in given origin group for load balancing. Must be between 1 and 1000
        """
        return pulumi.get(self, "weight")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

