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
    'ListAccountSasTokensResult',
    'AwaitableListAccountSasTokensResult',
    'list_account_sas_tokens',
]

@pulumi.output_type
class ListAccountSasTokensResult:
    """
    The SAS response that contains the storage account, container and associated SAS token for connection use.
    """
    def __init__(__self__, next_link=None, value=None):
        if next_link and not isinstance(next_link, str):
            raise TypeError("Expected argument 'next_link' to be a str")
        pulumi.set(__self__, "next_link", next_link)
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> str:
        """
        the link (url) to the next page of results.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Sequence['outputs.SasTokenInfoResponseResult']:
        return pulumi.get(self, "value")


class AwaitableListAccountSasTokensResult(ListAccountSasTokensResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListAccountSasTokensResult(
            next_link=self.next_link,
            value=self.value)


def list_account_sas_tokens(account_name: Optional[str] = None,
                            container_name: Optional[str] = None,
                            resource_group_name: Optional[str] = None,
                            storage_account_name: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListAccountSasTokensResult:
    """
    Use this data source to access information about an existing resource.

    :param str account_name: The name of the Data Lake Analytics account from which an Azure Storage account's SAS token is being requested.
    :param str container_name: The name of the Azure storage container for which the SAS token is being requested.
    :param str resource_group_name: The name of the Azure resource group that contains the Data Lake Analytics account.
    :param str storage_account_name: The name of the Azure storage account for which the SAS token is being requested.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['containerName'] = container_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['storageAccountName'] = storage_account_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-nextgen:datalakeanalytics/v20151001preview:listAccountSasTokens', __args__, opts=opts, typ=ListAccountSasTokensResult).value

    return AwaitableListAccountSasTokensResult(
        next_link=__ret__.next_link,
        value=__ret__.value)
