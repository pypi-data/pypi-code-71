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
    'GetServerDetailsResult',
    'AwaitableGetServerDetailsResult',
    'get_server_details',
]

@pulumi.output_type
class GetServerDetailsResult:
    """
    Represents an instance of an Analysis Services resource.
    """
    def __init__(__self__, as_administrators=None, backup_blob_container_uri=None, id=None, location=None, name=None, provisioning_state=None, server_full_name=None, sku=None, state=None, tags=None, type=None):
        if as_administrators and not isinstance(as_administrators, dict):
            raise TypeError("Expected argument 'as_administrators' to be a dict")
        pulumi.set(__self__, "as_administrators", as_administrators)
        if backup_blob_container_uri and not isinstance(backup_blob_container_uri, str):
            raise TypeError("Expected argument 'backup_blob_container_uri' to be a str")
        pulumi.set(__self__, "backup_blob_container_uri", backup_blob_container_uri)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if server_full_name and not isinstance(server_full_name, str):
            raise TypeError("Expected argument 'server_full_name' to be a str")
        pulumi.set(__self__, "server_full_name", server_full_name)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="asAdministrators")
    def as_administrators(self) -> Optional['outputs.ServerAdministratorsResponse']:
        """
        A collection of AS server administrators
        """
        return pulumi.get(self, "as_administrators")

    @property
    @pulumi.getter(name="backupBlobContainerUri")
    def backup_blob_container_uri(self) -> Optional[str]:
        """
        The container URI of backup blob.
        """
        return pulumi.get(self, "backup_blob_container_uri")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        An identifier that represents the Analysis Services resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Location of the Analysis Services resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the Analysis Services resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The current deployment state of Analysis Services resource. The provisioningState is to indicate states for resource provisioning.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="serverFullName")
    def server_full_name(self) -> str:
        """
        The full name of the Analysis Services resource.
        """
        return pulumi.get(self, "server_full_name")

    @property
    @pulumi.getter
    def sku(self) -> 'outputs.ResourceSkuResponse':
        """
        The SKU of the Analysis Services resource.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of Analysis Services resource. The state is to indicate more states outside of resource provisioning.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Key-value pairs of additional resource provisioning properties.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the Analysis Services resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetServerDetailsResult(GetServerDetailsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServerDetailsResult(
            as_administrators=self.as_administrators,
            backup_blob_container_uri=self.backup_blob_container_uri,
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            server_full_name=self.server_full_name,
            sku=self.sku,
            state=self.state,
            tags=self.tags,
            type=self.type)


def get_server_details(resource_group_name: Optional[str] = None,
                       server_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServerDetailsResult:
    """
    Use this data source to access information about an existing resource.

    :param str resource_group_name: The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
    :param str server_name: The name of the Analysis Services server. It must be a minimum of 3 characters, and a maximum of 63.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverName'] = server_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-nextgen:analysisservices/v20160516:getServerDetails', __args__, opts=opts, typ=GetServerDetailsResult).value

    return AwaitableGetServerDetailsResult(
        as_administrators=__ret__.as_administrators,
        backup_blob_container_uri=__ret__.backup_blob_container_uri,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        server_full_name=__ret__.server_full_name,
        sku=__ret__.sku,
        state=__ret__.state,
        tags=__ret__.tags,
        type=__ret__.type)
