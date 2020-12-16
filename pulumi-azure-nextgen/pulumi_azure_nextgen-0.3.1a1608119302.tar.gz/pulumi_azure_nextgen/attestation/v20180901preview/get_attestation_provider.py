# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables

__all__ = [
    'GetAttestationProviderResult',
    'AwaitableGetAttestationProviderResult',
    'get_attestation_provider',
]

@pulumi.output_type
class GetAttestationProviderResult:
    """
    Attestation service response message.
    """
    def __init__(__self__, attest_uri=None, id=None, location=None, name=None, status=None, tags=None, trust_model=None, type=None):
        if attest_uri and not isinstance(attest_uri, str):
            raise TypeError("Expected argument 'attest_uri' to be a str")
        pulumi.set(__self__, "attest_uri", attest_uri)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if trust_model and not isinstance(trust_model, str):
            raise TypeError("Expected argument 'trust_model' to be a str")
        pulumi.set(__self__, "trust_model", trust_model)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="attestUri")
    def attest_uri(self) -> Optional[str]:
        """
        Gets the uri of attestation service
        """
        return pulumi.get(self, "attest_uri")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        Status of attestation service.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="trustModel")
    def trust_model(self) -> Optional[str]:
        """
        Trust model for the attestation service instance.
        """
        return pulumi.get(self, "trust_model")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetAttestationProviderResult(GetAttestationProviderResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAttestationProviderResult(
            attest_uri=self.attest_uri,
            id=self.id,
            location=self.location,
            name=self.name,
            status=self.status,
            tags=self.tags,
            trust_model=self.trust_model,
            type=self.type)


def get_attestation_provider(provider_name: Optional[str] = None,
                             resource_group_name: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAttestationProviderResult:
    """
    Use this data source to access information about an existing resource.

    :param str provider_name: Name of the attestation service instance
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['providerName'] = provider_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-nextgen:attestation/v20180901preview:getAttestationProvider', __args__, opts=opts, typ=GetAttestationProviderResult).value

    return AwaitableGetAttestationProviderResult(
        attest_uri=__ret__.attest_uri,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        status=__ret__.status,
        tags=__ret__.tags,
        trust_model=__ret__.trust_model,
        type=__ret__.type)
