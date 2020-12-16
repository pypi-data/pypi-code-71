# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables

__all__ = [
    'GetVirtualNetworkGatewayVpnclientIpsecParametersResult',
    'AwaitableGetVirtualNetworkGatewayVpnclientIpsecParametersResult',
    'get_virtual_network_gateway_vpnclient_ipsec_parameters',
]

@pulumi.output_type
class GetVirtualNetworkGatewayVpnclientIpsecParametersResult:
    """
    An IPSec parameters for a virtual network gateway P2S connection.
    """
    def __init__(__self__, dh_group=None, ike_encryption=None, ike_integrity=None, ipsec_encryption=None, ipsec_integrity=None, pfs_group=None, sa_data_size_kilobytes=None, sa_life_time_seconds=None):
        if dh_group and not isinstance(dh_group, str):
            raise TypeError("Expected argument 'dh_group' to be a str")
        pulumi.set(__self__, "dh_group", dh_group)
        if ike_encryption and not isinstance(ike_encryption, str):
            raise TypeError("Expected argument 'ike_encryption' to be a str")
        pulumi.set(__self__, "ike_encryption", ike_encryption)
        if ike_integrity and not isinstance(ike_integrity, str):
            raise TypeError("Expected argument 'ike_integrity' to be a str")
        pulumi.set(__self__, "ike_integrity", ike_integrity)
        if ipsec_encryption and not isinstance(ipsec_encryption, str):
            raise TypeError("Expected argument 'ipsec_encryption' to be a str")
        pulumi.set(__self__, "ipsec_encryption", ipsec_encryption)
        if ipsec_integrity and not isinstance(ipsec_integrity, str):
            raise TypeError("Expected argument 'ipsec_integrity' to be a str")
        pulumi.set(__self__, "ipsec_integrity", ipsec_integrity)
        if pfs_group and not isinstance(pfs_group, str):
            raise TypeError("Expected argument 'pfs_group' to be a str")
        pulumi.set(__self__, "pfs_group", pfs_group)
        if sa_data_size_kilobytes and not isinstance(sa_data_size_kilobytes, int):
            raise TypeError("Expected argument 'sa_data_size_kilobytes' to be a int")
        pulumi.set(__self__, "sa_data_size_kilobytes", sa_data_size_kilobytes)
        if sa_life_time_seconds and not isinstance(sa_life_time_seconds, int):
            raise TypeError("Expected argument 'sa_life_time_seconds' to be a int")
        pulumi.set(__self__, "sa_life_time_seconds", sa_life_time_seconds)

    @property
    @pulumi.getter(name="dhGroup")
    def dh_group(self) -> str:
        """
        The DH Groups used in IKE Phase 1 for initial SA.
        """
        return pulumi.get(self, "dh_group")

    @property
    @pulumi.getter(name="ikeEncryption")
    def ike_encryption(self) -> str:
        """
        The IKE encryption algorithm (IKE phase 2).
        """
        return pulumi.get(self, "ike_encryption")

    @property
    @pulumi.getter(name="ikeIntegrity")
    def ike_integrity(self) -> str:
        """
        The IKE integrity algorithm (IKE phase 2).
        """
        return pulumi.get(self, "ike_integrity")

    @property
    @pulumi.getter(name="ipsecEncryption")
    def ipsec_encryption(self) -> str:
        """
        The IPSec encryption algorithm (IKE phase 1).
        """
        return pulumi.get(self, "ipsec_encryption")

    @property
    @pulumi.getter(name="ipsecIntegrity")
    def ipsec_integrity(self) -> str:
        """
        The IPSec integrity algorithm (IKE phase 1).
        """
        return pulumi.get(self, "ipsec_integrity")

    @property
    @pulumi.getter(name="pfsGroup")
    def pfs_group(self) -> str:
        """
        The Pfs Groups used in IKE Phase 2 for new child SA.
        """
        return pulumi.get(self, "pfs_group")

    @property
    @pulumi.getter(name="saDataSizeKilobytes")
    def sa_data_size_kilobytes(self) -> int:
        """
        The IPSec Security Association (also called Quick Mode or Phase 2 SA) payload size in KB for P2S client..
        """
        return pulumi.get(self, "sa_data_size_kilobytes")

    @property
    @pulumi.getter(name="saLifeTimeSeconds")
    def sa_life_time_seconds(self) -> int:
        """
        The IPSec Security Association (also called Quick Mode or Phase 2 SA) lifetime in seconds for P2S client.
        """
        return pulumi.get(self, "sa_life_time_seconds")


class AwaitableGetVirtualNetworkGatewayVpnclientIpsecParametersResult(GetVirtualNetworkGatewayVpnclientIpsecParametersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualNetworkGatewayVpnclientIpsecParametersResult(
            dh_group=self.dh_group,
            ike_encryption=self.ike_encryption,
            ike_integrity=self.ike_integrity,
            ipsec_encryption=self.ipsec_encryption,
            ipsec_integrity=self.ipsec_integrity,
            pfs_group=self.pfs_group,
            sa_data_size_kilobytes=self.sa_data_size_kilobytes,
            sa_life_time_seconds=self.sa_life_time_seconds)


def get_virtual_network_gateway_vpnclient_ipsec_parameters(resource_group_name: Optional[str] = None,
                                                           virtual_network_gateway_name: Optional[str] = None,
                                                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualNetworkGatewayVpnclientIpsecParametersResult:
    """
    Use this data source to access information about an existing resource.

    :param str resource_group_name: The name of the resource group.
    :param str virtual_network_gateway_name: The virtual network gateway name.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['virtualNetworkGatewayName'] = virtual_network_gateway_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-nextgen:network/v20180801:getVirtualNetworkGatewayVpnclientIpsecParameters', __args__, opts=opts, typ=GetVirtualNetworkGatewayVpnclientIpsecParametersResult).value

    return AwaitableGetVirtualNetworkGatewayVpnclientIpsecParametersResult(
        dh_group=__ret__.dh_group,
        ike_encryption=__ret__.ike_encryption,
        ike_integrity=__ret__.ike_integrity,
        ipsec_encryption=__ret__.ipsec_encryption,
        ipsec_integrity=__ret__.ipsec_integrity,
        pfs_group=__ret__.pfs_group,
        sa_data_size_kilobytes=__ret__.sa_data_size_kilobytes,
        sa_life_time_seconds=__ret__.sa_life_time_seconds)
