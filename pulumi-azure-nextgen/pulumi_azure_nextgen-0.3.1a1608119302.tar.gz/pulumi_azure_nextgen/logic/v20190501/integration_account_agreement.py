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

__all__ = ['IntegrationAccountAgreement']


class IntegrationAccountAgreement(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agreement_name: Optional[pulumi.Input[str]] = None,
                 agreement_type: Optional[pulumi.Input['AgreementType']] = None,
                 content: Optional[pulumi.Input[pulumi.InputType['AgreementContentArgs']]] = None,
                 guest_identity: Optional[pulumi.Input[pulumi.InputType['BusinessIdentityArgs']]] = None,
                 guest_partner: Optional[pulumi.Input[str]] = None,
                 host_identity: Optional[pulumi.Input[pulumi.InputType['BusinessIdentityArgs']]] = None,
                 host_partner: Optional[pulumi.Input[str]] = None,
                 integration_account_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[Any] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        The integration account agreement.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] agreement_name: The integration account agreement name.
        :param pulumi.Input['AgreementType'] agreement_type: The agreement type.
        :param pulumi.Input[pulumi.InputType['AgreementContentArgs']] content: The agreement content.
        :param pulumi.Input[pulumi.InputType['BusinessIdentityArgs']] guest_identity: The business identity of the guest partner.
        :param pulumi.Input[str] guest_partner: The integration account partner that is set as guest partner for this agreement.
        :param pulumi.Input[pulumi.InputType['BusinessIdentityArgs']] host_identity: The business identity of the host partner.
        :param pulumi.Input[str] host_partner: The integration account partner that is set as host partner for this agreement.
        :param pulumi.Input[str] integration_account_name: The integration account name.
        :param pulumi.Input[str] location: The resource location.
        :param Any metadata: The metadata.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
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

            if agreement_name is None and not opts.urn:
                raise TypeError("Missing required property 'agreement_name'")
            __props__['agreement_name'] = agreement_name
            if agreement_type is None and not opts.urn:
                raise TypeError("Missing required property 'agreement_type'")
            __props__['agreement_type'] = agreement_type
            if content is None and not opts.urn:
                raise TypeError("Missing required property 'content'")
            __props__['content'] = content
            if guest_identity is None and not opts.urn:
                raise TypeError("Missing required property 'guest_identity'")
            __props__['guest_identity'] = guest_identity
            if guest_partner is None and not opts.urn:
                raise TypeError("Missing required property 'guest_partner'")
            __props__['guest_partner'] = guest_partner
            if host_identity is None and not opts.urn:
                raise TypeError("Missing required property 'host_identity'")
            __props__['host_identity'] = host_identity
            if host_partner is None and not opts.urn:
                raise TypeError("Missing required property 'host_partner'")
            __props__['host_partner'] = host_partner
            if integration_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'integration_account_name'")
            __props__['integration_account_name'] = integration_account_name
            __props__['location'] = location
            __props__['metadata'] = metadata
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['tags'] = tags
            __props__['changed_time'] = None
            __props__['created_time'] = None
            __props__['name'] = None
            __props__['type'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:logic/latest:IntegrationAccountAgreement"), pulumi.Alias(type_="azure-nextgen:logic/v20150801preview:IntegrationAccountAgreement"), pulumi.Alias(type_="azure-nextgen:logic/v20160601:IntegrationAccountAgreement"), pulumi.Alias(type_="azure-nextgen:logic/v20180701preview:IntegrationAccountAgreement")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(IntegrationAccountAgreement, __self__).__init__(
            'azure-nextgen:logic/v20190501:IntegrationAccountAgreement',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'IntegrationAccountAgreement':
        """
        Get an existing IntegrationAccountAgreement resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return IntegrationAccountAgreement(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="agreementType")
    def agreement_type(self) -> pulumi.Output[str]:
        """
        The agreement type.
        """
        return pulumi.get(self, "agreement_type")

    @property
    @pulumi.getter(name="changedTime")
    def changed_time(self) -> pulumi.Output[str]:
        """
        The changed time.
        """
        return pulumi.get(self, "changed_time")

    @property
    @pulumi.getter
    def content(self) -> pulumi.Output['outputs.AgreementContentResponse']:
        """
        The agreement content.
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[str]:
        """
        The created time.
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter(name="guestIdentity")
    def guest_identity(self) -> pulumi.Output['outputs.BusinessIdentityResponse']:
        """
        The business identity of the guest partner.
        """
        return pulumi.get(self, "guest_identity")

    @property
    @pulumi.getter(name="guestPartner")
    def guest_partner(self) -> pulumi.Output[str]:
        """
        The integration account partner that is set as guest partner for this agreement.
        """
        return pulumi.get(self, "guest_partner")

    @property
    @pulumi.getter(name="hostIdentity")
    def host_identity(self) -> pulumi.Output['outputs.BusinessIdentityResponse']:
        """
        The business identity of the host partner.
        """
        return pulumi.get(self, "host_identity")

    @property
    @pulumi.getter(name="hostPartner")
    def host_partner(self) -> pulumi.Output[str]:
        """
        The integration account partner that is set as host partner for this agreement.
        """
        return pulumi.get(self, "host_partner")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Any]]:
        """
        The metadata.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Gets the resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Gets the resource type.
        """
        return pulumi.get(self, "type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

