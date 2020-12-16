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

__all__ = ['Domain']


class Domain(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_renew: Optional[pulumi.Input[bool]] = None,
                 consent: Optional[pulumi.Input[pulumi.InputType['DomainPurchaseConsentArgs']]] = None,
                 contact_admin: Optional[pulumi.Input[pulumi.InputType['ContactArgs']]] = None,
                 contact_billing: Optional[pulumi.Input[pulumi.InputType['ContactArgs']]] = None,
                 contact_registrant: Optional[pulumi.Input[pulumi.InputType['ContactArgs']]] = None,
                 contact_tech: Optional[pulumi.Input[pulumi.InputType['ContactArgs']]] = None,
                 created_time: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 domain_not_renewable_reasons: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 expiration_time: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 last_renewed_time: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_host_names: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HostNameArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 name_servers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 privacy: Optional[pulumi.Input[bool]] = None,
                 provisioning_state: Optional[pulumi.Input['ProvisioningState']] = None,
                 ready_for_dns_record_management: Optional[pulumi.Input[bool]] = None,
                 registration_status: Optional[pulumi.Input['DomainStatus']] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Represents a domain

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] auto_renew: If true then domain will renewed automatically
        :param pulumi.Input[pulumi.InputType['DomainPurchaseConsentArgs']] consent: Legal agreement consent
        :param pulumi.Input[pulumi.InputType['ContactArgs']] contact_admin: Admin contact information
        :param pulumi.Input[pulumi.InputType['ContactArgs']] contact_billing: Billing contact information
        :param pulumi.Input[pulumi.InputType['ContactArgs']] contact_registrant: Registrant contact information
        :param pulumi.Input[pulumi.InputType['ContactArgs']] contact_tech: Technical contact information
        :param pulumi.Input[str] created_time: Domain creation timestamp
        :param pulumi.Input[str] domain_name: Name of the domain
        :param pulumi.Input[Sequence[pulumi.Input[str]]] domain_not_renewable_reasons: Reasons why domain is not renewable
        :param pulumi.Input[str] expiration_time: Domain expiration timestamp
        :param pulumi.Input[str] id: Resource Id
        :param pulumi.Input[str] kind: Kind of resource
        :param pulumi.Input[str] last_renewed_time: Timestamp when the domain was renewed last time
        :param pulumi.Input[str] location: Resource Location
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HostNameArgs']]]] managed_host_names: All hostnames derived from the domain and assigned to Azure resources
        :param pulumi.Input[str] name: Resource Name
        :param pulumi.Input[Sequence[pulumi.Input[str]]] name_servers: Name servers
        :param pulumi.Input[bool] privacy: If true then domain privacy is enabled for this domain
        :param pulumi.Input['ProvisioningState'] provisioning_state: Domain provisioning state
        :param pulumi.Input[bool] ready_for_dns_record_management: If true then Azure can assign this domain to Web Apps. This value will be true if domain registration status is active and it is hosted on name servers Azure has programmatic access to
        :param pulumi.Input['DomainStatus'] registration_status: Domain registration status
        :param pulumi.Input[str] resource_group_name: &gt;Name of the resource group
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] type: Resource type
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

            __props__['auto_renew'] = auto_renew
            __props__['consent'] = consent
            __props__['contact_admin'] = contact_admin
            __props__['contact_billing'] = contact_billing
            __props__['contact_registrant'] = contact_registrant
            __props__['contact_tech'] = contact_tech
            __props__['created_time'] = created_time
            if domain_name is None and not opts.urn:
                raise TypeError("Missing required property 'domain_name'")
            __props__['domain_name'] = domain_name
            __props__['domain_not_renewable_reasons'] = domain_not_renewable_reasons
            __props__['expiration_time'] = expiration_time
            __props__['id'] = id
            __props__['kind'] = kind
            __props__['last_renewed_time'] = last_renewed_time
            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__['location'] = location
            __props__['managed_host_names'] = managed_host_names
            __props__['name'] = name
            __props__['name_servers'] = name_servers
            __props__['privacy'] = privacy
            __props__['provisioning_state'] = provisioning_state
            __props__['ready_for_dns_record_management'] = ready_for_dns_record_management
            __props__['registration_status'] = registration_status
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['tags'] = tags
            __props__['type'] = type
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:domainregistration/latest:Domain"), pulumi.Alias(type_="azure-nextgen:domainregistration/v20150401:Domain"), pulumi.Alias(type_="azure-nextgen:domainregistration/v20180201:Domain"), pulumi.Alias(type_="azure-nextgen:domainregistration/v20190801:Domain"), pulumi.Alias(type_="azure-nextgen:domainregistration/v20200601:Domain"), pulumi.Alias(type_="azure-nextgen:domainregistration/v20200901:Domain")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Domain, __self__).__init__(
            'azure-nextgen:domainregistration/v20150801:Domain',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Domain':
        """
        Get an existing Domain resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return Domain(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autoRenew")
    def auto_renew(self) -> pulumi.Output[Optional[bool]]:
        """
        If true then domain will renewed automatically
        """
        return pulumi.get(self, "auto_renew")

    @property
    @pulumi.getter
    def consent(self) -> pulumi.Output[Optional['outputs.DomainPurchaseConsentResponse']]:
        """
        Legal agreement consent
        """
        return pulumi.get(self, "consent")

    @property
    @pulumi.getter(name="contactAdmin")
    def contact_admin(self) -> pulumi.Output[Optional['outputs.ContactResponse']]:
        """
        Admin contact information
        """
        return pulumi.get(self, "contact_admin")

    @property
    @pulumi.getter(name="contactBilling")
    def contact_billing(self) -> pulumi.Output[Optional['outputs.ContactResponse']]:
        """
        Billing contact information
        """
        return pulumi.get(self, "contact_billing")

    @property
    @pulumi.getter(name="contactRegistrant")
    def contact_registrant(self) -> pulumi.Output[Optional['outputs.ContactResponse']]:
        """
        Registrant contact information
        """
        return pulumi.get(self, "contact_registrant")

    @property
    @pulumi.getter(name="contactTech")
    def contact_tech(self) -> pulumi.Output[Optional['outputs.ContactResponse']]:
        """
        Technical contact information
        """
        return pulumi.get(self, "contact_tech")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[Optional[str]]:
        """
        Domain creation timestamp
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter(name="domainNotRenewableReasons")
    def domain_not_renewable_reasons(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Reasons why domain is not renewable
        """
        return pulumi.get(self, "domain_not_renewable_reasons")

    @property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> pulumi.Output[Optional[str]]:
        """
        Domain expiration timestamp
        """
        return pulumi.get(self, "expiration_time")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Kind of resource
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="lastRenewedTime")
    def last_renewed_time(self) -> pulumi.Output[Optional[str]]:
        """
        Timestamp when the domain was renewed last time
        """
        return pulumi.get(self, "last_renewed_time")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource Location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managedHostNames")
    def managed_host_names(self) -> pulumi.Output[Optional[Sequence['outputs.HostNameResponse']]]:
        """
        All hostnames derived from the domain and assigned to Azure resources
        """
        return pulumi.get(self, "managed_host_names")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        Resource Name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nameServers")
    def name_servers(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Name servers
        """
        return pulumi.get(self, "name_servers")

    @property
    @pulumi.getter
    def privacy(self) -> pulumi.Output[Optional[bool]]:
        """
        If true then domain privacy is enabled for this domain
        """
        return pulumi.get(self, "privacy")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        Domain provisioning state
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="readyForDnsRecordManagement")
    def ready_for_dns_record_management(self) -> pulumi.Output[Optional[bool]]:
        """
        If true then Azure can assign this domain to Web Apps. This value will be true if domain registration status is active and it is hosted on name servers Azure has programmatic access to
        """
        return pulumi.get(self, "ready_for_dns_record_management")

    @property
    @pulumi.getter(name="registrationStatus")
    def registration_status(self) -> pulumi.Output[Optional[str]]:
        """
        Domain registration status
        """
        return pulumi.get(self, "registration_status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

