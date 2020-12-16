# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables

__all__ = [
    'ListIdentityProviderSecretsResult',
    'AwaitableListIdentityProviderSecretsResult',
    'list_identity_provider_secrets',
]

@pulumi.output_type
class ListIdentityProviderSecretsResult:
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


class AwaitableListIdentityProviderSecretsResult(ListIdentityProviderSecretsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListIdentityProviderSecretsResult(
            client_secret=self.client_secret)


def list_identity_provider_secrets(identity_provider_name: Optional[str] = None,
                                   resource_group_name: Optional[str] = None,
                                   service_name: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListIdentityProviderSecretsResult:
    """
    Use this data source to access information about an existing resource.

    :param str identity_provider_name: Identity Provider Type identifier.
    :param str resource_group_name: The name of the resource group.
    :param str service_name: The name of the API Management service.
    """
    __args__ = dict()
    __args__['identityProviderName'] = identity_provider_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-nextgen:apimanagement/v20200601preview:listIdentityProviderSecrets', __args__, opts=opts, typ=ListIdentityProviderSecretsResult).value

    return AwaitableListIdentityProviderSecretsResult(
        client_secret=__ret__.client_secret)
