# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ConfigurationProfile',
]


class ConfigurationProfile(str, Enum):
    """
    A value indicating configuration profile.
    """
    AZURE_VIRTUAL_MACHINE_BEST_PRACTICES_DEV_TEST = "Azure virtual machine best practices – Dev/Test"
    AZURE_VIRTUAL_MACHINE_BEST_PRACTICES_PRODUCTION = "Azure virtual machine best practices – Production"
