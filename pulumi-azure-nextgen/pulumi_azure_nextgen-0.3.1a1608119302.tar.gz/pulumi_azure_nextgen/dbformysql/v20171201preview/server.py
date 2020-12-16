# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['Server']


class Server(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union[pulumi.InputType['ServerPropertiesForDefaultCreateArgs'], pulumi.InputType['ServerPropertiesForGeoRestoreArgs'], pulumi.InputType['ServerPropertiesForReplicaArgs'], pulumi.InputType['ServerPropertiesForRestoreArgs']]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Represents a server.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: The location the resource resides in.
        :param pulumi.Input[Union[pulumi.InputType['ServerPropertiesForDefaultCreateArgs'], pulumi.InputType['ServerPropertiesForGeoRestoreArgs'], pulumi.InputType['ServerPropertiesForReplicaArgs'], pulumi.InputType['ServerPropertiesForRestoreArgs']]] properties: Properties of the server.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] server_name: The name of the server.
        :param pulumi.Input[pulumi.InputType['SkuArgs']] sku: The SKU (pricing tier) of the server.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Application-specific metadata in the form of key-value pairs.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__['location'] = location
            if properties is None and not opts.urn:
                raise TypeError("Missing required property 'properties'")
            __props__['properties'] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            if server_name is None and not opts.urn:
                raise TypeError("Missing required property 'server_name'")
            __props__['server_name'] = server_name
            __props__['sku'] = sku
            __props__['tags'] = tags
            __props__['administrator_login'] = None
            __props__['byok_enforcement'] = None
            __props__['earliest_restore_date'] = None
            __props__['fully_qualified_domain_name'] = None
            __props__['identity'] = None
            __props__['infrastructure_encryption'] = None
            __props__['master_server_id'] = None
            __props__['minimal_tls_version'] = None
            __props__['name'] = None
            __props__['private_endpoint_connections'] = None
            __props__['public_network_access'] = None
            __props__['replica_capacity'] = None
            __props__['replication_role'] = None
            __props__['ssl_enforcement'] = None
            __props__['storage_profile'] = None
            __props__['type'] = None
            __props__['user_visible_state'] = None
            __props__['version'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:dbformysql/latest:Server"), pulumi.Alias(type_="azure-nextgen:dbformysql/v20171201:Server")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Server, __self__).__init__(
            'azure-nextgen:dbformysql/v20171201preview:Server',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Server':
        """
        Get an existing Server resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return Server(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="administratorLogin")
    def administrator_login(self) -> pulumi.Output[Optional[str]]:
        """
        The administrator's login name of a server. Can only be specified when the server is being created (and is required for creation).
        """
        return pulumi.get(self, "administrator_login")

    @property
    @pulumi.getter(name="byokEnforcement")
    def byok_enforcement(self) -> pulumi.Output[str]:
        """
        Status showing whether the server data encryption is enabled with customer-managed keys.
        """
        return pulumi.get(self, "byok_enforcement")

    @property
    @pulumi.getter(name="earliestRestoreDate")
    def earliest_restore_date(self) -> pulumi.Output[Optional[str]]:
        """
        Earliest restore point creation time (ISO8601 format)
        """
        return pulumi.get(self, "earliest_restore_date")

    @property
    @pulumi.getter(name="fullyQualifiedDomainName")
    def fully_qualified_domain_name(self) -> pulumi.Output[Optional[str]]:
        """
        The fully qualified domain name of a server.
        """
        return pulumi.get(self, "fully_qualified_domain_name")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ResourceIdentityResponse']]:
        """
        The Azure Active Directory identity of the server.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="infrastructureEncryption")
    def infrastructure_encryption(self) -> pulumi.Output[Optional[str]]:
        """
        Status showing whether the server enabled infrastructure encryption.
        """
        return pulumi.get(self, "infrastructure_encryption")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="masterServerId")
    def master_server_id(self) -> pulumi.Output[Optional[str]]:
        """
        The master server id of a replica server.
        """
        return pulumi.get(self, "master_server_id")

    @property
    @pulumi.getter(name="minimalTlsVersion")
    def minimal_tls_version(self) -> pulumi.Output[Optional[str]]:
        """
        Enforce a minimal Tls version for the server.
        """
        return pulumi.get(self, "minimal_tls_version")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> pulumi.Output[Sequence['outputs.ServerPrivateEndpointConnectionResponse']]:
        """
        List of private endpoint connections on a server
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[Optional[str]]:
        """
        Whether or not public endpoint access is allowed for this server.  Value is optional but if passed in, must be 'Enabled' or 'Disabled'
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter(name="replicaCapacity")
    def replica_capacity(self) -> pulumi.Output[Optional[int]]:
        """
        The maximum number of replicas that a master server can have.
        """
        return pulumi.get(self, "replica_capacity")

    @property
    @pulumi.getter(name="replicationRole")
    def replication_role(self) -> pulumi.Output[Optional[str]]:
        """
        The replication role of the server.
        """
        return pulumi.get(self, "replication_role")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.SkuResponse']]:
        """
        The SKU (pricing tier) of the server.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="sslEnforcement")
    def ssl_enforcement(self) -> pulumi.Output[Optional[str]]:
        """
        Enable ssl enforcement or not when connect to server.
        """
        return pulumi.get(self, "ssl_enforcement")

    @property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> pulumi.Output[Optional['outputs.StorageProfileResponse']]:
        """
        Storage profile of a server.
        """
        return pulumi.get(self, "storage_profile")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userVisibleState")
    def user_visible_state(self) -> pulumi.Output[Optional[str]]:
        """
        A state of a server that is visible to user.
        """
        return pulumi.get(self, "user_visible_state")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[str]]:
        """
        Server version.
        """
        return pulumi.get(self, "version")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

