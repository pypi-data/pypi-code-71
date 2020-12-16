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

__all__ = ['ReportByBillingAccount']


class ReportByBillingAccount(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 billing_account_id: Optional[pulumi.Input[str]] = None,
                 definition: Optional[pulumi.Input[pulumi.InputType['ReportDefinitionArgs']]] = None,
                 delivery_info: Optional[pulumi.Input[pulumi.InputType['ReportDeliveryInfoArgs']]] = None,
                 format: Optional[pulumi.Input[Union[str, 'FormatType']]] = None,
                 report_name: Optional[pulumi.Input[str]] = None,
                 schedule: Optional[pulumi.Input[pulumi.InputType['ReportScheduleArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        A report resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] billing_account_id: BillingAccount ID
        :param pulumi.Input[pulumi.InputType['ReportDefinitionArgs']] definition: Has definition for the report.
        :param pulumi.Input[pulumi.InputType['ReportDeliveryInfoArgs']] delivery_info: Has delivery information for the report.
        :param pulumi.Input[Union[str, 'FormatType']] format: The format of the report being delivered.
        :param pulumi.Input[str] report_name: Report Name.
        :param pulumi.Input[pulumi.InputType['ReportScheduleArgs']] schedule: Has schedule information for the report.
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

            if billing_account_id is None and not opts.urn:
                raise TypeError("Missing required property 'billing_account_id'")
            __props__['billing_account_id'] = billing_account_id
            if definition is None and not opts.urn:
                raise TypeError("Missing required property 'definition'")
            __props__['definition'] = definition
            if delivery_info is None and not opts.urn:
                raise TypeError("Missing required property 'delivery_info'")
            __props__['delivery_info'] = delivery_info
            __props__['format'] = format
            if report_name is None and not opts.urn:
                raise TypeError("Missing required property 'report_name'")
            __props__['report_name'] = report_name
            __props__['schedule'] = schedule
            __props__['name'] = None
            __props__['tags'] = None
            __props__['type'] = None
        super(ReportByBillingAccount, __self__).__init__(
            'azure-nextgen:billing/v20180801preview:ReportByBillingAccount',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ReportByBillingAccount':
        """
        Get an existing ReportByBillingAccount resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return ReportByBillingAccount(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def definition(self) -> pulumi.Output['outputs.ReportDefinitionResponse']:
        """
        Has definition for the report.
        """
        return pulumi.get(self, "definition")

    @property
    @pulumi.getter(name="deliveryInfo")
    def delivery_info(self) -> pulumi.Output['outputs.ReportDeliveryInfoResponse']:
        """
        Has delivery information for the report.
        """
        return pulumi.get(self, "delivery_info")

    @property
    @pulumi.getter
    def format(self) -> pulumi.Output[Optional[str]]:
        """
        The format of the report being delivered.
        """
        return pulumi.get(self, "format")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def schedule(self) -> pulumi.Output[Optional['outputs.ReportScheduleResponse']]:
        """
        Has schedule information for the report.
        """
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

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

