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

__all__ = ['Relationship']


class Relationship(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cardinality: Optional[pulumi.Input['CardinalityTypes']] = None,
                 description: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 display_name: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 expiry_date_time_utc: Optional[pulumi.Input[str]] = None,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PropertyDefinitionArgs']]]]] = None,
                 hub_name: Optional[pulumi.Input[str]] = None,
                 lookup_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RelationshipTypeMappingArgs']]]]] = None,
                 profile_type: Optional[pulumi.Input[str]] = None,
                 related_profile_type: Optional[pulumi.Input[str]] = None,
                 relationship_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        The relationship resource format.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input['CardinalityTypes'] cardinality: The Relationship Cardinality.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] description: Localized descriptions for the Relationship.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] display_name: Localized display name for the Relationship.
        :param pulumi.Input[str] expiry_date_time_utc: The expiry date time in UTC.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PropertyDefinitionArgs']]]] fields: The properties of the Relationship.
        :param pulumi.Input[str] hub_name: The name of the hub.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RelationshipTypeMappingArgs']]]] lookup_mappings: Optional property to be used to map fields in profile to their strong ids in related profile.
        :param pulumi.Input[str] profile_type: Profile type.
        :param pulumi.Input[str] related_profile_type: Related profile being referenced.
        :param pulumi.Input[str] relationship_name: The name of the Relationship.
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

            __props__['cardinality'] = cardinality
            __props__['description'] = description
            __props__['display_name'] = display_name
            __props__['expiry_date_time_utc'] = expiry_date_time_utc
            __props__['fields'] = fields
            if hub_name is None and not opts.urn:
                raise TypeError("Missing required property 'hub_name'")
            __props__['hub_name'] = hub_name
            __props__['lookup_mappings'] = lookup_mappings
            if profile_type is None and not opts.urn:
                raise TypeError("Missing required property 'profile_type'")
            __props__['profile_type'] = profile_type
            if related_profile_type is None and not opts.urn:
                raise TypeError("Missing required property 'related_profile_type'")
            __props__['related_profile_type'] = related_profile_type
            if relationship_name is None and not opts.urn:
                raise TypeError("Missing required property 'relationship_name'")
            __props__['relationship_name'] = relationship_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['name'] = None
            __props__['provisioning_state'] = None
            __props__['relationship_guid_id'] = None
            __props__['tenant_id'] = None
            __props__['type'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:customerinsights/latest:Relationship"), pulumi.Alias(type_="azure-nextgen:customerinsights/v20170101:Relationship")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Relationship, __self__).__init__(
            'azure-nextgen:customerinsights/v20170426:Relationship',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Relationship':
        """
        Get an existing Relationship resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return Relationship(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def cardinality(self) -> pulumi.Output[Optional[str]]:
        """
        The Relationship Cardinality.
        """
        return pulumi.get(self, "cardinality")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Localized descriptions for the Relationship.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Localized display name for the Relationship.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="expiryDateTimeUtc")
    def expiry_date_time_utc(self) -> pulumi.Output[Optional[str]]:
        """
        The expiry date time in UTC.
        """
        return pulumi.get(self, "expiry_date_time_utc")

    @property
    @pulumi.getter
    def fields(self) -> pulumi.Output[Optional[Sequence['outputs.PropertyDefinitionResponse']]]:
        """
        The properties of the Relationship.
        """
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter(name="lookupMappings")
    def lookup_mappings(self) -> pulumi.Output[Optional[Sequence['outputs.RelationshipTypeMappingResponse']]]:
        """
        Optional property to be used to map fields in profile to their strong ids in related profile.
        """
        return pulumi.get(self, "lookup_mappings")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="profileType")
    def profile_type(self) -> pulumi.Output[str]:
        """
        Profile type.
        """
        return pulumi.get(self, "profile_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="relatedProfileType")
    def related_profile_type(self) -> pulumi.Output[str]:
        """
        Related profile being referenced.
        """
        return pulumi.get(self, "related_profile_type")

    @property
    @pulumi.getter(name="relationshipGuidId")
    def relationship_guid_id(self) -> pulumi.Output[str]:
        """
        The relationship guid id.
        """
        return pulumi.get(self, "relationship_guid_id")

    @property
    @pulumi.getter(name="relationshipName")
    def relationship_name(self) -> pulumi.Output[str]:
        """
        The Relationship name.
        """
        return pulumi.get(self, "relationship_name")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[str]:
        """
        The hub name.
        """
        return pulumi.get(self, "tenant_id")

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

