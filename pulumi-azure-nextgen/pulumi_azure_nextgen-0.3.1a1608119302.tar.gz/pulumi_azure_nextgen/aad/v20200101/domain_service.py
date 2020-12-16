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

__all__ = ['DomainService']


class DomainService(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_configuration_type: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 domain_security_settings: Optional[pulumi.Input[pulumi.InputType['DomainSecuritySettingsArgs']]] = None,
                 domain_service_name: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 filtered_sync: Optional[pulumi.Input[Union[str, 'FilteredSync']]] = None,
                 ldaps_settings: Optional[pulumi.Input[pulumi.InputType['LdapsSettingsArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 migration_properties: Optional[pulumi.Input[pulumi.InputType['MigrationPropertiesArgs']]] = None,
                 notification_settings: Optional[pulumi.Input[pulumi.InputType['NotificationSettingsArgs']]] = None,
                 replica_sets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ReplicaSetArgs']]]]] = None,
                 resource_forest_settings: Optional[pulumi.Input[pulumi.InputType['ResourceForestSettingsArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Domain service.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_configuration_type: Domain Configuration Type
        :param pulumi.Input[str] domain_name: The name of the Azure domain that the user would like to deploy Domain Services to.
        :param pulumi.Input[pulumi.InputType['DomainSecuritySettingsArgs']] domain_security_settings: DomainSecurity Settings
        :param pulumi.Input[str] domain_service_name: The name of the domain service.
        :param pulumi.Input[str] etag: Resource etag
        :param pulumi.Input[Union[str, 'FilteredSync']] filtered_sync: Enabled or Disabled flag to turn on Group-based filtered sync
        :param pulumi.Input[pulumi.InputType['LdapsSettingsArgs']] ldaps_settings: Secure LDAP Settings
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[pulumi.InputType['MigrationPropertiesArgs']] migration_properties: Migration Properties
        :param pulumi.Input[pulumi.InputType['NotificationSettingsArgs']] notification_settings: Notification Settings
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ReplicaSetArgs']]]] replica_sets: List of ReplicaSets
        :param pulumi.Input[pulumi.InputType['ResourceForestSettingsArgs']] resource_forest_settings: Resource Forest Settings
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        :param pulumi.Input[str] sku: Sku Type
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
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

            __props__['domain_configuration_type'] = domain_configuration_type
            __props__['domain_name'] = domain_name
            __props__['domain_security_settings'] = domain_security_settings
            if domain_service_name is None and not opts.urn:
                raise TypeError("Missing required property 'domain_service_name'")
            __props__['domain_service_name'] = domain_service_name
            __props__['etag'] = etag
            __props__['filtered_sync'] = filtered_sync
            __props__['ldaps_settings'] = ldaps_settings
            __props__['location'] = location
            __props__['migration_properties'] = migration_properties
            __props__['notification_settings'] = notification_settings
            __props__['replica_sets'] = replica_sets
            __props__['resource_forest_settings'] = resource_forest_settings
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['sku'] = sku
            __props__['tags'] = tags
            __props__['deployment_id'] = None
            __props__['name'] = None
            __props__['provisioning_state'] = None
            __props__['sync_owner'] = None
            __props__['tenant_id'] = None
            __props__['type'] = None
            __props__['version'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:aad/latest:DomainService"), pulumi.Alias(type_="azure-nextgen:aad/v20170101:DomainService"), pulumi.Alias(type_="azure-nextgen:aad/v20170601:DomainService")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DomainService, __self__).__init__(
            'azure-nextgen:aad/v20200101:DomainService',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DomainService':
        """
        Get an existing DomainService resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return DomainService(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> pulumi.Output[str]:
        """
        Deployment Id
        """
        return pulumi.get(self, "deployment_id")

    @property
    @pulumi.getter(name="domainConfigurationType")
    def domain_configuration_type(self) -> pulumi.Output[Optional[str]]:
        """
        Domain Configuration Type
        """
        return pulumi.get(self, "domain_configuration_type")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the Azure domain that the user would like to deploy Domain Services to.
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="domainSecuritySettings")
    def domain_security_settings(self) -> pulumi.Output[Optional['outputs.DomainSecuritySettingsResponse']]:
        """
        DomainSecurity Settings
        """
        return pulumi.get(self, "domain_security_settings")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Resource etag
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="filteredSync")
    def filtered_sync(self) -> pulumi.Output[Optional[str]]:
        """
        Enabled or Disabled flag to turn on Group-based filtered sync
        """
        return pulumi.get(self, "filtered_sync")

    @property
    @pulumi.getter(name="ldapsSettings")
    def ldaps_settings(self) -> pulumi.Output[Optional['outputs.LdapsSettingsResponse']]:
        """
        Secure LDAP Settings
        """
        return pulumi.get(self, "ldaps_settings")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="migrationProperties")
    def migration_properties(self) -> pulumi.Output[Optional['outputs.MigrationPropertiesResponse']]:
        """
        Migration Properties
        """
        return pulumi.get(self, "migration_properties")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="notificationSettings")
    def notification_settings(self) -> pulumi.Output[Optional['outputs.NotificationSettingsResponse']]:
        """
        Notification Settings
        """
        return pulumi.get(self, "notification_settings")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        the current deployment or provisioning state, which only appears in the response.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="replicaSets")
    def replica_sets(self) -> pulumi.Output[Optional[Sequence['outputs.ReplicaSetResponse']]]:
        """
        List of ReplicaSets
        """
        return pulumi.get(self, "replica_sets")

    @property
    @pulumi.getter(name="resourceForestSettings")
    def resource_forest_settings(self) -> pulumi.Output[Optional['outputs.ResourceForestSettingsResponse']]:
        """
        Resource Forest Settings
        """
        return pulumi.get(self, "resource_forest_settings")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[str]]:
        """
        Sku Type
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="syncOwner")
    def sync_owner(self) -> pulumi.Output[str]:
        """
        SyncOwner ReplicaSet Id
        """
        return pulumi.get(self, "sync_owner")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[str]:
        """
        Azure Active Directory Tenant Id
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[int]:
        """
        Data Model Version
        """
        return pulumi.get(self, "version")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

