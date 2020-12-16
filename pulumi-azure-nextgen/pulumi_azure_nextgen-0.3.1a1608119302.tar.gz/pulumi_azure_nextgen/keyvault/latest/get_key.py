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
    'GetKeyResult',
    'AwaitableGetKeyResult',
    'get_key',
]

@pulumi.output_type
class GetKeyResult:
    """
    The key resource.
    """
    def __init__(__self__, attributes=None, curve_name=None, id=None, key_ops=None, key_size=None, key_uri=None, key_uri_with_version=None, kty=None, location=None, name=None, tags=None, type=None):
        if attributes and not isinstance(attributes, dict):
            raise TypeError("Expected argument 'attributes' to be a dict")
        pulumi.set(__self__, "attributes", attributes)
        if curve_name and not isinstance(curve_name, str):
            raise TypeError("Expected argument 'curve_name' to be a str")
        pulumi.set(__self__, "curve_name", curve_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if key_ops and not isinstance(key_ops, list):
            raise TypeError("Expected argument 'key_ops' to be a list")
        pulumi.set(__self__, "key_ops", key_ops)
        if key_size and not isinstance(key_size, int):
            raise TypeError("Expected argument 'key_size' to be a int")
        pulumi.set(__self__, "key_size", key_size)
        if key_uri and not isinstance(key_uri, str):
            raise TypeError("Expected argument 'key_uri' to be a str")
        pulumi.set(__self__, "key_uri", key_uri)
        if key_uri_with_version and not isinstance(key_uri_with_version, str):
            raise TypeError("Expected argument 'key_uri_with_version' to be a str")
        pulumi.set(__self__, "key_uri_with_version", key_uri_with_version)
        if kty and not isinstance(kty, str):
            raise TypeError("Expected argument 'kty' to be a str")
        pulumi.set(__self__, "kty", kty)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def attributes(self) -> Optional['outputs.KeyAttributesResponse']:
        """
        The attributes of the key.
        """
        return pulumi.get(self, "attributes")

    @property
    @pulumi.getter(name="curveName")
    def curve_name(self) -> Optional[str]:
        """
        The elliptic curve name. For valid values, see JsonWebKeyCurveName.
        """
        return pulumi.get(self, "curve_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified identifier of the key vault resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="keyOps")
    def key_ops(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "key_ops")

    @property
    @pulumi.getter(name="keySize")
    def key_size(self) -> Optional[int]:
        """
        The key size in bits. For example: 2048, 3072, or 4096 for RSA.
        """
        return pulumi.get(self, "key_size")

    @property
    @pulumi.getter(name="keyUri")
    def key_uri(self) -> str:
        """
        The URI to retrieve the current version of the key.
        """
        return pulumi.get(self, "key_uri")

    @property
    @pulumi.getter(name="keyUriWithVersion")
    def key_uri_with_version(self) -> str:
        """
        The URI to retrieve the specific version of the key.
        """
        return pulumi.get(self, "key_uri_with_version")

    @property
    @pulumi.getter
    def kty(self) -> Optional[str]:
        """
        The type of the key. For valid values, see JsonWebKeyType.
        """
        return pulumi.get(self, "kty")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Azure location of the key vault resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the key vault resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        Tags assigned to the key vault resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type of the key vault resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetKeyResult(GetKeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKeyResult(
            attributes=self.attributes,
            curve_name=self.curve_name,
            id=self.id,
            key_ops=self.key_ops,
            key_size=self.key_size,
            key_uri=self.key_uri,
            key_uri_with_version=self.key_uri_with_version,
            kty=self.kty,
            location=self.location,
            name=self.name,
            tags=self.tags,
            type=self.type)


def get_key(key_name: Optional[str] = None,
            resource_group_name: Optional[str] = None,
            vault_name: Optional[str] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKeyResult:
    """
    Use this data source to access information about an existing resource.

    :param str key_name: The name of the key to be retrieved.
    :param str resource_group_name: The name of the resource group which contains the specified key vault.
    :param str vault_name: The name of the vault which contains the key to be retrieved.
    """
    __args__ = dict()
    __args__['keyName'] = key_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['vaultName'] = vault_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-nextgen:keyvault/latest:getKey', __args__, opts=opts, typ=GetKeyResult).value

    return AwaitableGetKeyResult(
        attributes=__ret__.attributes,
        curve_name=__ret__.curve_name,
        id=__ret__.id,
        key_ops=__ret__.key_ops,
        key_size=__ret__.key_size,
        key_uri=__ret__.key_uri,
        key_uri_with_version=__ret__.key_uri_with_version,
        kty=__ret__.kty,
        location=__ret__.location,
        name=__ret__.name,
        tags=__ret__.tags,
        type=__ret__.type)
