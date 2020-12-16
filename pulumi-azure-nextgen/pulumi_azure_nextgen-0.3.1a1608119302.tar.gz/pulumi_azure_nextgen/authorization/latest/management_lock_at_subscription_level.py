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

__all__ = ['ManagementLockAtSubscriptionLevel']


class ManagementLockAtSubscriptionLevel(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 level: Optional[pulumi.Input[Union[str, 'LockLevel']]] = None,
                 lock_name: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 owners: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ManagementLockOwnerArgs']]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        The lock information.
        Latest API Version: 2016-09-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'LockLevel']] level: The level of the lock. Possible values are: NotSpecified, CanNotDelete, ReadOnly. CanNotDelete means authorized users are able to read and modify the resources, but not delete. ReadOnly means authorized users can only read from a resource, but they can't modify or delete it.
        :param pulumi.Input[str] lock_name: The name of lock. The lock name can be a maximum of 260 characters. It cannot contain <, > %, &, :, \, ?, /, or any control characters.
        :param pulumi.Input[str] notes: Notes about the lock. Maximum of 512 characters.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ManagementLockOwnerArgs']]]] owners: The owners of the lock.
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

            if level is None and not opts.urn:
                raise TypeError("Missing required property 'level'")
            __props__['level'] = level
            if lock_name is None and not opts.urn:
                raise TypeError("Missing required property 'lock_name'")
            __props__['lock_name'] = lock_name
            __props__['notes'] = notes
            __props__['owners'] = owners
            __props__['name'] = None
            __props__['type'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:authorization/v20150101:ManagementLockAtSubscriptionLevel"), pulumi.Alias(type_="azure-nextgen:authorization/v20160901:ManagementLockAtSubscriptionLevel")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ManagementLockAtSubscriptionLevel, __self__).__init__(
            'azure-nextgen:authorization/latest:ManagementLockAtSubscriptionLevel',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ManagementLockAtSubscriptionLevel':
        """
        Get an existing ManagementLockAtSubscriptionLevel resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return ManagementLockAtSubscriptionLevel(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def level(self) -> pulumi.Output[str]:
        """
        The level of the lock. Possible values are: NotSpecified, CanNotDelete, ReadOnly. CanNotDelete means authorized users are able to read and modify the resources, but not delete. ReadOnly means authorized users can only read from a resource, but they can't modify or delete it.
        """
        return pulumi.get(self, "level")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the lock.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def notes(self) -> pulumi.Output[Optional[str]]:
        """
        Notes about the lock. Maximum of 512 characters.
        """
        return pulumi.get(self, "notes")

    @property
    @pulumi.getter
    def owners(self) -> pulumi.Output[Optional[Sequence['outputs.ManagementLockOwnerResponse']]]:
        """
        The owners of the lock.
        """
        return pulumi.get(self, "owners")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The resource type of the lock - Microsoft.Authorization/locks.
        """
        return pulumi.get(self, "type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

