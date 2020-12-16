# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AgentAutoUpdateStatus',
    'BackupItemType',
    'BackupManagementType',
    'ContainerType',
    'CreateMode',
    'DataSourceType',
    'DayOfWeek',
    'DiskAccountType',
    'FailoverDeploymentModel',
    'HealthStatus',
    'LastBackupStatus',
    'LicenseType',
    'MonthOfYear',
    'OperationType',
    'PolicyType',
    'PossibleOperationsDirections',
    'PrivateEndpointConnectionStatus',
    'ProtectedItemHealthStatus',
    'ProtectedItemState',
    'ProtectionState',
    'ProtectionStatus',
    'ProvisioningState',
    'RecoveryPlanGroupType',
    'ReplicationProtectedItemOperation',
    'ResourceHealthStatus',
    'ResourceIdentityType',
    'RetentionDurationType',
    'RetentionScheduleFormat',
    'ScheduleRunType',
    'SetMultiVmSyncStatus',
    'SkuName',
    'WeekOfMonth',
    'WorkloadType',
]


class AgentAutoUpdateStatus(str, Enum):
    """
    A value indicating whether the auto update is enabled.
    """
    DISABLED = "Disabled"
    ENABLED = "Enabled"


class BackupItemType(str, Enum):
    """
    Type of backup items associated with this container.
    """
    INVALID = "Invalid"
    VM = "VM"
    FILE_FOLDER = "FileFolder"
    AZURE_SQL_DB = "AzureSqlDb"
    SQLDB = "SQLDB"
    EXCHANGE = "Exchange"
    SHAREPOINT = "Sharepoint"
    V_MWARE_VM = "VMwareVM"
    SYSTEM_STATE = "SystemState"
    CLIENT = "Client"
    GENERIC_DATA_SOURCE = "GenericDataSource"
    SQL_DATA_BASE = "SQLDataBase"
    AZURE_FILE_SHARE = "AzureFileShare"
    SAP_HANA_DATABASE = "SAPHanaDatabase"
    SAPASE_DATABASE = "SAPAseDatabase"


class BackupManagementType(str, Enum):
    """
    Type of backup management for the backed up item.
    """
    INVALID = "Invalid"
    AZURE_IAAS_VM = "AzureIaasVM"
    MAB = "MAB"
    DPM = "DPM"
    AZURE_BACKUP_SERVER = "AzureBackupServer"
    AZURE_SQL = "AzureSql"
    AZURE_STORAGE = "AzureStorage"
    AZURE_WORKLOAD = "AzureWorkload"
    DEFAULT_BACKUP = "DefaultBackup"


class ContainerType(str, Enum):
    """
    Type of the container. The value of this property for: 1. Compute Azure VM is Microsoft.Compute/virtualMachines 2.
    Classic Compute Azure VM is Microsoft.ClassicCompute/virtualMachines 3. Windows machines (like MAB, DPM etc) is
    Windows 4. Azure SQL instance is AzureSqlContainer. 5. Storage containers is StorageContainer. 6. Azure workload
    Backup is VMAppContainer
    """
    INVALID = "Invalid"
    UNKNOWN = "Unknown"
    IAAS_VM_CONTAINER = "IaasVMContainer"
    IAAS_VM_SERVICE_CONTAINER = "IaasVMServiceContainer"
    DPM_CONTAINER = "DPMContainer"
    AZURE_BACKUP_SERVER_CONTAINER = "AzureBackupServerContainer"
    MAB_CONTAINER = "MABContainer"
    CLUSTER = "Cluster"
    AZURE_SQL_CONTAINER = "AzureSqlContainer"
    WINDOWS = "Windows"
    V_CENTER = "VCenter"
    VM_APP_CONTAINER = "VMAppContainer"
    SQLAG_WORK_LOAD_CONTAINER = "SQLAGWorkLoadContainer"
    STORAGE_CONTAINER = "StorageContainer"
    GENERIC_CONTAINER = "GenericContainer"


class CreateMode(str, Enum):
    """
    Create mode to indicate recovery of existing soft deleted data source or creation of new data source.
    """
    INVALID = "Invalid"
    DEFAULT = "Default"
    RECOVER = "Recover"


class DataSourceType(str, Enum):
    """
    Type of workload this item represents.
    """
    INVALID = "Invalid"
    VM = "VM"
    FILE_FOLDER = "FileFolder"
    AZURE_SQL_DB = "AzureSqlDb"
    SQLDB = "SQLDB"
    EXCHANGE = "Exchange"
    SHAREPOINT = "Sharepoint"
    V_MWARE_VM = "VMwareVM"
    SYSTEM_STATE = "SystemState"
    CLIENT = "Client"
    GENERIC_DATA_SOURCE = "GenericDataSource"
    SQL_DATA_BASE = "SQLDataBase"
    AZURE_FILE_SHARE = "AzureFileShare"
    SAP_HANA_DATABASE = "SAPHanaDatabase"
    SAPASE_DATABASE = "SAPAseDatabase"


class DayOfWeek(str, Enum):
    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"


class DiskAccountType(str, Enum):
    """
    The disk type.
    """
    STANDARD_LRS = "Standard_LRS"
    PREMIUM_LRS = "Premium_LRS"
    STANDARD_SS_D_LRS = "StandardSSD_LRS"


class FailoverDeploymentModel(str, Enum):
    """
    The failover deployment model.
    """
    NOT_APPLICABLE = "NotApplicable"
    CLASSIC = "Classic"
    RESOURCE_MANAGER = "ResourceManager"


class HealthStatus(str, Enum):
    """
    Health status of protected item.
    """
    PASSED = "Passed"
    ACTION_REQUIRED = "ActionRequired"
    ACTION_SUGGESTED = "ActionSuggested"
    INVALID = "Invalid"


class LastBackupStatus(str, Enum):
    """
    Last backup operation status. Possible values: Healthy, Unhealthy.
    """
    INVALID = "Invalid"
    HEALTHY = "Healthy"
    UNHEALTHY = "Unhealthy"
    IR_PENDING = "IRPending"


class LicenseType(str, Enum):
    """
    The license type.
    """
    NOT_SPECIFIED = "NotSpecified"
    NO_LICENSE_TYPE = "NoLicenseType"
    WINDOWS_SERVER = "WindowsServer"


class MonthOfYear(str, Enum):
    INVALID = "Invalid"
    JANUARY = "January"
    FEBRUARY = "February"
    MARCH = "March"
    APRIL = "April"
    MAY = "May"
    JUNE = "June"
    JULY = "July"
    AUGUST = "August"
    SEPTEMBER = "September"
    OCTOBER = "October"
    NOVEMBER = "November"
    DECEMBER = "December"


class OperationType(str, Enum):
    """
    Re-Do Operation
    """
    INVALID = "Invalid"
    REGISTER = "Register"
    REREGISTER = "Reregister"


class PolicyType(str, Enum):
    """
    Type of backup policy type
    """
    INVALID = "Invalid"
    FULL = "Full"
    DIFFERENTIAL = "Differential"
    LOG = "Log"
    COPY_ONLY_FULL = "CopyOnlyFull"
    INCREMENTAL = "Incremental"


class PossibleOperationsDirections(str, Enum):
    PRIMARY_TO_RECOVERY = "PrimaryToRecovery"
    RECOVERY_TO_PRIMARY = "RecoveryToPrimary"


class PrivateEndpointConnectionStatus(str, Enum):
    """
    Gets or sets the status
    """
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"


class ProtectedItemHealthStatus(str, Enum):
    """
    Health status of the backup item, evaluated based on last heartbeat received
    """
    INVALID = "Invalid"
    HEALTHY = "Healthy"
    UNHEALTHY = "Unhealthy"
    NOT_REACHABLE = "NotReachable"
    IR_PENDING = "IRPending"


class ProtectedItemState(str, Enum):
    """
    Protection state of the backup engine
    """
    INVALID = "Invalid"
    IR_PENDING = "IRPending"
    PROTECTED = "Protected"
    PROTECTION_ERROR = "ProtectionError"
    PROTECTION_STOPPED = "ProtectionStopped"
    PROTECTION_PAUSED = "ProtectionPaused"


class ProtectionState(str, Enum):
    """
    Backup state of this backup item.
    """
    INVALID = "Invalid"
    IR_PENDING = "IRPending"
    PROTECTED = "Protected"
    PROTECTION_ERROR = "ProtectionError"
    PROTECTION_STOPPED = "ProtectionStopped"
    PROTECTION_PAUSED = "ProtectionPaused"


class ProtectionStatus(str, Enum):
    """
    Backup state of this backup item.
    """
    INVALID = "Invalid"
    NOT_PROTECTED = "NotProtected"
    PROTECTING = "Protecting"
    PROTECTED = "Protected"
    PROTECTION_FAILED = "ProtectionFailed"


class ProvisioningState(str, Enum):
    """
    Gets or sets provisioning state of the private endpoint connection
    """
    SUCCEEDED = "Succeeded"
    DELETING = "Deleting"
    FAILED = "Failed"
    PENDING = "Pending"


class RecoveryPlanGroupType(str, Enum):
    """
    The group type.
    """
    SHUTDOWN = "Shutdown"
    BOOT = "Boot"
    FAILOVER = "Failover"


class ReplicationProtectedItemOperation(str, Enum):
    REVERSE_REPLICATE = "ReverseReplicate"
    COMMIT = "Commit"
    PLANNED_FAILOVER = "PlannedFailover"
    UNPLANNED_FAILOVER = "UnplannedFailover"
    DISABLE_PROTECTION = "DisableProtection"
    TEST_FAILOVER = "TestFailover"
    TEST_FAILOVER_CLEANUP = "TestFailoverCleanup"
    FAILBACK = "Failback"
    FINALIZE_FAILBACK = "FinalizeFailback"
    CHANGE_PIT = "ChangePit"
    REPAIR_REPLICATION = "RepairReplication"
    SWITCH_PROTECTION = "SwitchProtection"
    COMPLETE_MIGRATION = "CompleteMigration"


class ResourceHealthStatus(str, Enum):
    """
    Resource Health Status
    """
    HEALTHY = "Healthy"
    TRANSIENT_DEGRADED = "TransientDegraded"
    PERSISTENT_DEGRADED = "PersistentDegraded"
    TRANSIENT_UNHEALTHY = "TransientUnhealthy"
    PERSISTENT_UNHEALTHY = "PersistentUnhealthy"
    INVALID = "Invalid"


class ResourceIdentityType(str, Enum):
    """
    The identity type.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"
    NONE = "None"


class RetentionDurationType(str, Enum):
    """
    Retention duration type of retention policy.
    """
    INVALID = "Invalid"
    DAYS = "Days"
    WEEKS = "Weeks"
    MONTHS = "Months"
    YEARS = "Years"


class RetentionScheduleFormat(str, Enum):
    """
    Retention schedule format for yearly retention policy.
    """
    INVALID = "Invalid"
    DAILY = "Daily"
    WEEKLY = "Weekly"


class ScheduleRunType(str, Enum):
    """
    Frequency of the schedule operation of this policy.
    """
    INVALID = "Invalid"
    DAILY = "Daily"
    WEEKLY = "Weekly"


class SetMultiVmSyncStatus(str, Enum):
    """
    A value indicating whether multi-VM sync has to be enabled. Value should be 'Enabled' or 'Disabled'.
    """
    ENABLE = "Enable"
    DISABLE = "Disable"


class SkuName(str, Enum):
    """
    The Sku name.
    """
    STANDARD = "Standard"
    RS0 = "RS0"


class WeekOfMonth(str, Enum):
    FIRST = "First"
    SECOND = "Second"
    THIRD = "Third"
    FOURTH = "Fourth"
    LAST = "Last"
    INVALID = "Invalid"


class WorkloadType(str, Enum):
    """
    Type of workload for the backup management
    """
    INVALID = "Invalid"
    VM = "VM"
    FILE_FOLDER = "FileFolder"
    AZURE_SQL_DB = "AzureSqlDb"
    SQLDB = "SQLDB"
    EXCHANGE = "Exchange"
    SHAREPOINT = "Sharepoint"
    V_MWARE_VM = "VMwareVM"
    SYSTEM_STATE = "SystemState"
    CLIENT = "Client"
    GENERIC_DATA_SOURCE = "GenericDataSource"
    SQL_DATA_BASE = "SQLDataBase"
    AZURE_FILE_SHARE = "AzureFileShare"
    SAP_HANA_DATABASE = "SAPHanaDatabase"
    SAPASE_DATABASE = "SAPAseDatabase"
