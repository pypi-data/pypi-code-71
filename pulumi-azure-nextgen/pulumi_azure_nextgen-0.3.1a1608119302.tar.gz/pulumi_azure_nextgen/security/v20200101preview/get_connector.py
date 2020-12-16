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
    'GetConnectorResult',
    'AwaitableGetConnectorResult',
    'get_connector',
]

@pulumi.output_type
class GetConnectorResult:
    """
    The connector setting
    """
    def __init__(__self__, authentication_details=None, hybrid_compute_settings=None, id=None, name=None, type=None):
        if authentication_details and not isinstance(authentication_details, dict):
            raise TypeError("Expected argument 'authentication_details' to be a dict")
        pulumi.set(__self__, "authentication_details", authentication_details)
        if hybrid_compute_settings and not isinstance(hybrid_compute_settings, dict):
            raise TypeError("Expected argument 'hybrid_compute_settings' to be a dict")
        pulumi.set(__self__, "hybrid_compute_settings", hybrid_compute_settings)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="authenticationDetails")
    def authentication_details(self) -> Optional[Any]:
        """
        Settings for authentication management, these settings are relevant only for the cloud connector.
        """
        return pulumi.get(self, "authentication_details")

    @property
    @pulumi.getter(name="hybridComputeSettings")
    def hybrid_compute_settings(self) -> Optional['outputs.HybridComputeSettingsPropertiesResponse']:
        """
        Settings for hybrid compute management. These settings are relevant only for Arc autoProvision (Hybrid Compute).
        """
        return pulumi.get(self, "hybrid_compute_settings")

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
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetConnectorResult(GetConnectorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConnectorResult(
            authentication_details=self.authentication_details,
            hybrid_compute_settings=self.hybrid_compute_settings,
            id=self.id,
            name=self.name,
            type=self.type)


def get_connector(connector_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConnectorResult:
    """
    Use this data source to access information about an existing resource.

    :param str connector_name: Name of the cloud account connector
    """
    __args__ = dict()
    __args__['connectorName'] = connector_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-nextgen:security/v20200101preview:getConnector', __args__, opts=opts, typ=GetConnectorResult).value

    return AwaitableGetConnectorResult(
        authentication_details=__ret__.authentication_details,
        hybrid_compute_settings=__ret__.hybrid_compute_settings,
        id=__ret__.id,
        name=__ret__.name,
        type=__ret__.type)
