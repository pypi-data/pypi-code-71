# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'CertificateOrderStatus',
    'CertificateProductType',
    'KeyVaultSecretStatus',
    'ProvisioningState',
]


class CertificateOrderStatus(str, Enum):
    """
    Current order status
    """
    PENDINGISSUANCE = "Pendingissuance"
    ISSUED = "Issued"
    REVOKED = "Revoked"
    CANCELED = "Canceled"
    DENIED = "Denied"
    PENDINGREVOCATION = "Pendingrevocation"
    PENDING_REKEY = "PendingRekey"
    UNUSED = "Unused"
    EXPIRED = "Expired"
    NOT_SUBMITTED = "NotSubmitted"


class CertificateProductType(str, Enum):
    """
    Certificate product type
    """
    STANDARD_DOMAIN_VALIDATED_SSL = "StandardDomainValidatedSsl"
    STANDARD_DOMAIN_VALIDATED_WILD_CARD_SSL = "StandardDomainValidatedWildCardSsl"


class KeyVaultSecretStatus(str, Enum):
    """
    Status of the Key Vault secret
    """
    INITIALIZED = "Initialized"
    WAITING_ON_CERTIFICATE_ORDER = "WaitingOnCertificateOrder"
    SUCCEEDED = "Succeeded"
    CERTIFICATE_ORDER_FAILED = "CertificateOrderFailed"
    OPERATION_NOT_PERMITTED_ON_KEY_VAULT = "OperationNotPermittedOnKeyVault"
    AZURE_SERVICE_UNAUTHORIZED_TO_ACCESS_KEY_VAULT = "AzureServiceUnauthorizedToAccessKeyVault"
    KEY_VAULT_DOES_NOT_EXIST = "KeyVaultDoesNotExist"
    KEY_VAULT_SECRET_DOES_NOT_EXIST = "KeyVaultSecretDoesNotExist"
    UNKNOWN_ERROR = "UnknownError"
    UNKNOWN = "Unknown"


class ProvisioningState(str, Enum):
    """
    Status of certificate order
    """
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    IN_PROGRESS = "InProgress"
    DELETING = "Deleting"
