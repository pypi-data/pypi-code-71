# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables
from . import outputs

__all__ = [
    'GetRuleResult',
    'AwaitableGetRuleResult',
    'get_rule',
]

@pulumi.output_type
class GetRuleResult:
    """
    Description of Rule Resource.
    """
    def __init__(__self__, action=None, correlation_filter=None, filter_type=None, id=None, name=None, sql_filter=None, type=None):
        if action and not isinstance(action, dict):
            raise TypeError("Expected argument 'action' to be a dict")
        pulumi.set(__self__, "action", action)
        if correlation_filter and not isinstance(correlation_filter, dict):
            raise TypeError("Expected argument 'correlation_filter' to be a dict")
        pulumi.set(__self__, "correlation_filter", correlation_filter)
        if filter_type and not isinstance(filter_type, str):
            raise TypeError("Expected argument 'filter_type' to be a str")
        pulumi.set(__self__, "filter_type", filter_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if sql_filter and not isinstance(sql_filter, dict):
            raise TypeError("Expected argument 'sql_filter' to be a dict")
        pulumi.set(__self__, "sql_filter", sql_filter)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def action(self) -> Optional['outputs.ActionResponse']:
        """
        Represents the filter actions which are allowed for the transformation of a message that have been matched by a filter expression.
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter(name="correlationFilter")
    def correlation_filter(self) -> Optional['outputs.CorrelationFilterResponse']:
        """
        Properties of correlationFilter
        """
        return pulumi.get(self, "correlation_filter")

    @property
    @pulumi.getter(name="filterType")
    def filter_type(self) -> Optional[str]:
        """
        Filter type that is evaluated against a BrokeredMessage.
        """
        return pulumi.get(self, "filter_type")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="sqlFilter")
    def sql_filter(self) -> Optional['outputs.SqlFilterResponse']:
        """
        Properties of sqlFilter
        """
        return pulumi.get(self, "sql_filter")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetRuleResult(GetRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRuleResult(
            action=self.action,
            correlation_filter=self.correlation_filter,
            filter_type=self.filter_type,
            id=self.id,
            name=self.name,
            sql_filter=self.sql_filter,
            type=self.type)


def get_rule(namespace_name: Optional[str] = None,
             resource_group_name: Optional[str] = None,
             rule_name: Optional[str] = None,
             subscription_name: Optional[str] = None,
             topic_name: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRuleResult:
    """
    Use this data source to access information about an existing resource.

    :param str namespace_name: The namespace name
    :param str resource_group_name: Name of the Resource group within the Azure subscription.
    :param str rule_name: The rule name.
    :param str subscription_name: The subscription name.
    :param str topic_name: The topic name.
    """
    __args__ = dict()
    __args__['namespaceName'] = namespace_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['ruleName'] = rule_name
    __args__['subscriptionName'] = subscription_name
    __args__['topicName'] = topic_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-nextgen:servicebus/latest:getRule', __args__, opts=opts, typ=GetRuleResult).value

    return AwaitableGetRuleResult(
        action=__ret__.action,
        correlation_filter=__ret__.correlation_filter,
        filter_type=__ret__.filter_type,
        id=__ret__.id,
        name=__ret__.name,
        sql_filter=__ret__.sql_filter,
        type=__ret__.type)
