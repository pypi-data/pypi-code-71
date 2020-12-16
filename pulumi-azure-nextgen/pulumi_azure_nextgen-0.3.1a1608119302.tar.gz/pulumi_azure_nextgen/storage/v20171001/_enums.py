# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AccessTier',
    'Action',
    'Bypass',
    'DefaultAction',
    'IdentityType',
    'KeySource',
    'Kind',
    'ReasonCode',
    'SkuName',
    'State',
]


class AccessTier(str, Enum):
    """
    Required for storage accounts where kind = BlobStorage. The access tier used for billing.
    """
    HOT = "Hot"
    COOL = "Cool"


class Action(str, Enum):
    """
    The action of virtual network rule.
    """
    ALLOW = "Allow"


class Bypass(str, Enum):
    """
    Specifies whether traffic is bypassed for Logging/Metrics/AzureServices. Possible values are any combination of Logging|Metrics|AzureServices (For example, "Logging, Metrics"), or None to bypass none of those traffics.
    """
    NONE = "None"
    LOGGING = "Logging"
    METRICS = "Metrics"
    AZURE_SERVICES = "AzureServices"


class DefaultAction(str, Enum):
    """
    Specifies the default action of allow or deny when no other rules match.
    """
    ALLOW = "Allow"
    DENY = "Deny"


class IdentityType(str, Enum):
    """
    The identity type.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"


class KeySource(str, Enum):
    """
    The encryption keySource (provider). Possible values (case-insensitive):  Microsoft.Storage, Microsoft.Keyvault
    """
    MICROSOFT_STORAGE = "Microsoft.Storage"
    MICROSOFT_KEYVAULT = "Microsoft.Keyvault"


class Kind(str, Enum):
    """
    Required. Indicates the type of storage account.
    """
    STORAGE = "Storage"
    STORAGE_V2 = "StorageV2"
    BLOB_STORAGE = "BlobStorage"


class ReasonCode(str, Enum):
    """
    The reason for the restriction. As of now this can be "QuotaId" or "NotAvailableForSubscription". Quota Id is set when the SKU has requiredQuotas parameter as the subscription does not belong to that quota. The "NotAvailableForSubscription" is related to capacity at DC.
    """
    QUOTA_ID = "QuotaId"
    NOT_AVAILABLE_FOR_SUBSCRIPTION = "NotAvailableForSubscription"


class SkuName(str, Enum):
    """
    Gets or sets the sku name. Required for account creation; optional for update. Note that in older versions, sku name was called accountType.
    """
    STANDARD_LRS = "Standard_LRS"
    STANDARD_GRS = "Standard_GRS"
    STANDARD_RAGRS = "Standard_RAGRS"
    STANDARD_ZRS = "Standard_ZRS"
    PREMIUM_LRS = "Premium_LRS"


class State(str, Enum):
    """
    Gets the state of virtual network rule.
    """
    PROVISIONING = "provisioning"
    DEPROVISIONING = "deprovisioning"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    NETWORK_SOURCE_DELETED = "networkSourceDeleted"
