# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables
from ._enums import *

__all__ = ['Assessment']


class Assessment(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assessment_name: Optional[pulumi.Input[str]] = None,
                 azure_hybrid_use_benefit: Optional[pulumi.Input[Union[str, 'AzureHybridUseBenefit']]] = None,
                 azure_location: Optional[pulumi.Input[Union[str, 'AzureLocation']]] = None,
                 azure_offer_code: Optional[pulumi.Input[Union[str, 'AzureOfferCode']]] = None,
                 azure_pricing_tier: Optional[pulumi.Input[Union[str, 'AzurePricingTier']]] = None,
                 azure_storage_redundancy: Optional[pulumi.Input[Union[str, 'AzureStorageRedundancy']]] = None,
                 currency: Optional[pulumi.Input[Union[str, 'Currency']]] = None,
                 discount_percentage: Optional[pulumi.Input[float]] = None,
                 e_tag: Optional[pulumi.Input[str]] = None,
                 group_name: Optional[pulumi.Input[str]] = None,
                 percentile: Optional[pulumi.Input[Union[str, 'Percentile']]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scaling_factor: Optional[pulumi.Input[float]] = None,
                 sizing_criterion: Optional[pulumi.Input[Union[str, 'AssessmentSizingCriterion']]] = None,
                 stage: Optional[pulumi.Input[Union[str, 'AssessmentStage']]] = None,
                 time_range: Optional[pulumi.Input[Union[str, 'TimeRange']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        An assessment created for a group in the Migration project.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] assessment_name: Unique name of an assessment within a project.
        :param pulumi.Input[Union[str, 'AzureHybridUseBenefit']] azure_hybrid_use_benefit: AHUB discount on windows virtual machines.
        :param pulumi.Input[Union[str, 'AzureLocation']] azure_location: Target Azure location for which the machines should be assessed. These enums are the same as used by Compute API.
        :param pulumi.Input[Union[str, 'AzureOfferCode']] azure_offer_code: Offer code according to which cost estimation is done.
        :param pulumi.Input[Union[str, 'AzurePricingTier']] azure_pricing_tier: Pricing tier for Size evaluation.
        :param pulumi.Input[Union[str, 'AzureStorageRedundancy']] azure_storage_redundancy: Storage Redundancy type offered by Azure.
        :param pulumi.Input[Union[str, 'Currency']] currency: Currency to report prices in.
        :param pulumi.Input[float] discount_percentage: Custom discount percentage to be applied on final costs. Can be in the range [0, 100].
        :param pulumi.Input[str] e_tag: For optimistic concurrency control.
        :param pulumi.Input[str] group_name: Unique name of a group within a project.
        :param pulumi.Input[Union[str, 'Percentile']] percentile: Percentile of performance data used to recommend Azure size.
        :param pulumi.Input[str] project_name: Name of the Azure Migrate project.
        :param pulumi.Input[str] resource_group_name: Name of the Azure Resource Group that project is part of.
        :param pulumi.Input[float] scaling_factor: Scaling factor used over utilization data to add a performance buffer for new machines to be created in Azure. Min Value = 1.0, Max value = 1.9, Default = 1.3.
        :param pulumi.Input[Union[str, 'AssessmentSizingCriterion']] sizing_criterion: Assessment sizing criterion.
        :param pulumi.Input[Union[str, 'AssessmentStage']] stage: User configurable setting that describes the status of the assessment.
        :param pulumi.Input[Union[str, 'TimeRange']] time_range: Time range of performance data used to recommend a size.
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

            if assessment_name is None and not opts.urn:
                raise TypeError("Missing required property 'assessment_name'")
            __props__['assessment_name'] = assessment_name
            if azure_hybrid_use_benefit is None and not opts.urn:
                raise TypeError("Missing required property 'azure_hybrid_use_benefit'")
            __props__['azure_hybrid_use_benefit'] = azure_hybrid_use_benefit
            if azure_location is None and not opts.urn:
                raise TypeError("Missing required property 'azure_location'")
            __props__['azure_location'] = azure_location
            if azure_offer_code is None and not opts.urn:
                raise TypeError("Missing required property 'azure_offer_code'")
            __props__['azure_offer_code'] = azure_offer_code
            if azure_pricing_tier is None and not opts.urn:
                raise TypeError("Missing required property 'azure_pricing_tier'")
            __props__['azure_pricing_tier'] = azure_pricing_tier
            if azure_storage_redundancy is None and not opts.urn:
                raise TypeError("Missing required property 'azure_storage_redundancy'")
            __props__['azure_storage_redundancy'] = azure_storage_redundancy
            if currency is None and not opts.urn:
                raise TypeError("Missing required property 'currency'")
            __props__['currency'] = currency
            if discount_percentage is None and not opts.urn:
                raise TypeError("Missing required property 'discount_percentage'")
            __props__['discount_percentage'] = discount_percentage
            __props__['e_tag'] = e_tag
            if group_name is None and not opts.urn:
                raise TypeError("Missing required property 'group_name'")
            __props__['group_name'] = group_name
            if percentile is None and not opts.urn:
                raise TypeError("Missing required property 'percentile'")
            __props__['percentile'] = percentile
            if project_name is None and not opts.urn:
                raise TypeError("Missing required property 'project_name'")
            __props__['project_name'] = project_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            if scaling_factor is None and not opts.urn:
                raise TypeError("Missing required property 'scaling_factor'")
            __props__['scaling_factor'] = scaling_factor
            if sizing_criterion is None and not opts.urn:
                raise TypeError("Missing required property 'sizing_criterion'")
            __props__['sizing_criterion'] = sizing_criterion
            if stage is None and not opts.urn:
                raise TypeError("Missing required property 'stage'")
            __props__['stage'] = stage
            if time_range is None and not opts.urn:
                raise TypeError("Missing required property 'time_range'")
            __props__['time_range'] = time_range
            __props__['confidence_rating_in_percentage'] = None
            __props__['created_timestamp'] = None
            __props__['monthly_bandwidth_cost'] = None
            __props__['monthly_compute_cost'] = None
            __props__['monthly_storage_cost'] = None
            __props__['name'] = None
            __props__['number_of_machines'] = None
            __props__['prices_timestamp'] = None
            __props__['status'] = None
            __props__['type'] = None
            __props__['updated_timestamp'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:migrate/v20171111preview:Assessment")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Assessment, __self__).__init__(
            'azure-nextgen:migrate/v20180202:Assessment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Assessment':
        """
        Get an existing Assessment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return Assessment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="azureHybridUseBenefit")
    def azure_hybrid_use_benefit(self) -> pulumi.Output[str]:
        """
        AHUB discount on windows virtual machines.
        """
        return pulumi.get(self, "azure_hybrid_use_benefit")

    @property
    @pulumi.getter(name="azureLocation")
    def azure_location(self) -> pulumi.Output[str]:
        """
        Target Azure location for which the machines should be assessed. These enums are the same as used by Compute API.
        """
        return pulumi.get(self, "azure_location")

    @property
    @pulumi.getter(name="azureOfferCode")
    def azure_offer_code(self) -> pulumi.Output[str]:
        """
        Offer code according to which cost estimation is done.
        """
        return pulumi.get(self, "azure_offer_code")

    @property
    @pulumi.getter(name="azurePricingTier")
    def azure_pricing_tier(self) -> pulumi.Output[str]:
        """
        Pricing tier for Size evaluation.
        """
        return pulumi.get(self, "azure_pricing_tier")

    @property
    @pulumi.getter(name="azureStorageRedundancy")
    def azure_storage_redundancy(self) -> pulumi.Output[str]:
        """
        Storage Redundancy type offered by Azure.
        """
        return pulumi.get(self, "azure_storage_redundancy")

    @property
    @pulumi.getter(name="confidenceRatingInPercentage")
    def confidence_rating_in_percentage(self) -> pulumi.Output[float]:
        """
        Confidence rating percentage for assessment. Can be in the range [0, 100].
        """
        return pulumi.get(self, "confidence_rating_in_percentage")

    @property
    @pulumi.getter(name="createdTimestamp")
    def created_timestamp(self) -> pulumi.Output[str]:
        """
        Time when this project was created. Date-Time represented in ISO-8601 format.
        """
        return pulumi.get(self, "created_timestamp")

    @property
    @pulumi.getter
    def currency(self) -> pulumi.Output[str]:
        """
        Currency to report prices in.
        """
        return pulumi.get(self, "currency")

    @property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> pulumi.Output[float]:
        """
        Custom discount percentage to be applied on final costs. Can be in the range [0, 100].
        """
        return pulumi.get(self, "discount_percentage")

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[Optional[str]]:
        """
        For optimistic concurrency control.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter(name="monthlyBandwidthCost")
    def monthly_bandwidth_cost(self) -> pulumi.Output[float]:
        """
        Monthly network cost estimate for the machines that are part of this assessment as a group, for a 31-day month.
        """
        return pulumi.get(self, "monthly_bandwidth_cost")

    @property
    @pulumi.getter(name="monthlyComputeCost")
    def monthly_compute_cost(self) -> pulumi.Output[float]:
        """
        Monthly compute cost estimate for the machines that are part of this assessment as a group, for a 31-day month.
        """
        return pulumi.get(self, "monthly_compute_cost")

    @property
    @pulumi.getter(name="monthlyStorageCost")
    def monthly_storage_cost(self) -> pulumi.Output[float]:
        """
        Monthly storage cost estimate for the machines that are part of this assessment as a group, for a 31-day month.
        """
        return pulumi.get(self, "monthly_storage_cost")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Unique name of an assessment.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="numberOfMachines")
    def number_of_machines(self) -> pulumi.Output[int]:
        """
        Number of assessed machines part of this assessment.
        """
        return pulumi.get(self, "number_of_machines")

    @property
    @pulumi.getter
    def percentile(self) -> pulumi.Output[str]:
        """
        Percentile of performance data used to recommend Azure size.
        """
        return pulumi.get(self, "percentile")

    @property
    @pulumi.getter(name="pricesTimestamp")
    def prices_timestamp(self) -> pulumi.Output[str]:
        """
        Time when the Azure Prices were queried. Date-Time represented in ISO-8601 format.
        """
        return pulumi.get(self, "prices_timestamp")

    @property
    @pulumi.getter(name="scalingFactor")
    def scaling_factor(self) -> pulumi.Output[float]:
        """
        Scaling factor used over utilization data to add a performance buffer for new machines to be created in Azure. Min Value = 1.0, Max value = 1.9, Default = 1.3.
        """
        return pulumi.get(self, "scaling_factor")

    @property
    @pulumi.getter(name="sizingCriterion")
    def sizing_criterion(self) -> pulumi.Output[str]:
        """
        Assessment sizing criterion.
        """
        return pulumi.get(self, "sizing_criterion")

    @property
    @pulumi.getter
    def stage(self) -> pulumi.Output[str]:
        """
        User configurable setting that describes the status of the assessment.
        """
        return pulumi.get(self, "stage")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Whether the assessment has been created and is valid.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="timeRange")
    def time_range(self) -> pulumi.Output[str]:
        """
        Time range of performance data used to recommend a size.
        """
        return pulumi.get(self, "time_range")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the object = [Microsoft.Migrate/projects/groups/assessments].
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updatedTimestamp")
    def updated_timestamp(self) -> pulumi.Output[str]:
        """
        Time when this project was last updated. Date-Time represented in ISO-8601 format.
        """
        return pulumi.get(self, "updated_timestamp")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

