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

__all__ = [
    'ListWorkflowVersionTriggerCallbackUrlResult',
    'AwaitableListWorkflowVersionTriggerCallbackUrlResult',
    'list_workflow_version_trigger_callback_url',
]

@pulumi.output_type
class ListWorkflowVersionTriggerCallbackUrlResult:
    """
    The workflow trigger callback URL.
    """
    def __init__(__self__, base_path=None, method=None, queries=None, relative_path=None, relative_path_parameters=None, value=None):
        if base_path and not isinstance(base_path, str):
            raise TypeError("Expected argument 'base_path' to be a str")
        pulumi.set(__self__, "base_path", base_path)
        if method and not isinstance(method, str):
            raise TypeError("Expected argument 'method' to be a str")
        pulumi.set(__self__, "method", method)
        if queries and not isinstance(queries, dict):
            raise TypeError("Expected argument 'queries' to be a dict")
        pulumi.set(__self__, "queries", queries)
        if relative_path and not isinstance(relative_path, str):
            raise TypeError("Expected argument 'relative_path' to be a str")
        pulumi.set(__self__, "relative_path", relative_path)
        if relative_path_parameters and not isinstance(relative_path_parameters, list):
            raise TypeError("Expected argument 'relative_path_parameters' to be a list")
        pulumi.set(__self__, "relative_path_parameters", relative_path_parameters)
        if value and not isinstance(value, str):
            raise TypeError("Expected argument 'value' to be a str")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="basePath")
    def base_path(self) -> str:
        """
        Gets the workflow trigger callback URL base path.
        """
        return pulumi.get(self, "base_path")

    @property
    @pulumi.getter
    def method(self) -> str:
        """
        Gets the workflow trigger callback URL HTTP method.
        """
        return pulumi.get(self, "method")

    @property
    @pulumi.getter
    def queries(self) -> Optional['outputs.WorkflowTriggerListCallbackUrlQueriesResponseResult']:
        """
        Gets the workflow trigger callback URL query parameters.
        """
        return pulumi.get(self, "queries")

    @property
    @pulumi.getter(name="relativePath")
    def relative_path(self) -> str:
        """
        Gets the workflow trigger callback URL relative path.
        """
        return pulumi.get(self, "relative_path")

    @property
    @pulumi.getter(name="relativePathParameters")
    def relative_path_parameters(self) -> Optional[Sequence[str]]:
        """
        Gets the workflow trigger callback URL relative path parameters.
        """
        return pulumi.get(self, "relative_path_parameters")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        Gets the workflow trigger callback URL.
        """
        return pulumi.get(self, "value")


class AwaitableListWorkflowVersionTriggerCallbackUrlResult(ListWorkflowVersionTriggerCallbackUrlResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListWorkflowVersionTriggerCallbackUrlResult(
            base_path=self.base_path,
            method=self.method,
            queries=self.queries,
            relative_path=self.relative_path,
            relative_path_parameters=self.relative_path_parameters,
            value=self.value)


def list_workflow_version_trigger_callback_url(key_type: Optional[Union[str, 'KeyType']] = None,
                                               not_after: Optional[str] = None,
                                               resource_group_name: Optional[str] = None,
                                               trigger_name: Optional[str] = None,
                                               version_id: Optional[str] = None,
                                               workflow_name: Optional[str] = None,
                                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListWorkflowVersionTriggerCallbackUrlResult:
    """
    Use this data source to access information about an existing resource.

    :param Union[str, 'KeyType'] key_type: The key type.
    :param str not_after: The expiry time.
    :param str resource_group_name: The resource group name.
    :param str trigger_name: The workflow trigger name.
    :param str version_id: The workflow versionId.
    :param str workflow_name: The workflow name.
    """
    __args__ = dict()
    __args__['keyType'] = key_type
    __args__['notAfter'] = not_after
    __args__['resourceGroupName'] = resource_group_name
    __args__['triggerName'] = trigger_name
    __args__['versionId'] = version_id
    __args__['workflowName'] = workflow_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-nextgen:logic/v20190501:listWorkflowVersionTriggerCallbackUrl', __args__, opts=opts, typ=ListWorkflowVersionTriggerCallbackUrlResult).value

    return AwaitableListWorkflowVersionTriggerCallbackUrlResult(
        base_path=__ret__.base_path,
        method=__ret__.method,
        queries=__ret__.queries,
        relative_path=__ret__.relative_path,
        relative_path_parameters=__ret__.relative_path_parameters,
        value=__ret__.value)
