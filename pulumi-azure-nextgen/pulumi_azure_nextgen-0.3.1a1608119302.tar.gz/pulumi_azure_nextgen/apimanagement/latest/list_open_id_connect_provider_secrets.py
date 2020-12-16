# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables

__all__ = [
    'ListOpenIdConnectProviderSecretsResult',
    'AwaitableListOpenIdConnectProviderSecretsResult',
    'list_open_id_connect_provider_secrets',
]

@pulumi.output_type
class ListOpenIdConnectProviderSecretsResult:
    """
    Client or app secret used in IdentityProviders, Aad, OpenID or OAuth.
    """
    def __init__(__self__, client_secret=None):
        if client_secret and not isinstance(client_secret, str):
            raise TypeError("Expected argument 'client_secret' to be a str")
        pulumi.set(__self__, "client_secret", client_secret)

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[str]:
        """
        Client or app secret used in IdentityProviders, Aad, OpenID or OAuth.
        """
        return pulumi.get(self, "client_secret")


class AwaitableListOpenIdConnectProviderSecretsResult(ListOpenIdConnectProviderSecretsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListOpenIdConnectProviderSecretsResult(
            client_secret=self.client_secret)


def list_open_id_connect_provider_secrets(opid: Optional[str] = None,
                                          resource_group_name: Optional[str] = None,
                                          service_name: Optional[str] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListOpenIdConnectProviderSecretsResult:
    """
    Use this data source to access information about an existing resource.

    :param str opid: Identifier of the OpenID Connect Provider.
    :param str resource_group_name: The name of the resource group.
    :param str service_name: The name of the API Management service.
    """
    __args__ = dict()
    __args__['opid'] = opid
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-nextgen:apimanagement/latest:listOpenIdConnectProviderSecrets', __args__, opts=opts, typ=ListOpenIdConnectProviderSecretsResult).value

    return AwaitableListOpenIdConnectProviderSecretsResult(
        client_secret=__ret__.client_secret)
