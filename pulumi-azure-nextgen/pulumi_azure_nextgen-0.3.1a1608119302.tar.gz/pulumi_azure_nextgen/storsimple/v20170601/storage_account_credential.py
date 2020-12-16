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

__all__ = ['StorageAccountCredential']


class StorageAccountCredential(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_key: Optional[pulumi.Input[pulumi.InputType['AsymmetricEncryptedSecretArgs']]] = None,
                 end_point: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input['Kind']] = None,
                 manager_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 ssl_status: Optional[pulumi.Input['SslStatus']] = None,
                 storage_account_credential_name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        The storage account credential.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AsymmetricEncryptedSecretArgs']] access_key: The details of the storage account password.
        :param pulumi.Input[str] end_point: The storage endpoint
        :param pulumi.Input['Kind'] kind: The Kind of the object. Currently only Series8000 is supported
        :param pulumi.Input[str] manager_name: The manager name
        :param pulumi.Input[str] resource_group_name: The resource group name
        :param pulumi.Input['SslStatus'] ssl_status: Signifies whether SSL needs to be enabled or not.
        :param pulumi.Input[str] storage_account_credential_name: The storage account credential name.
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

            __props__['access_key'] = access_key
            if end_point is None and not opts.urn:
                raise TypeError("Missing required property 'end_point'")
            __props__['end_point'] = end_point
            __props__['kind'] = kind
            if manager_name is None and not opts.urn:
                raise TypeError("Missing required property 'manager_name'")
            __props__['manager_name'] = manager_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            if ssl_status is None and not opts.urn:
                raise TypeError("Missing required property 'ssl_status'")
            __props__['ssl_status'] = ssl_status
            if storage_account_credential_name is None and not opts.urn:
                raise TypeError("Missing required property 'storage_account_credential_name'")
            __props__['storage_account_credential_name'] = storage_account_credential_name
            __props__['name'] = None
            __props__['type'] = None
            __props__['volumes_count'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:storsimple/latest:StorageAccountCredential"), pulumi.Alias(type_="azure-nextgen:storsimple/v20161001:StorageAccountCredential")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(StorageAccountCredential, __self__).__init__(
            'azure-nextgen:storsimple/v20170601:StorageAccountCredential',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'StorageAccountCredential':
        """
        Get an existing StorageAccountCredential resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return StorageAccountCredential(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessKey")
    def access_key(self) -> pulumi.Output[Optional['outputs.AsymmetricEncryptedSecretResponse']]:
        """
        The details of the storage account password.
        """
        return pulumi.get(self, "access_key")

    @property
    @pulumi.getter(name="endPoint")
    def end_point(self) -> pulumi.Output[str]:
        """
        The storage endpoint
        """
        return pulumi.get(self, "end_point")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        The Kind of the object. Currently only Series8000 is supported
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the object.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="sslStatus")
    def ssl_status(self) -> pulumi.Output[str]:
        """
        Signifies whether SSL needs to be enabled or not.
        """
        return pulumi.get(self, "ssl_status")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The hierarchical type of the object.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="volumesCount")
    def volumes_count(self) -> pulumi.Output[int]:
        """
        The count of volumes using this storage account credential.
        """
        return pulumi.get(self, "volumes_count")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

