# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'DataSource',
    'ExportData',
    'RecommendationConfigStatus',
    'RecommendationType',
    'SecuritySolutionStatus',
    'UnmaskedIpLoggingStatus',
]


class DataSource(str, Enum):
    TWIN_DATA = "TwinData"


class ExportData(str, Enum):
    RAW_EVENTS = "RawEvents"


class RecommendationConfigStatus(str, Enum):
    """
    Recommendation status. When the recommendation status is disabled recommendations are not generated.
    """
    DISABLED = "Disabled"
    ENABLED = "Enabled"


class RecommendationType(str, Enum):
    """
    The type of IoT Security recommendation.
    """
    IO_T_ACR_AUTHENTICATION = "IoT_ACRAuthentication"
    IO_T_AGENT_SENDS_UNUTILIZED_MESSAGES = "IoT_AgentSendsUnutilizedMessages"
    IO_T_BASELINE = "IoT_Baseline"
    IO_T_EDGE_HUB_MEM_OPTIMIZE = "IoT_EdgeHubMemOptimize"
    IO_T_EDGE_LOGGING_OPTIONS = "IoT_EdgeLoggingOptions"
    IO_T_INCONSISTENT_MODULE_SETTINGS = "IoT_InconsistentModuleSettings"
    IO_T_INSTALL_AGENT = "IoT_InstallAgent"
    IO_T_IP_FILTER_DENY_ALL = "IoT_IPFilter_DenyAll"
    IO_T_IP_FILTER_PERMISSIVE_RULE = "IoT_IPFilter_PermissiveRule"
    IO_T_OPEN_PORTS = "IoT_OpenPorts"
    IO_T_PERMISSIVE_FIREWALL_POLICY = "IoT_PermissiveFirewallPolicy"
    IO_T_PERMISSIVE_INPUT_FIREWALL_RULES = "IoT_PermissiveInputFirewallRules"
    IO_T_PERMISSIVE_OUTPUT_FIREWALL_RULES = "IoT_PermissiveOutputFirewallRules"
    IO_T_PRIVILEGED_DOCKER_OPTIONS = "IoT_PrivilegedDockerOptions"
    IO_T_SHARED_CREDENTIALS = "IoT_SharedCredentials"
    IO_T_VULNERABLE_TLS_CIPHER_SUITE = "IoT_VulnerableTLSCipherSuite"


class SecuritySolutionStatus(str, Enum):
    """
    Status of the IoT Security solution.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class UnmaskedIpLoggingStatus(str, Enum):
    """
    Unmasked IP address logging status
    """
    DISABLED = "Disabled"
    ENABLED = "Enabled"
