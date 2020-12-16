# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ActionAfterReboot',
    'AllowModuleOverwrite',
    'CachingTypes',
    'ComponentNames',
    'ConfigurationMode',
    'DedicatedHostLicenseTypes',
    'DiffDiskOptions',
    'DiffDiskPlacement',
    'DiskCreateOption',
    'DiskCreateOptionTypes',
    'DiskEncryptionSetIdentityType',
    'DiskEncryptionSetType',
    'DiskStorageAccountTypes',
    'EncryptionType',
    'GallerySharingPermissionTypes',
    'HostCaching',
    'HyperVGeneration',
    'HyperVGenerationTypes',
    'IPVersion',
    'InGuestPatchMode',
    'IntervalInMins',
    'Kind',
    'NetworkAccessPolicy',
    'OperatingSystemStateTypes',
    'OperatingSystemTypes',
    'PassNames',
    'ProtocolTypes',
    'ProximityPlacementGroupType',
    'RebootIfNeeded',
    'ResourceIdentityType',
    'SettingNames',
    'SnapshotStorageAccountTypes',
    'StatusLevelTypes',
    'StorageAccountType',
    'StorageAccountTypes',
    'UpgradeMode',
    'VirtualMachineEvictionPolicyTypes',
    'VirtualMachinePriorityTypes',
    'VirtualMachineScaleSetScaleInRules',
    'VirtualMachineSizeTypes',
]


class ActionAfterReboot(str, Enum):
    """
    Specifies what happens after a reboot during the application of a configuration. The possible values are ContinueConfiguration and StopConfiguration
    """
    CONTINUE_CONFIGURATION = "ContinueConfiguration"
    STOP_CONFIGURATION = "StopConfiguration"


class AllowModuleOverwrite(str, Enum):
    """
    If true - new configurations downloaded from the pull service are allowed to overwrite the old ones on the target node. Otherwise, false
    """
    TRUE = "True"
    FALSE = "False"


class CachingTypes(str, Enum):
    """
    Specifies the caching requirements. <br><br> Possible values are: <br><br> **None** <br><br> **ReadOnly** <br><br> **ReadWrite** <br><br> Default: **None** for Standard storage. **ReadOnly** for Premium storage.
    """
    NONE = "None"
    READ_ONLY = "ReadOnly"
    READ_WRITE = "ReadWrite"


class ComponentNames(str, Enum):
    """
    The component name. Currently, the only allowable value is Microsoft-Windows-Shell-Setup.
    """
    MICROSOFT_WINDOWS_SHELL_SETUP = "Microsoft-Windows-Shell-Setup"


class ConfigurationMode(str, Enum):
    """
    Specifies how the LCM(Local Configuration Manager) actually applies the configuration to the target nodes. Possible values are ApplyOnly, ApplyAndMonitor, and ApplyAndAutoCorrect.
    """
    APPLY_ONLY = "ApplyOnly"
    APPLY_AND_MONITOR = "ApplyAndMonitor"
    APPLY_AND_AUTO_CORRECT = "ApplyAndAutoCorrect"


class DedicatedHostLicenseTypes(str, Enum):
    """
    Specifies the software license type that will be applied to the VMs deployed on the dedicated host. <br><br> Possible values are: <br><br> **None** <br><br> **Windows_Server_Hybrid** <br><br> **Windows_Server_Perpetual** <br><br> Default: **None**
    """
    NONE = "None"
    WINDOWS_SERVER_HYBRID = "Windows_Server_Hybrid"
    WINDOWS_SERVER_PERPETUAL = "Windows_Server_Perpetual"


class DiffDiskOptions(str, Enum):
    """
    Specifies the ephemeral disk settings for operating system disk.
    """
    LOCAL = "Local"


class DiffDiskPlacement(str, Enum):
    """
    Specifies the ephemeral disk placement for operating system disk.<br><br> Possible values are: <br><br> **CacheDisk** <br><br> **ResourceDisk** <br><br> Default: **CacheDisk** if one is configured for the VM size otherwise **ResourceDisk** is used.<br><br> Refer to VM size documentation for Windows VM at https://docs.microsoft.com/en-us/azure/virtual-machines/windows/sizes and Linux VM at https://docs.microsoft.com/en-us/azure/virtual-machines/linux/sizes to check which VM sizes exposes a cache disk.
    """
    CACHE_DISK = "CacheDisk"
    RESOURCE_DISK = "ResourceDisk"


class DiskCreateOption(str, Enum):
    """
    This enumerates the possible sources of a disk's creation.
    """
    EMPTY = "Empty"
    ATTACH = "Attach"
    FROM_IMAGE = "FromImage"
    IMPORT_ = "Import"
    COPY = "Copy"
    RESTORE = "Restore"
    UPLOAD = "Upload"


class DiskCreateOptionTypes(str, Enum):
    """
    Specifies how the virtual machine should be created.<br><br> Possible values are:<br><br> **Attach** \u2013 This value is used when you are using a specialized disk to create the virtual machine.<br><br> **FromImage** \u2013 This value is used when you are using an image to create the virtual machine. If you are using a platform image, you also use the imageReference element described above. If you are using a marketplace image, you  also use the plan element previously described.
    """
    FROM_IMAGE = "FromImage"
    EMPTY = "Empty"
    ATTACH = "Attach"


class DiskEncryptionSetIdentityType(str, Enum):
    """
    The type of Managed Identity used by the DiskEncryptionSet. Only SystemAssigned is supported.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"


class DiskEncryptionSetType(str, Enum):
    """
    The type of key used to encrypt the data of the disk.
    """
    ENCRYPTION_AT_REST_WITH_CUSTOMER_KEY = "EncryptionAtRestWithCustomerKey"
    ENCRYPTION_AT_REST_WITH_PLATFORM_AND_CUSTOMER_KEYS = "EncryptionAtRestWithPlatformAndCustomerKeys"


class DiskStorageAccountTypes(str, Enum):
    """
    The sku name.
    """
    STANDARD_LRS = "Standard_LRS"
    PREMIUM_LRS = "Premium_LRS"
    STANDARD_SS_D_LRS = "StandardSSD_LRS"
    ULTRA_SS_D_LRS = "UltraSSD_LRS"


class EncryptionType(str, Enum):
    """
    The type of key used to encrypt the data of the disk.
    """
    ENCRYPTION_AT_REST_WITH_PLATFORM_KEY = "EncryptionAtRestWithPlatformKey"
    ENCRYPTION_AT_REST_WITH_CUSTOMER_KEY = "EncryptionAtRestWithCustomerKey"
    ENCRYPTION_AT_REST_WITH_PLATFORM_AND_CUSTOMER_KEYS = "EncryptionAtRestWithPlatformAndCustomerKeys"


class GallerySharingPermissionTypes(str, Enum):
    """
    This property allows you to specify the permission of sharing gallery. <br><br> Possible values are: <br><br> **Private** <br><br> **Groups**
    """
    PRIVATE = "Private"
    GROUPS = "Groups"


class HostCaching(str, Enum):
    """
    The host caching of the disk. Valid values are 'None', 'ReadOnly', and 'ReadWrite'
    """
    NONE = "None"
    READ_ONLY = "ReadOnly"
    READ_WRITE = "ReadWrite"


class HyperVGeneration(str, Enum):
    """
    The hypervisor generation of the Virtual Machine. Applicable to OS disks only.
    """
    V1 = "V1"
    V2 = "V2"


class HyperVGenerationTypes(str, Enum):
    """
    Gets the HyperVGenerationType of the VirtualMachine created from the image
    """
    V1 = "V1"
    V2 = "V2"


class IPVersion(str, Enum):
    """
    Available from Api-Version 2019-07-01 onwards, it represents whether the specific ipconfiguration is IPv4 or IPv6. Default is taken as IPv4. Possible values are: 'IPv4' and 'IPv6'.
    """
    I_PV4 = "IPv4"
    I_PV6 = "IPv6"


class InGuestPatchMode(str, Enum):
    """
    Specifies the mode of in-guest patching to IaaS virtual machine.<br /><br /> Possible values are:<br /><br /> **Manual** - You  control the application of patches to a virtual machine. You do this by applying patches manually inside the VM. In this mode, automatic updates are disabled; the property WindowsConfiguration.enableAutomaticUpdates must be false<br /><br /> **AutomaticByOS** - The virtual machine will automatically be updated by the OS. The property WindowsConfiguration.enableAutomaticUpdates must be true. <br /><br /> ** AutomaticByPlatform** - the virtual machine will automatically updated by the platform. The properties provisionVMAgent and WindowsConfiguration.enableAutomaticUpdates must be true 
    """
    MANUAL = "Manual"
    AUTOMATIC_BY_OS = "AutomaticByOS"
    AUTOMATIC_BY_PLATFORM = "AutomaticByPlatform"


class IntervalInMins(str, Enum):
    """
    Interval value in minutes used to create LogAnalytics call rate logs.
    """
    THREE_MINS = "ThreeMins"
    FIVE_MINS = "FiveMins"
    THIRTY_MINS = "ThirtyMins"
    SIXTY_MINS = "SixtyMins"


class Kind(str, Enum):
    """
    Kind of the guest configuration. For example:DSC
    """
    DSC = "DSC"


class NetworkAccessPolicy(str, Enum):
    """
    Policy for accessing the disk via network.
    """
    ALLOW_ALL = "AllowAll"
    ALLOW_PRIVATE = "AllowPrivate"
    DENY_ALL = "DenyAll"


class OperatingSystemStateTypes(str, Enum):
    """
    The OS State.
    """
    GENERALIZED = "Generalized"
    SPECIALIZED = "Specialized"


class OperatingSystemTypes(str, Enum):
    """
    This property allows you to specify the type of the OS that is included in the disk if creating a VM from user-image or a specialized VHD. <br><br> Possible values are: <br><br> **Windows** <br><br> **Linux**
    """
    WINDOWS = "Windows"
    LINUX = "Linux"


class PassNames(str, Enum):
    """
    The pass name. Currently, the only allowable value is OobeSystem.
    """
    OOBE_SYSTEM = "OobeSystem"


class ProtocolTypes(str, Enum):
    """
    Specifies the protocol of WinRM listener. <br><br> Possible values are: <br>**http** <br><br> **https**
    """
    HTTP = "Http"
    HTTPS = "Https"


class ProximityPlacementGroupType(str, Enum):
    """
    Specifies the type of the proximity placement group. <br><br> Possible values are: <br><br> **Standard** : Co-locate resources within an Azure region or Availability Zone. <br><br> **Ultra** : For future use.
    """
    STANDARD = "Standard"
    ULTRA = "Ultra"


class RebootIfNeeded(str, Enum):
    """
    Set this to true to automatically reboot the node after a configuration that requires reboot is applied. Otherwise, you will have to manually reboot the node for any configuration that requires it. The default value is false. To use this setting when a reboot condition is enacted by something other than DSC (such as Windows Installer), combine this setting with the xPendingReboot module.
    """
    TRUE = "True"
    FALSE = "False"


class ResourceIdentityType(str, Enum):
    """
    The type of identity used for the virtual machine scale set. The type 'SystemAssigned, UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the virtual machine scale set.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"
    NONE = "None"


class SettingNames(str, Enum):
    """
    Specifies the name of the setting to which the content applies. Possible values are: FirstLogonCommands and AutoLogon.
    """
    AUTO_LOGON = "AutoLogon"
    FIRST_LOGON_COMMANDS = "FirstLogonCommands"


class SnapshotStorageAccountTypes(str, Enum):
    """
    The sku name.
    """
    STANDARD_LRS = "Standard_LRS"
    PREMIUM_LRS = "Premium_LRS"
    STANDARD_ZRS = "Standard_ZRS"


class StatusLevelTypes(str, Enum):
    """
    The level code.
    """
    INFO = "Info"
    WARNING = "Warning"
    ERROR = "Error"


class StorageAccountType(str, Enum):
    """
    Specifies the storage account type to be used to store the image. This property is not updatable.
    """
    STANDARD_LRS = "Standard_LRS"
    STANDARD_ZRS = "Standard_ZRS"
    PREMIUM_LRS = "Premium_LRS"


class StorageAccountTypes(str, Enum):
    """
    Specifies the storage account type for the managed disk. NOTE: UltraSSD_LRS can only be used with data disks, it cannot be used with OS Disk.
    """
    STANDARD_LRS = "Standard_LRS"
    PREMIUM_LRS = "Premium_LRS"
    STANDARD_SS_D_LRS = "StandardSSD_LRS"
    ULTRA_SS_D_LRS = "UltraSSD_LRS"


class UpgradeMode(str, Enum):
    """
    Specifies the mode of an upgrade to virtual machines in the scale set.<br /><br /> Possible values are:<br /><br /> **Manual** - You  control the application of updates to virtual machines in the scale set. You do this by using the manualUpgrade action.<br /><br /> **Automatic** - All virtual machines in the scale set are  automatically updated at the same time.
    """
    AUTOMATIC = "Automatic"
    MANUAL = "Manual"
    ROLLING = "Rolling"


class VirtualMachineEvictionPolicyTypes(str, Enum):
    """
    Specifies the eviction policy for the Azure Spot virtual machine and Azure Spot scale set. <br><br>For Azure Spot virtual machines, both 'Deallocate' and 'Delete' are supported and the minimum api-version is 2019-03-01. <br><br>For Azure Spot scale sets, both 'Deallocate' and 'Delete' are supported and the minimum api-version is 2017-10-30-preview.
    """
    DEALLOCATE = "Deallocate"
    DELETE = "Delete"


class VirtualMachinePriorityTypes(str, Enum):
    """
    Specifies the priority for the virtual machines in the scale set. <br><br>Minimum api-version: 2017-10-30-preview
    """
    REGULAR = "Regular"
    LOW = "Low"
    SPOT = "Spot"


class VirtualMachineScaleSetScaleInRules(str, Enum):
    DEFAULT = "Default"
    OLDEST_VM = "OldestVM"
    NEWEST_VM = "NewestVM"


class VirtualMachineSizeTypes(str, Enum):
    """
    Specifies the size of the virtual machine. For more information about virtual machine sizes, see [Sizes for virtual machines](https://docs.microsoft.com/en-us/azure/virtual-machines/sizes). <br><br> The available VM sizes depend on region and availability set. For a list of available sizes use these APIs:  <br><br> [List all available virtual machine sizes in an availability set](https://docs.microsoft.com/rest/api/compute/availabilitysets/listavailablesizes) <br><br> [List all available virtual machine sizes in a region]( https://docs.microsoft.com/en-us/rest/api/compute/resourceskus/list) <br><br> [List all available virtual machine sizes for resizing](https://docs.microsoft.com/rest/api/compute/virtualmachines/listavailablesizes). <br><br> This list of sizes is no longer updated and the **VirtualMachineSizeTypes** string constants will be removed from the subsequent REST API specification. Use [List all available virtual machine sizes in a region]( https://docs.microsoft.com/en-us/rest/api/compute/resourceskus/list) to get the latest sizes.
    """
    BASIC_A0 = "Basic_A0"
    BASIC_A1 = "Basic_A1"
    BASIC_A2 = "Basic_A2"
    BASIC_A3 = "Basic_A3"
    BASIC_A4 = "Basic_A4"
    STANDARD_A0 = "Standard_A0"
    STANDARD_A1 = "Standard_A1"
    STANDARD_A2 = "Standard_A2"
    STANDARD_A3 = "Standard_A3"
    STANDARD_A4 = "Standard_A4"
    STANDARD_A5 = "Standard_A5"
    STANDARD_A6 = "Standard_A6"
    STANDARD_A7 = "Standard_A7"
    STANDARD_A8 = "Standard_A8"
    STANDARD_A9 = "Standard_A9"
    STANDARD_A10 = "Standard_A10"
    STANDARD_A11 = "Standard_A11"
    STANDARD_A1_V2 = "Standard_A1_v2"
    STANDARD_A2_V2 = "Standard_A2_v2"
    STANDARD_A4_V2 = "Standard_A4_v2"
    STANDARD_A8_V2 = "Standard_A8_v2"
    STANDARD_A2M_V2 = "Standard_A2m_v2"
    STANDARD_A4M_V2 = "Standard_A4m_v2"
    STANDARD_A8M_V2 = "Standard_A8m_v2"
    STANDARD_B1S = "Standard_B1s"
    STANDARD_B1MS = "Standard_B1ms"
    STANDARD_B2S = "Standard_B2s"
    STANDARD_B2MS = "Standard_B2ms"
    STANDARD_B4MS = "Standard_B4ms"
    STANDARD_B8MS = "Standard_B8ms"
    STANDARD_D1 = "Standard_D1"
    STANDARD_D2 = "Standard_D2"
    STANDARD_D3 = "Standard_D3"
    STANDARD_D4 = "Standard_D4"
    STANDARD_D11 = "Standard_D11"
    STANDARD_D12 = "Standard_D12"
    STANDARD_D13 = "Standard_D13"
    STANDARD_D14 = "Standard_D14"
    STANDARD_D1_V2 = "Standard_D1_v2"
    STANDARD_D2_V2 = "Standard_D2_v2"
    STANDARD_D3_V2 = "Standard_D3_v2"
    STANDARD_D4_V2 = "Standard_D4_v2"
    STANDARD_D5_V2 = "Standard_D5_v2"
    STANDARD_D2_V3 = "Standard_D2_v3"
    STANDARD_D4_V3 = "Standard_D4_v3"
    STANDARD_D8_V3 = "Standard_D8_v3"
    STANDARD_D16_V3 = "Standard_D16_v3"
    STANDARD_D32_V3 = "Standard_D32_v3"
    STANDARD_D64_V3 = "Standard_D64_v3"
    STANDARD_D2S_V3 = "Standard_D2s_v3"
    STANDARD_D4S_V3 = "Standard_D4s_v3"
    STANDARD_D8S_V3 = "Standard_D8s_v3"
    STANDARD_D16S_V3 = "Standard_D16s_v3"
    STANDARD_D32S_V3 = "Standard_D32s_v3"
    STANDARD_D64S_V3 = "Standard_D64s_v3"
    STANDARD_D11_V2 = "Standard_D11_v2"
    STANDARD_D12_V2 = "Standard_D12_v2"
    STANDARD_D13_V2 = "Standard_D13_v2"
    STANDARD_D14_V2 = "Standard_D14_v2"
    STANDARD_D15_V2 = "Standard_D15_v2"
    STANDARD_DS1 = "Standard_DS1"
    STANDARD_DS2 = "Standard_DS2"
    STANDARD_DS3 = "Standard_DS3"
    STANDARD_DS4 = "Standard_DS4"
    STANDARD_DS11 = "Standard_DS11"
    STANDARD_DS12 = "Standard_DS12"
    STANDARD_DS13 = "Standard_DS13"
    STANDARD_DS14 = "Standard_DS14"
    STANDARD_DS1_V2 = "Standard_DS1_v2"
    STANDARD_DS2_V2 = "Standard_DS2_v2"
    STANDARD_DS3_V2 = "Standard_DS3_v2"
    STANDARD_DS4_V2 = "Standard_DS4_v2"
    STANDARD_DS5_V2 = "Standard_DS5_v2"
    STANDARD_DS11_V2 = "Standard_DS11_v2"
    STANDARD_DS12_V2 = "Standard_DS12_v2"
    STANDARD_DS13_V2 = "Standard_DS13_v2"
    STANDARD_DS14_V2 = "Standard_DS14_v2"
    STANDARD_DS15_V2 = "Standard_DS15_v2"
    STANDARD_DS13_4_V2 = "Standard_DS13-4_v2"
    STANDARD_DS13_2_V2 = "Standard_DS13-2_v2"
    STANDARD_DS14_8_V2 = "Standard_DS14-8_v2"
    STANDARD_DS14_4_V2 = "Standard_DS14-4_v2"
    STANDARD_E2_V3 = "Standard_E2_v3"
    STANDARD_E4_V3 = "Standard_E4_v3"
    STANDARD_E8_V3 = "Standard_E8_v3"
    STANDARD_E16_V3 = "Standard_E16_v3"
    STANDARD_E32_V3 = "Standard_E32_v3"
    STANDARD_E64_V3 = "Standard_E64_v3"
    STANDARD_E2S_V3 = "Standard_E2s_v3"
    STANDARD_E4S_V3 = "Standard_E4s_v3"
    STANDARD_E8S_V3 = "Standard_E8s_v3"
    STANDARD_E16S_V3 = "Standard_E16s_v3"
    STANDARD_E32S_V3 = "Standard_E32s_v3"
    STANDARD_E64S_V3 = "Standard_E64s_v3"
    STANDARD_E32_16_V3 = "Standard_E32-16_v3"
    STANDARD_E32_8S_V3 = "Standard_E32-8s_v3"
    STANDARD_E64_32S_V3 = "Standard_E64-32s_v3"
    STANDARD_E64_16S_V3 = "Standard_E64-16s_v3"
    STANDARD_F1 = "Standard_F1"
    STANDARD_F2 = "Standard_F2"
    STANDARD_F4 = "Standard_F4"
    STANDARD_F8 = "Standard_F8"
    STANDARD_F16 = "Standard_F16"
    STANDARD_F1S = "Standard_F1s"
    STANDARD_F2S = "Standard_F2s"
    STANDARD_F4S = "Standard_F4s"
    STANDARD_F8S = "Standard_F8s"
    STANDARD_F16S = "Standard_F16s"
    STANDARD_F2S_V2 = "Standard_F2s_v2"
    STANDARD_F4S_V2 = "Standard_F4s_v2"
    STANDARD_F8S_V2 = "Standard_F8s_v2"
    STANDARD_F16S_V2 = "Standard_F16s_v2"
    STANDARD_F32S_V2 = "Standard_F32s_v2"
    STANDARD_F64S_V2 = "Standard_F64s_v2"
    STANDARD_F72S_V2 = "Standard_F72s_v2"
    STANDARD_G1 = "Standard_G1"
    STANDARD_G2 = "Standard_G2"
    STANDARD_G3 = "Standard_G3"
    STANDARD_G4 = "Standard_G4"
    STANDARD_G5 = "Standard_G5"
    STANDARD_GS1 = "Standard_GS1"
    STANDARD_GS2 = "Standard_GS2"
    STANDARD_GS3 = "Standard_GS3"
    STANDARD_GS4 = "Standard_GS4"
    STANDARD_GS5 = "Standard_GS5"
    STANDARD_GS4_8 = "Standard_GS4-8"
    STANDARD_GS4_4 = "Standard_GS4-4"
    STANDARD_GS5_16 = "Standard_GS5-16"
    STANDARD_GS5_8 = "Standard_GS5-8"
    STANDARD_H8 = "Standard_H8"
    STANDARD_H16 = "Standard_H16"
    STANDARD_H8M = "Standard_H8m"
    STANDARD_H16M = "Standard_H16m"
    STANDARD_H16R = "Standard_H16r"
    STANDARD_H16MR = "Standard_H16mr"
    STANDARD_L4S = "Standard_L4s"
    STANDARD_L8S = "Standard_L8s"
    STANDARD_L16S = "Standard_L16s"
    STANDARD_L32S = "Standard_L32s"
    STANDARD_M64S = "Standard_M64s"
    STANDARD_M64MS = "Standard_M64ms"
    STANDARD_M128S = "Standard_M128s"
    STANDARD_M128MS = "Standard_M128ms"
    STANDARD_M64_32MS = "Standard_M64-32ms"
    STANDARD_M64_16MS = "Standard_M64-16ms"
    STANDARD_M128_64MS = "Standard_M128-64ms"
    STANDARD_M128_32MS = "Standard_M128-32ms"
    STANDARD_NC6 = "Standard_NC6"
    STANDARD_NC12 = "Standard_NC12"
    STANDARD_NC24 = "Standard_NC24"
    STANDARD_NC24R = "Standard_NC24r"
    STANDARD_NC6S_V2 = "Standard_NC6s_v2"
    STANDARD_NC12S_V2 = "Standard_NC12s_v2"
    STANDARD_NC24S_V2 = "Standard_NC24s_v2"
    STANDARD_NC24RS_V2 = "Standard_NC24rs_v2"
    STANDARD_NC6S_V3 = "Standard_NC6s_v3"
    STANDARD_NC12S_V3 = "Standard_NC12s_v3"
    STANDARD_NC24S_V3 = "Standard_NC24s_v3"
    STANDARD_NC24RS_V3 = "Standard_NC24rs_v3"
    STANDARD_ND6S = "Standard_ND6s"
    STANDARD_ND12S = "Standard_ND12s"
    STANDARD_ND24S = "Standard_ND24s"
    STANDARD_ND24RS = "Standard_ND24rs"
    STANDARD_NV6 = "Standard_NV6"
    STANDARD_NV12 = "Standard_NV12"
    STANDARD_NV24 = "Standard_NV24"
