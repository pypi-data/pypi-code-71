# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['Budget']


class Budget(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 budget_type: Optional[pulumi.Input[str]] = None,
                 cost_filters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 cost_types: Optional[pulumi.Input[pulumi.InputType['BudgetCostTypesArgs']]] = None,
                 limit_amount: Optional[pulumi.Input[str]] = None,
                 limit_unit: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 notifications: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BudgetNotificationArgs']]]]] = None,
                 time_period_end: Optional[pulumi.Input[str]] = None,
                 time_period_start: Optional[pulumi.Input[str]] = None,
                 time_unit: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a budgets budget resource. Budgets use the cost visualisation provided by Cost Explorer to show you the status of your budgets, to provide forecasts of your estimated costs, and to track your AWS usage, including your free tier usage.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        ec2 = aws.budgets.Budget("ec2",
            budget_type="COST",
            cost_filters={
                "Service": "Amazon Elastic Compute Cloud - Compute",
            },
            limit_amount="1200",
            limit_unit="USD",
            notifications=[aws.budgets.BudgetNotificationArgs(
                comparison_operator="GREATER_THAN",
                notification_type="FORECASTED",
                subscriber_email_addresses=["test@example.com"],
                threshold=100,
                threshold_type="PERCENTAGE",
            )],
            time_period_end="2087-06-15_00:00",
            time_period_start="2017-07-01_00:00",
            time_unit="MONTHLY")
        ```

        Create a budget for *$100*.

        ```python
        import pulumi
        import pulumi_aws as aws

        cost = aws.budgets.Budget("cost",
            budget_type="COST",
            limit_amount="100",
            limit_unit="USD")
        ```

        Create a budget for s3 with a limit of *3 GB* of storage.

        ```python
        import pulumi
        import pulumi_aws as aws

        s3 = aws.budgets.Budget("s3",
            budget_type="USAGE",
            limit_amount="3",
            limit_unit="GB")
        ```

        Create a Savings Plan Utilization Budget

        ```python
        import pulumi
        import pulumi_aws as aws

        savings_plan_utilization = aws.budgets.Budget("savingsPlanUtilization",
            budget_type="SAVINGS_PLANS_UTILIZATION",
            cost_types=aws.budgets.BudgetCostTypesArgs(
                include_credit=False,
                include_discount=False,
                include_other_subscription=False,
                include_recurring=False,
                include_refund=False,
                include_subscription=True,
                include_support=False,
                include_tax=False,
                include_upfront=False,
                use_blended=False,
            ),
            limit_amount="100.0",
            limit_unit="PERCENTAGE")
        ```

        Create a RI Utilization Budget

        ```python
        import pulumi
        import pulumi_aws as aws

        ri_utilization = aws.budgets.Budget("riUtilization",
            budget_type="RI_UTILIZATION",
            cost_filters={
                "Service": "Amazon Relational Database Service",
            },
            cost_types=aws.budgets.BudgetCostTypesArgs(
                include_credit=False,
                include_discount=False,
                include_other_subscription=False,
                include_recurring=False,
                include_refund=False,
                include_subscription=True,
                include_support=False,
                include_tax=False,
                include_upfront=False,
                use_blended=False,
            ),
            limit_amount="100.0",
            limit_unit="PERCENTAGE")
        ```

        ## Import

        Budgets can be imported using `AccountID:BudgetName`, e.g.

        ```sh
         $ pulumi import aws:budgets/budget:Budget myBudget 123456789012:myBudget`
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The ID of the target account for budget. Will use current user's account_id by default if omitted.
        :param pulumi.Input[str] budget_type: Whether this budget tracks monetary cost or usage.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] cost_filters: Map of CostFilters key/value pairs to apply to the budget.
        :param pulumi.Input[pulumi.InputType['BudgetCostTypesArgs']] cost_types: Object containing CostTypes The types of cost included in a budget, such as tax and subscriptions..
        :param pulumi.Input[str] limit_amount: The amount of cost or usage being measured for a budget.
        :param pulumi.Input[str] limit_unit: The unit of measurement used for the budget forecast, actual spend, or budget threshold, such as dollars or GB. See [Spend](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/data-type-spend.html) documentation.
        :param pulumi.Input[str] name: The name of a budget. Unique within accounts.
        :param pulumi.Input[str] name_prefix: The prefix of the name of a budget. Unique within accounts.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BudgetNotificationArgs']]]] notifications: Object containing Budget Notifications. Can be used multiple times to define more than one budget notification
        :param pulumi.Input[str] time_period_end: The end of the time period covered by the budget. There are no restrictions on the end date. Format: `2017-01-01_12:00`.
        :param pulumi.Input[str] time_period_start: The start of the time period covered by the budget. The start date must come before the end date. Format: `2017-01-01_12:00`.
        :param pulumi.Input[str] time_unit: The length of time until a budget resets the actual and forecasted spend. Valid values: `MONTHLY`, `QUARTERLY`, `ANNUALLY`.
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

            __props__['account_id'] = account_id
            if budget_type is None and not opts.urn:
                raise TypeError("Missing required property 'budget_type'")
            __props__['budget_type'] = budget_type
            __props__['cost_filters'] = cost_filters
            __props__['cost_types'] = cost_types
            if limit_amount is None and not opts.urn:
                raise TypeError("Missing required property 'limit_amount'")
            __props__['limit_amount'] = limit_amount
            if limit_unit is None and not opts.urn:
                raise TypeError("Missing required property 'limit_unit'")
            __props__['limit_unit'] = limit_unit
            __props__['name'] = name
            __props__['name_prefix'] = name_prefix
            __props__['notifications'] = notifications
            __props__['time_period_end'] = time_period_end
            if time_period_start is None and not opts.urn:
                raise TypeError("Missing required property 'time_period_start'")
            __props__['time_period_start'] = time_period_start
            if time_unit is None and not opts.urn:
                raise TypeError("Missing required property 'time_unit'")
            __props__['time_unit'] = time_unit
        super(Budget, __self__).__init__(
            'aws:budgets/budget:Budget',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            budget_type: Optional[pulumi.Input[str]] = None,
            cost_filters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            cost_types: Optional[pulumi.Input[pulumi.InputType['BudgetCostTypesArgs']]] = None,
            limit_amount: Optional[pulumi.Input[str]] = None,
            limit_unit: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            name_prefix: Optional[pulumi.Input[str]] = None,
            notifications: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BudgetNotificationArgs']]]]] = None,
            time_period_end: Optional[pulumi.Input[str]] = None,
            time_period_start: Optional[pulumi.Input[str]] = None,
            time_unit: Optional[pulumi.Input[str]] = None) -> 'Budget':
        """
        Get an existing Budget resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The ID of the target account for budget. Will use current user's account_id by default if omitted.
        :param pulumi.Input[str] budget_type: Whether this budget tracks monetary cost or usage.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] cost_filters: Map of CostFilters key/value pairs to apply to the budget.
        :param pulumi.Input[pulumi.InputType['BudgetCostTypesArgs']] cost_types: Object containing CostTypes The types of cost included in a budget, such as tax and subscriptions..
        :param pulumi.Input[str] limit_amount: The amount of cost or usage being measured for a budget.
        :param pulumi.Input[str] limit_unit: The unit of measurement used for the budget forecast, actual spend, or budget threshold, such as dollars or GB. See [Spend](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/data-type-spend.html) documentation.
        :param pulumi.Input[str] name: The name of a budget. Unique within accounts.
        :param pulumi.Input[str] name_prefix: The prefix of the name of a budget. Unique within accounts.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BudgetNotificationArgs']]]] notifications: Object containing Budget Notifications. Can be used multiple times to define more than one budget notification
        :param pulumi.Input[str] time_period_end: The end of the time period covered by the budget. There are no restrictions on the end date. Format: `2017-01-01_12:00`.
        :param pulumi.Input[str] time_period_start: The start of the time period covered by the budget. The start date must come before the end date. Format: `2017-01-01_12:00`.
        :param pulumi.Input[str] time_unit: The length of time until a budget resets the actual and forecasted spend. Valid values: `MONTHLY`, `QUARTERLY`, `ANNUALLY`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["account_id"] = account_id
        __props__["budget_type"] = budget_type
        __props__["cost_filters"] = cost_filters
        __props__["cost_types"] = cost_types
        __props__["limit_amount"] = limit_amount
        __props__["limit_unit"] = limit_unit
        __props__["name"] = name
        __props__["name_prefix"] = name_prefix
        __props__["notifications"] = notifications
        __props__["time_period_end"] = time_period_end
        __props__["time_period_start"] = time_period_start
        __props__["time_unit"] = time_unit
        return Budget(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        The ID of the target account for budget. Will use current user's account_id by default if omitted.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="budgetType")
    def budget_type(self) -> pulumi.Output[str]:
        """
        Whether this budget tracks monetary cost or usage.
        """
        return pulumi.get(self, "budget_type")

    @property
    @pulumi.getter(name="costFilters")
    def cost_filters(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Map of CostFilters key/value pairs to apply to the budget.
        """
        return pulumi.get(self, "cost_filters")

    @property
    @pulumi.getter(name="costTypes")
    def cost_types(self) -> pulumi.Output['outputs.BudgetCostTypes']:
        """
        Object containing CostTypes The types of cost included in a budget, such as tax and subscriptions..
        """
        return pulumi.get(self, "cost_types")

    @property
    @pulumi.getter(name="limitAmount")
    def limit_amount(self) -> pulumi.Output[str]:
        """
        The amount of cost or usage being measured for a budget.
        """
        return pulumi.get(self, "limit_amount")

    @property
    @pulumi.getter(name="limitUnit")
    def limit_unit(self) -> pulumi.Output[str]:
        """
        The unit of measurement used for the budget forecast, actual spend, or budget threshold, such as dollars or GB. See [Spend](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/data-type-spend.html) documentation.
        """
        return pulumi.get(self, "limit_unit")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of a budget. Unique within accounts.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[str]:
        """
        The prefix of the name of a budget. Unique within accounts.
        """
        return pulumi.get(self, "name_prefix")

    @property
    @pulumi.getter
    def notifications(self) -> pulumi.Output[Optional[Sequence['outputs.BudgetNotification']]]:
        """
        Object containing Budget Notifications. Can be used multiple times to define more than one budget notification
        """
        return pulumi.get(self, "notifications")

    @property
    @pulumi.getter(name="timePeriodEnd")
    def time_period_end(self) -> pulumi.Output[Optional[str]]:
        """
        The end of the time period covered by the budget. There are no restrictions on the end date. Format: `2017-01-01_12:00`.
        """
        return pulumi.get(self, "time_period_end")

    @property
    @pulumi.getter(name="timePeriodStart")
    def time_period_start(self) -> pulumi.Output[str]:
        """
        The start of the time period covered by the budget. The start date must come before the end date. Format: `2017-01-01_12:00`.
        """
        return pulumi.get(self, "time_period_start")

    @property
    @pulumi.getter(name="timeUnit")
    def time_unit(self) -> pulumi.Output[str]:
        """
        The length of time until a budget resets the actual and forecasted spend. Valid values: `MONTHLY`, `QUARTERLY`, `ANNUALLY`.
        """
        return pulumi.get(self, "time_unit")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

