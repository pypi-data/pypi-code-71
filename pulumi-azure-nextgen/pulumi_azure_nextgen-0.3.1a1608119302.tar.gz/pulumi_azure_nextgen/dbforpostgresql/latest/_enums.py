# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AdministratorType',
    'CreateMode',
    'GeoRedundantBackup',
    'IdentityType',
    'InfrastructureEncryption',
    'MinimalTlsVersionEnum',
    'PublicNetworkAccessEnum',
    'ServerKeyType',
    'ServerVersion',
    'SkuTier',
    'SslEnforcementEnum',
    'StorageAutogrow',
]


class AdministratorType(str, Enum):
    """
    The type of administrator.
    """
    ACTIVE_DIRECTORY = "ActiveDirectory"


class CreateMode(str, Enum):
    """
    The mode to create a new server.
    """
    DEFAULT = "Default"
    POINT_IN_TIME_RESTORE = "PointInTimeRestore"
    GEO_RESTORE = "GeoRestore"
    REPLICA = "Replica"


class GeoRedundantBackup(str, Enum):
    """
    Enable Geo-redundant or not for server backup.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class IdentityType(str, Enum):
    """
    The identity type. Set this to 'SystemAssigned' in order to automatically create and assign an Azure Active Directory principal for the resource.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"


class InfrastructureEncryption(str, Enum):
    """
    Status showing whether the server enabled infrastructure encryption.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class MinimalTlsVersionEnum(str, Enum):
    """
    Enforce a minimal Tls version for the server.
    """
    TLS1_0 = "TLS1_0"
    TLS1_1 = "TLS1_1"
    TLS1_2 = "TLS1_2"
    TLS_ENFORCEMENT_DISABLED = "TLSEnforcementDisabled"


class PublicNetworkAccessEnum(str, Enum):
    """
    Whether or not public network access is allowed for this server. Value is optional but if passed in, must be 'Enabled' or 'Disabled'
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ServerKeyType(str, Enum):
    """
    The key type like 'AzureKeyVault'.
    """
    AZURE_KEY_VAULT = "AzureKeyVault"


class ServerVersion(str, Enum):
    """
    Server version.
    """
    _9_5 = "9.5"
    _9_6 = "9.6"
    _10 = "10"
    _10_0 = "10.0"
    _10_2 = "10.2"
    _11 = "11"


class SkuTier(str, Enum):
    """
    The tier of the particular SKU, e.g. Basic.
    """
    BASIC = "Basic"
    GENERAL_PURPOSE = "GeneralPurpose"
    MEMORY_OPTIMIZED = "MemoryOptimized"


class SslEnforcementEnum(str, Enum):
    """
    Enable ssl enforcement or not when connect to server.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class StorageAutogrow(str, Enum):
    """
    Enable Storage Auto Grow.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"
