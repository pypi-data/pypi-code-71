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

__all__ = ['PolicySetDefinition']


class PolicySetDefinition(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[Any] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['ParameterDefinitionsValueArgs']]]]] = None,
                 policy_definition_groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PolicyDefinitionGroupArgs']]]]] = None,
                 policy_definitions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PolicyDefinitionReferenceArgs']]]]] = None,
                 policy_set_definition_name: Optional[pulumi.Input[str]] = None,
                 policy_type: Optional[pulumi.Input[Union[str, 'PolicyType']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        The policy set definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The policy set definition description.
        :param pulumi.Input[str] display_name: The display name of the policy set definition.
        :param Any metadata: The policy set definition metadata.  Metadata is an open ended object and is typically a collection of key value pairs.
        :param pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['ParameterDefinitionsValueArgs']]]] parameters: The policy set definition parameters that can be used in policy definition references.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PolicyDefinitionGroupArgs']]]] policy_definition_groups: The metadata describing groups of policy definition references within the policy set definition.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PolicyDefinitionReferenceArgs']]]] policy_definitions: An array of policy definition references.
        :param pulumi.Input[str] policy_set_definition_name: The name of the policy set definition to create.
        :param pulumi.Input[Union[str, 'PolicyType']] policy_type: The type of policy definition. Possible values are NotSpecified, BuiltIn, Custom, and Static.
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

            __props__['description'] = description
            __props__['display_name'] = display_name
            __props__['metadata'] = metadata
            __props__['parameters'] = parameters
            __props__['policy_definition_groups'] = policy_definition_groups
            if policy_definitions is None and not opts.urn:
                raise TypeError("Missing required property 'policy_definitions'")
            __props__['policy_definitions'] = policy_definitions
            if policy_set_definition_name is None and not opts.urn:
                raise TypeError("Missing required property 'policy_set_definition_name'")
            __props__['policy_set_definition_name'] = policy_set_definition_name
            __props__['policy_type'] = policy_type
            __props__['name'] = None
            __props__['type'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:authorization/latest:PolicySetDefinition"), pulumi.Alias(type_="azure-nextgen:authorization/v20170601preview:PolicySetDefinition"), pulumi.Alias(type_="azure-nextgen:authorization/v20180301:PolicySetDefinition"), pulumi.Alias(type_="azure-nextgen:authorization/v20180501:PolicySetDefinition"), pulumi.Alias(type_="azure-nextgen:authorization/v20190101:PolicySetDefinition"), pulumi.Alias(type_="azure-nextgen:authorization/v20190601:PolicySetDefinition"), pulumi.Alias(type_="azure-nextgen:authorization/v20200301:PolicySetDefinition"), pulumi.Alias(type_="azure-nextgen:authorization/v20200901:PolicySetDefinition")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PolicySetDefinition, __self__).__init__(
            'azure-nextgen:authorization/v20190901:PolicySetDefinition',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PolicySetDefinition':
        """
        Get an existing PolicySetDefinition resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return PolicySetDefinition(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The policy set definition description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        The display name of the policy set definition.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Any]]:
        """
        The policy set definition metadata.  Metadata is an open ended object and is typically a collection of key value pairs.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the policy set definition.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Mapping[str, 'outputs.ParameterDefinitionsValueResponse']]]:
        """
        The policy set definition parameters that can be used in policy definition references.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="policyDefinitionGroups")
    def policy_definition_groups(self) -> pulumi.Output[Optional[Sequence['outputs.PolicyDefinitionGroupResponse']]]:
        """
        The metadata describing groups of policy definition references within the policy set definition.
        """
        return pulumi.get(self, "policy_definition_groups")

    @property
    @pulumi.getter(name="policyDefinitions")
    def policy_definitions(self) -> pulumi.Output[Sequence['outputs.PolicyDefinitionReferenceResponse']]:
        """
        An array of policy definition references.
        """
        return pulumi.get(self, "policy_definitions")

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of policy definition. Possible values are NotSpecified, BuiltIn, Custom, and Static.
        """
        return pulumi.get(self, "policy_type")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource (Microsoft.Authorization/policySetDefinitions).
        """
        return pulumi.get(self, "type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

