# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables

__all__ = [
    'ListWebAppFunctionSecretsSlotResult',
    'AwaitableListWebAppFunctionSecretsSlotResult',
    'list_web_app_function_secrets_slot',
]

@pulumi.output_type
class ListWebAppFunctionSecretsSlotResult:
    """
    Function secrets.
    """
    def __init__(__self__, key=None, trigger_url=None):
        if key and not isinstance(key, str):
            raise TypeError("Expected argument 'key' to be a str")
        pulumi.set(__self__, "key", key)
        if trigger_url and not isinstance(trigger_url, str):
            raise TypeError("Expected argument 'trigger_url' to be a str")
        pulumi.set(__self__, "trigger_url", trigger_url)

    @property
    @pulumi.getter
    def key(self) -> Optional[str]:
        """
        Secret key.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter(name="triggerUrl")
    def trigger_url(self) -> Optional[str]:
        """
        Trigger URL.
        """
        return pulumi.get(self, "trigger_url")


class AwaitableListWebAppFunctionSecretsSlotResult(ListWebAppFunctionSecretsSlotResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListWebAppFunctionSecretsSlotResult(
            key=self.key,
            trigger_url=self.trigger_url)


def list_web_app_function_secrets_slot(function_name: Optional[str] = None,
                                       name: Optional[str] = None,
                                       resource_group_name: Optional[str] = None,
                                       slot: Optional[str] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListWebAppFunctionSecretsSlotResult:
    """
    Use this data source to access information about an existing resource.

    :param str function_name: Function name.
    :param str name: Site name.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    :param str slot: Name of the deployment slot.
    """
    __args__ = dict()
    __args__['functionName'] = function_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    __args__['slot'] = slot
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-nextgen:web/v20200601:listWebAppFunctionSecretsSlot', __args__, opts=opts, typ=ListWebAppFunctionSecretsSlotResult).value

    return AwaitableListWebAppFunctionSecretsSlotResult(
        key=__ret__.key,
        trigger_url=__ret__.trigger_url)
