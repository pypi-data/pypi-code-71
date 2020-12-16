# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables
from . import outputs

__all__ = [
    'GetAccountResult',
    'AwaitableGetAccountResult',
    'get_account',
]

@pulumi.output_type
class GetAccountResult:
    """
    Data Lake Store account information.
    """
    def __init__(__self__, account_id=None, creation_time=None, current_tier=None, default_group=None, encryption_config=None, encryption_provisioning_state=None, encryption_state=None, endpoint=None, firewall_allow_azure_ips=None, firewall_rules=None, firewall_state=None, id=None, identity=None, last_modified_time=None, location=None, name=None, new_tier=None, provisioning_state=None, state=None, tags=None, trusted_id_provider_state=None, trusted_id_providers=None, type=None, virtual_network_rules=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if current_tier and not isinstance(current_tier, str):
            raise TypeError("Expected argument 'current_tier' to be a str")
        pulumi.set(__self__, "current_tier", current_tier)
        if default_group and not isinstance(default_group, str):
            raise TypeError("Expected argument 'default_group' to be a str")
        pulumi.set(__self__, "default_group", default_group)
        if encryption_config and not isinstance(encryption_config, dict):
            raise TypeError("Expected argument 'encryption_config' to be a dict")
        pulumi.set(__self__, "encryption_config", encryption_config)
        if encryption_provisioning_state and not isinstance(encryption_provisioning_state, str):
            raise TypeError("Expected argument 'encryption_provisioning_state' to be a str")
        pulumi.set(__self__, "encryption_provisioning_state", encryption_provisioning_state)
        if encryption_state and not isinstance(encryption_state, str):
            raise TypeError("Expected argument 'encryption_state' to be a str")
        pulumi.set(__self__, "encryption_state", encryption_state)
        if endpoint and not isinstance(endpoint, str):
            raise TypeError("Expected argument 'endpoint' to be a str")
        pulumi.set(__self__, "endpoint", endpoint)
        if firewall_allow_azure_ips and not isinstance(firewall_allow_azure_ips, str):
            raise TypeError("Expected argument 'firewall_allow_azure_ips' to be a str")
        pulumi.set(__self__, "firewall_allow_azure_ips", firewall_allow_azure_ips)
        if firewall_rules and not isinstance(firewall_rules, list):
            raise TypeError("Expected argument 'firewall_rules' to be a list")
        pulumi.set(__self__, "firewall_rules", firewall_rules)
        if firewall_state and not isinstance(firewall_state, str):
            raise TypeError("Expected argument 'firewall_state' to be a str")
        pulumi.set(__self__, "firewall_state", firewall_state)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if last_modified_time and not isinstance(last_modified_time, str):
            raise TypeError("Expected argument 'last_modified_time' to be a str")
        pulumi.set(__self__, "last_modified_time", last_modified_time)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if new_tier and not isinstance(new_tier, str):
            raise TypeError("Expected argument 'new_tier' to be a str")
        pulumi.set(__self__, "new_tier", new_tier)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if trusted_id_provider_state and not isinstance(trusted_id_provider_state, str):
            raise TypeError("Expected argument 'trusted_id_provider_state' to be a str")
        pulumi.set(__self__, "trusted_id_provider_state", trusted_id_provider_state)
        if trusted_id_providers and not isinstance(trusted_id_providers, list):
            raise TypeError("Expected argument 'trusted_id_providers' to be a list")
        pulumi.set(__self__, "trusted_id_providers", trusted_id_providers)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if virtual_network_rules and not isinstance(virtual_network_rules, list):
            raise TypeError("Expected argument 'virtual_network_rules' to be a list")
        pulumi.set(__self__, "virtual_network_rules", virtual_network_rules)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        """
        The unique identifier associated with this Data Lake Store account.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> str:
        """
        The account creation time.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="currentTier")
    def current_tier(self) -> str:
        """
        The commitment tier in use for the current month.
        """
        return pulumi.get(self, "current_tier")

    @property
    @pulumi.getter(name="defaultGroup")
    def default_group(self) -> str:
        """
        The default owner group for all new folders and files created in the Data Lake Store account.
        """
        return pulumi.get(self, "default_group")

    @property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> 'outputs.EncryptionConfigResponse':
        """
        The Key Vault encryption configuration.
        """
        return pulumi.get(self, "encryption_config")

    @property
    @pulumi.getter(name="encryptionProvisioningState")
    def encryption_provisioning_state(self) -> str:
        """
        The current state of encryption provisioning for this Data Lake Store account.
        """
        return pulumi.get(self, "encryption_provisioning_state")

    @property
    @pulumi.getter(name="encryptionState")
    def encryption_state(self) -> str:
        """
        The current state of encryption for this Data Lake Store account.
        """
        return pulumi.get(self, "encryption_state")

    @property
    @pulumi.getter
    def endpoint(self) -> str:
        """
        The full CName endpoint for this account.
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter(name="firewallAllowAzureIps")
    def firewall_allow_azure_ips(self) -> str:
        """
        The current state of allowing or disallowing IPs originating within Azure through the firewall. If the firewall is disabled, this is not enforced.
        """
        return pulumi.get(self, "firewall_allow_azure_ips")

    @property
    @pulumi.getter(name="firewallRules")
    def firewall_rules(self) -> Sequence['outputs.FirewallRuleResponse']:
        """
        The list of firewall rules associated with this Data Lake Store account.
        """
        return pulumi.get(self, "firewall_rules")

    @property
    @pulumi.getter(name="firewallState")
    def firewall_state(self) -> str:
        """
        The current state of the IP address firewall for this Data Lake Store account.
        """
        return pulumi.get(self, "firewall_state")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource identifier.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> 'outputs.EncryptionIdentityResponse':
        """
        The Key Vault encryption identity, if any.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> str:
        """
        The account last modified time.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="newTier")
    def new_tier(self) -> str:
        """
        The commitment tier to use for next month.
        """
        return pulumi.get(self, "new_tier")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning status of the Data Lake Store account.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The state of the Data Lake Store account.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="trustedIdProviderState")
    def trusted_id_provider_state(self) -> str:
        """
        The current state of the trusted identity provider feature for this Data Lake Store account.
        """
        return pulumi.get(self, "trusted_id_provider_state")

    @property
    @pulumi.getter(name="trustedIdProviders")
    def trusted_id_providers(self) -> Sequence['outputs.TrustedIdProviderResponse']:
        """
        The list of trusted identity providers associated with this Data Lake Store account.
        """
        return pulumi.get(self, "trusted_id_providers")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualNetworkRules")
    def virtual_network_rules(self) -> Sequence['outputs.VirtualNetworkRuleResponse']:
        """
        The list of virtual network rules associated with this Data Lake Store account.
        """
        return pulumi.get(self, "virtual_network_rules")


class AwaitableGetAccountResult(GetAccountResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccountResult(
            account_id=self.account_id,
            creation_time=self.creation_time,
            current_tier=self.current_tier,
            default_group=self.default_group,
            encryption_config=self.encryption_config,
            encryption_provisioning_state=self.encryption_provisioning_state,
            encryption_state=self.encryption_state,
            endpoint=self.endpoint,
            firewall_allow_azure_ips=self.firewall_allow_azure_ips,
            firewall_rules=self.firewall_rules,
            firewall_state=self.firewall_state,
            id=self.id,
            identity=self.identity,
            last_modified_time=self.last_modified_time,
            location=self.location,
            name=self.name,
            new_tier=self.new_tier,
            provisioning_state=self.provisioning_state,
            state=self.state,
            tags=self.tags,
            trusted_id_provider_state=self.trusted_id_provider_state,
            trusted_id_providers=self.trusted_id_providers,
            type=self.type,
            virtual_network_rules=self.virtual_network_rules)


def get_account(account_name: Optional[str] = None,
                resource_group_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccountResult:
    """
    Use this data source to access information about an existing resource.

    :param str account_name: The name of the Data Lake Store account.
    :param str resource_group_name: The name of the Azure resource group.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-nextgen:datalakestore/latest:getAccount', __args__, opts=opts, typ=GetAccountResult).value

    return AwaitableGetAccountResult(
        account_id=__ret__.account_id,
        creation_time=__ret__.creation_time,
        current_tier=__ret__.current_tier,
        default_group=__ret__.default_group,
        encryption_config=__ret__.encryption_config,
        encryption_provisioning_state=__ret__.encryption_provisioning_state,
        encryption_state=__ret__.encryption_state,
        endpoint=__ret__.endpoint,
        firewall_allow_azure_ips=__ret__.firewall_allow_azure_ips,
        firewall_rules=__ret__.firewall_rules,
        firewall_state=__ret__.firewall_state,
        id=__ret__.id,
        identity=__ret__.identity,
        last_modified_time=__ret__.last_modified_time,
        location=__ret__.location,
        name=__ret__.name,
        new_tier=__ret__.new_tier,
        provisioning_state=__ret__.provisioning_state,
        state=__ret__.state,
        tags=__ret__.tags,
        trusted_id_provider_state=__ret__.trusted_id_provider_state,
        trusted_id_providers=__ret__.trusted_id_providers,
        type=__ret__.type,
        virtual_network_rules=__ret__.virtual_network_rules)
