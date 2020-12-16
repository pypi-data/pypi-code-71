# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AzureSkuName',
    'AzureSkuTier',
    'Kind',
]


class AzureSkuName(str, Enum):
    """
    SKU name.
    """
    STANDARD_DS13_V2_1_T_B_PS = "Standard_DS13_v2+1TB_PS"
    STANDARD_DS13_V2_2_T_B_PS = "Standard_DS13_v2+2TB_PS"
    STANDARD_DS14_V2_3_T_B_PS = "Standard_DS14_v2+3TB_PS"
    STANDARD_DS14_V2_4_T_B_PS = "Standard_DS14_v2+4TB_PS"
    STANDARD_D13_V2 = "Standard_D13_v2"
    STANDARD_D14_V2 = "Standard_D14_v2"
    STANDARD_L8S = "Standard_L8s"
    STANDARD_L16S = "Standard_L16s"
    STANDARD_D11_V2 = "Standard_D11_v2"
    STANDARD_D12_V2 = "Standard_D12_v2"
    STANDARD_L4S = "Standard_L4s"
    DEV_NO_SL_A_STANDARD_D11_V2 = "Dev(No SLA)_Standard_D11_v2"


class AzureSkuTier(str, Enum):
    """
    SKU tier.
    """
    BASIC = "Basic"
    STANDARD = "Standard"


class Kind(str, Enum):
    """
    Kind of the endpoint for the data connection
    """
    EVENT_HUB = "EventHub"
    EVENT_GRID = "EventGrid"
    IOT_HUB = "IotHub"
