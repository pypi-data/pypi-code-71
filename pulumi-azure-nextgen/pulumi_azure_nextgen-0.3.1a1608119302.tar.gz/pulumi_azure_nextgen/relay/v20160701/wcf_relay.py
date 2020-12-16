# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables
from ._enums import *

__all__ = ['WCFRelay']


class WCFRelay(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 relay_name: Optional[pulumi.Input[str]] = None,
                 relay_type: Optional[pulumi.Input[Union[str, 'Relaytype']]] = None,
                 requires_client_authorization: Optional[pulumi.Input[bool]] = None,
                 requires_transport_security: Optional[pulumi.Input[bool]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 user_metadata: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Description of WcfRelays Resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] namespace_name: The Namespace Name
        :param pulumi.Input[str] relay_name: The relay name
        :param pulumi.Input[Union[str, 'Relaytype']] relay_type: WCFRelay Type.
        :param pulumi.Input[bool] requires_client_authorization: true if client authorization is needed for this relay; otherwise, false.
        :param pulumi.Input[bool] requires_transport_security: true if transport security is needed for this relay; otherwise, false.
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input[str] user_metadata: usermetadata is a placeholder to store user-defined string data for the HybridConnection endpoint.e.g. it can be used to store  descriptive data, such as list of teams and their contact information also user-defined configuration settings can be stored.
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

            if namespace_name is None and not opts.urn:
                raise TypeError("Missing required property 'namespace_name'")
            __props__['namespace_name'] = namespace_name
            if relay_name is None and not opts.urn:
                raise TypeError("Missing required property 'relay_name'")
            __props__['relay_name'] = relay_name
            __props__['relay_type'] = relay_type
            __props__['requires_client_authorization'] = requires_client_authorization
            __props__['requires_transport_security'] = requires_transport_security
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['user_metadata'] = user_metadata
            __props__['created_at'] = None
            __props__['is_dynamic'] = None
            __props__['listener_count'] = None
            __props__['name'] = None
            __props__['type'] = None
            __props__['updated_at'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:relay/latest:WCFRelay"), pulumi.Alias(type_="azure-nextgen:relay/v20170401:WCFRelay")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(WCFRelay, __self__).__init__(
            'azure-nextgen:relay/v20160701:WCFRelay',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WCFRelay':
        """
        Get an existing WCFRelay resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return WCFRelay(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The time the WCFRelay was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="isDynamic")
    def is_dynamic(self) -> pulumi.Output[bool]:
        """
        true if the relay is dynamic; otherwise, false.
        """
        return pulumi.get(self, "is_dynamic")

    @property
    @pulumi.getter(name="listenerCount")
    def listener_count(self) -> pulumi.Output[int]:
        """
        The number of listeners for this relay. min : 1 and max:25 supported
        """
        return pulumi.get(self, "listener_count")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="relayType")
    def relay_type(self) -> pulumi.Output[Optional[str]]:
        """
        WCFRelay Type.
        """
        return pulumi.get(self, "relay_type")

    @property
    @pulumi.getter(name="requiresClientAuthorization")
    def requires_client_authorization(self) -> pulumi.Output[Optional[bool]]:
        """
        true if client authorization is needed for this relay; otherwise, false.
        """
        return pulumi.get(self, "requires_client_authorization")

    @property
    @pulumi.getter(name="requiresTransportSecurity")
    def requires_transport_security(self) -> pulumi.Output[Optional[bool]]:
        """
        true if transport security is needed for this relay; otherwise, false.
        """
        return pulumi.get(self, "requires_transport_security")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        The time the namespace was updated.
        """
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter(name="userMetadata")
    def user_metadata(self) -> pulumi.Output[Optional[str]]:
        """
        usermetadata is a placeholder to store user-defined string data for the HybridConnection endpoint.e.g. it can be used to store  descriptive data, such as list of teams and their contact information also user-defined configuration settings can be stored.
        """
        return pulumi.get(self, "user_metadata")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

