# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'CertificatePermissions',
    'CreateMode',
    'JsonWebKeyCurveName',
    'JsonWebKeyOperation',
    'JsonWebKeyType',
    'KeyPermissions',
    'NetworkRuleAction',
    'NetworkRuleBypassOptions',
    'PrivateEndpointServiceConnectionStatus',
    'SecretPermissions',
    'SkuFamily',
    'SkuName',
    'StoragePermissions',
]


class CertificatePermissions(str, Enum):
    ALL = "all"
    GET = "get"
    LIST = "list"
    DELETE = "delete"
    CREATE = "create"
    IMPORT_ = "import"
    UPDATE = "update"
    MANAGECONTACTS = "managecontacts"
    GETISSUERS = "getissuers"
    LISTISSUERS = "listissuers"
    SETISSUERS = "setissuers"
    DELETEISSUERS = "deleteissuers"
    MANAGEISSUERS = "manageissuers"
    RECOVER = "recover"
    PURGE = "purge"
    BACKUP = "backup"
    RESTORE = "restore"


class CreateMode(str, Enum):
    """
    The vault's create mode to indicate whether the vault need to be recovered or not.
    """
    RECOVER = "recover"
    DEFAULT = "default"


class JsonWebKeyCurveName(str, Enum):
    """
    The elliptic curve name. For valid values, see JsonWebKeyCurveName.
    """
    P_256 = "P-256"
    P_384 = "P-384"
    P_521 = "P-521"
    P_256_K = "P-256K"


class JsonWebKeyOperation(str, Enum):
    """
    The permitted JSON web key operations of the key. For more information, see JsonWebKeyOperation.
    """
    ENCRYPT = "encrypt"
    DECRYPT = "decrypt"
    SIGN = "sign"
    VERIFY = "verify"
    WRAP_KEY = "wrapKey"
    UNWRAP_KEY = "unwrapKey"
    IMPORT_ = "import"


class JsonWebKeyType(str, Enum):
    """
    The type of the key. For valid values, see JsonWebKeyType.
    """
    EC = "EC"
    E_C_HSM = "EC-HSM"
    RSA = "RSA"
    RS_A_HSM = "RSA-HSM"


class KeyPermissions(str, Enum):
    ALL = "all"
    ENCRYPT = "encrypt"
    DECRYPT = "decrypt"
    WRAP_KEY = "wrapKey"
    UNWRAP_KEY = "unwrapKey"
    SIGN = "sign"
    VERIFY = "verify"
    GET = "get"
    LIST = "list"
    CREATE = "create"
    UPDATE = "update"
    IMPORT_ = "import"
    DELETE = "delete"
    BACKUP = "backup"
    RESTORE = "restore"
    RECOVER = "recover"
    PURGE = "purge"


class NetworkRuleAction(str, Enum):
    """
    The default action when no rule from ipRules and from virtualNetworkRules match. This is only used after the bypass property has been evaluated.
    """
    ALLOW = "Allow"
    DENY = "Deny"


class NetworkRuleBypassOptions(str, Enum):
    """
    Tells what traffic can bypass network rules. This can be 'AzureServices' or 'None'.  If not specified the default is 'AzureServices'.
    """
    AZURE_SERVICES = "AzureServices"
    NONE = "None"


class PrivateEndpointServiceConnectionStatus(str, Enum):
    """
    Indicates whether the connection has been approved, rejected or removed by the key vault owner.
    """
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"


class SecretPermissions(str, Enum):
    ALL = "all"
    GET = "get"
    LIST = "list"
    SET = "set"
    DELETE = "delete"
    BACKUP = "backup"
    RESTORE = "restore"
    RECOVER = "recover"
    PURGE = "purge"


class SkuFamily(str, Enum):
    """
    SKU family name
    """
    A = "A"


class SkuName(str, Enum):
    """
    SKU name to specify whether the key vault is a standard vault or a premium vault.
    """
    STANDARD = "standard"
    PREMIUM = "premium"


class StoragePermissions(str, Enum):
    ALL = "all"
    GET = "get"
    LIST = "list"
    DELETE = "delete"
    SET = "set"
    UPDATE = "update"
    REGENERATEKEY = "regeneratekey"
    RECOVER = "recover"
    PURGE = "purge"
    BACKUP = "backup"
    RESTORE = "restore"
    SETSAS = "setsas"
    LISTSAS = "listsas"
    GETSAS = "getsas"
    DELETESAS = "deletesas"
