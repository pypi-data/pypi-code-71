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

__all__ = ['Export']


class Export(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 definition: Optional[pulumi.Input[pulumi.InputType['ExportDefinitionArgs']]] = None,
                 delivery_info: Optional[pulumi.Input[pulumi.InputType['ExportDeliveryInfoArgs']]] = None,
                 e_tag: Optional[pulumi.Input[str]] = None,
                 export_name: Optional[pulumi.Input[str]] = None,
                 format: Optional[pulumi.Input[Union[str, 'FormatType']]] = None,
                 schedule: Optional[pulumi.Input[pulumi.InputType['ExportScheduleArgs']]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        A export resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ExportDefinitionArgs']] definition: Has definition for the export.
        :param pulumi.Input[pulumi.InputType['ExportDeliveryInfoArgs']] delivery_info: Has delivery information for the export.
        :param pulumi.Input[str] e_tag: eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.
        :param pulumi.Input[str] export_name: Export Name.
        :param pulumi.Input[Union[str, 'FormatType']] format: The format of the export being delivered.
        :param pulumi.Input[pulumi.InputType['ExportScheduleArgs']] schedule: Has schedule information for the export.
        :param pulumi.Input[str] scope: The scope associated with query and export operations. This includes '/subscriptions/{subscriptionId}/' for subscription scope, '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope and '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for Department scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope, '/providers/Microsoft.Management/managementGroups/{managementGroupId} for Management Group scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for billingProfile scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}' for invoiceSection scope, and '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}' specific for partners.
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

            if definition is None and not opts.urn:
                raise TypeError("Missing required property 'definition'")
            __props__['definition'] = definition
            if delivery_info is None and not opts.urn:
                raise TypeError("Missing required property 'delivery_info'")
            __props__['delivery_info'] = delivery_info
            __props__['e_tag'] = e_tag
            if export_name is None and not opts.urn:
                raise TypeError("Missing required property 'export_name'")
            __props__['export_name'] = export_name
            __props__['format'] = format
            __props__['schedule'] = schedule
            if scope is None and not opts.urn:
                raise TypeError("Missing required property 'scope'")
            __props__['scope'] = scope
            __props__['name'] = None
            __props__['type'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:costmanagement/latest:Export"), pulumi.Alias(type_="azure-nextgen:costmanagement/v20190101:Export"), pulumi.Alias(type_="azure-nextgen:costmanagement/v20190901:Export"), pulumi.Alias(type_="azure-nextgen:costmanagement/v20191001:Export"), pulumi.Alias(type_="azure-nextgen:costmanagement/v20200601:Export")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Export, __self__).__init__(
            'azure-nextgen:costmanagement/v20191101:Export',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Export':
        """
        Get an existing Export resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return Export(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def definition(self) -> pulumi.Output['outputs.ExportDefinitionResponse']:
        """
        Has definition for the export.
        """
        return pulumi.get(self, "definition")

    @property
    @pulumi.getter(name="deliveryInfo")
    def delivery_info(self) -> pulumi.Output['outputs.ExportDeliveryInfoResponse']:
        """
        Has delivery information for the export.
        """
        return pulumi.get(self, "delivery_info")

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[Optional[str]]:
        """
        eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter
    def format(self) -> pulumi.Output[Optional[str]]:
        """
        The format of the export being delivered.
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
    def schedule(self) -> pulumi.Output[Optional['outputs.ExportScheduleResponse']]:
        """
        Has schedule information for the export.
        """
        return pulumi.get(self, "schedule")

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

