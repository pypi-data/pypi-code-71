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

__all__ = ['GuestConfigurationAssignment']


class GuestConfigurationAssignment(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 guest_configuration_assignment_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['GuestConfigurationAssignmentPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 vm_name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Guest configuration assignment is an association between a machine and guest configuration.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] guest_configuration_assignment_name: Name of the guest configuration assignment.
        :param pulumi.Input[str] location: Region where the VM is located.
        :param pulumi.Input[str] name: Name of the guest configuration assignment.
        :param pulumi.Input[pulumi.InputType['GuestConfigurationAssignmentPropertiesArgs']] properties: Properties of the Guest configuration assignment.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] vm_name: The name of the virtual machine.
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

            if guest_configuration_assignment_name is None and not opts.urn:
                raise TypeError("Missing required property 'guest_configuration_assignment_name'")
            __props__['guest_configuration_assignment_name'] = guest_configuration_assignment_name
            __props__['location'] = location
            __props__['name'] = name
            __props__['properties'] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            if vm_name is None and not opts.urn:
                raise TypeError("Missing required property 'vm_name'")
            __props__['vm_name'] = vm_name
            __props__['type'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:compute/latest:GuestConfigurationAssignment"), pulumi.Alias(type_="azure-nextgen:compute/v20180630preview:GuestConfigurationAssignment"), pulumi.Alias(type_="azure-nextgen:compute/v20181120:GuestConfigurationAssignment")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(GuestConfigurationAssignment, __self__).__init__(
            'azure-nextgen:compute/v20200625:GuestConfigurationAssignment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'GuestConfigurationAssignment':
        """
        Get an existing GuestConfigurationAssignment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return GuestConfigurationAssignment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Region where the VM is located.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        Name of the guest configuration assignment.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.GuestConfigurationAssignmentPropertiesResponse']:
        """
        Properties of the Guest configuration assignment.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

