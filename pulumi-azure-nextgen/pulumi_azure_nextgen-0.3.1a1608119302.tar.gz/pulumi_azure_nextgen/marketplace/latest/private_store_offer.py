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

__all__ = ['PrivateStoreOffer']


class PrivateStoreOffer(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 e_tag: Optional[pulumi.Input[str]] = None,
                 icon_file_uris: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 offer_id: Optional[pulumi.Input[str]] = None,
                 plans: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PlanArgs']]]]] = None,
                 private_store_id: Optional[pulumi.Input[str]] = None,
                 specific_plan_ids_limitation: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 update_suppressed_due_idempotence: Optional[pulumi.Input[bool]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        The privateStore offer data structure.
        Latest API Version: 2020-01-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] e_tag: Identifier for purposes of race condition
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] icon_file_uris: Icon File Uris
        :param pulumi.Input[str] offer_id: The offer ID to update or delete
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PlanArgs']]]] plans: Offer plans
        :param pulumi.Input[str] private_store_id: The store ID - must use the tenant ID
        :param pulumi.Input[Sequence[pulumi.Input[str]]] specific_plan_ids_limitation: Plan ids limitation for this offer
        :param pulumi.Input[bool] update_suppressed_due_idempotence: Indicating whether the offer was not updated to db (true = not updated). If the allow list is identical to the existed one in db, the offer would not be updated.
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

            __props__['e_tag'] = e_tag
            __props__['icon_file_uris'] = icon_file_uris
            if offer_id is None and not opts.urn:
                raise TypeError("Missing required property 'offer_id'")
            __props__['offer_id'] = offer_id
            __props__['plans'] = plans
            if private_store_id is None and not opts.urn:
                raise TypeError("Missing required property 'private_store_id'")
            __props__['private_store_id'] = private_store_id
            __props__['specific_plan_ids_limitation'] = specific_plan_ids_limitation
            __props__['update_suppressed_due_idempotence'] = update_suppressed_due_idempotence
            __props__['created_at'] = None
            __props__['modified_at'] = None
            __props__['name'] = None
            __props__['offer_display_name'] = None
            __props__['publisher_display_name'] = None
            __props__['type'] = None
            __props__['unique_offer_id'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:marketplace/v20200101:PrivateStoreOffer")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PrivateStoreOffer, __self__).__init__(
            'azure-nextgen:marketplace/latest:PrivateStoreOffer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PrivateStoreOffer':
        """
        Get an existing PrivateStoreOffer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return PrivateStoreOffer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Private store offer creation date
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[Optional[str]]:
        """
        Identifier for purposes of race condition
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter(name="iconFileUris")
    def icon_file_uris(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Icon File Uris
        """
        return pulumi.get(self, "icon_file_uris")

    @property
    @pulumi.getter(name="modifiedAt")
    def modified_at(self) -> pulumi.Output[str]:
        """
        Private store offer modification date
        """
        return pulumi.get(self, "modified_at")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="offerDisplayName")
    def offer_display_name(self) -> pulumi.Output[str]:
        """
        It will be displayed prominently in the marketplace
        """
        return pulumi.get(self, "offer_display_name")

    @property
    @pulumi.getter
    def plans(self) -> pulumi.Output[Optional[Sequence['outputs.PlanResponse']]]:
        """
        Offer plans
        """
        return pulumi.get(self, "plans")

    @property
    @pulumi.getter(name="privateStoreId")
    def private_store_id(self) -> pulumi.Output[str]:
        """
        Private store unique id
        """
        return pulumi.get(self, "private_store_id")

    @property
    @pulumi.getter(name="publisherDisplayName")
    def publisher_display_name(self) -> pulumi.Output[str]:
        """
        Publisher name that will be displayed prominently in the marketplace
        """
        return pulumi.get(self, "publisher_display_name")

    @property
    @pulumi.getter(name="specificPlanIdsLimitation")
    def specific_plan_ids_limitation(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Plan ids limitation for this offer
        """
        return pulumi.get(self, "specific_plan_ids_limitation")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="uniqueOfferId")
    def unique_offer_id(self) -> pulumi.Output[str]:
        """
        Offers unique id
        """
        return pulumi.get(self, "unique_offer_id")

    @property
    @pulumi.getter(name="updateSuppressedDueIdempotence")
    def update_suppressed_due_idempotence(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicating whether the offer was not updated to db (true = not updated). If the allow list is identical to the existed one in db, the offer would not be updated.
        """
        return pulumi.get(self, "update_suppressed_due_idempotence")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

