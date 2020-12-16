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

__all__ = ['JobDefinition']


class JobDefinition(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 customer_secrets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomerSecretArgs']]]]] = None,
                 data_manager_name: Optional[pulumi.Input[str]] = None,
                 data_service_input: Optional[Any] = None,
                 data_service_name: Optional[pulumi.Input[str]] = None,
                 data_sink_id: Optional[pulumi.Input[str]] = None,
                 data_source_id: Optional[pulumi.Input[str]] = None,
                 job_definition_name: Optional[pulumi.Input[str]] = None,
                 last_modified_time: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 run_location: Optional[pulumi.Input['RunLocation']] = None,
                 schedules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScheduleArgs']]]]] = None,
                 state: Optional[pulumi.Input['State']] = None,
                 user_confirmation: Optional[pulumi.Input['UserConfirmation']] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Job Definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomerSecretArgs']]]] customer_secrets: List of customer secrets containing a key identifier and key value. The key identifier is a way for the specific data source to understand the key. Value contains customer secret encrypted by the encryptionKeys.
        :param pulumi.Input[str] data_manager_name: The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
        :param Any data_service_input: A generic json used differently by each data service type.
        :param pulumi.Input[str] data_service_name: The data service type of the job definition.
        :param pulumi.Input[str] data_sink_id: Data Sink Id associated to the job definition.
        :param pulumi.Input[str] data_source_id: Data Source Id associated to the job definition.
        :param pulumi.Input[str] job_definition_name: The job definition name to be created or updated.
        :param pulumi.Input[str] last_modified_time: Last modified time of the job definition.
        :param pulumi.Input[str] resource_group_name: The Resource Group Name
        :param pulumi.Input['RunLocation'] run_location: This is the preferred geo location for the job to run.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScheduleArgs']]]] schedules: Schedule for running the job definition
        :param pulumi.Input['State'] state: State of the job definition.
        :param pulumi.Input['UserConfirmation'] user_confirmation: Enum to detect if user confirmation is required. If not passed will default to NotRequired.
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

            __props__['customer_secrets'] = customer_secrets
            if data_manager_name is None and not opts.urn:
                raise TypeError("Missing required property 'data_manager_name'")
            __props__['data_manager_name'] = data_manager_name
            __props__['data_service_input'] = data_service_input
            if data_service_name is None and not opts.urn:
                raise TypeError("Missing required property 'data_service_name'")
            __props__['data_service_name'] = data_service_name
            if data_sink_id is None and not opts.urn:
                raise TypeError("Missing required property 'data_sink_id'")
            __props__['data_sink_id'] = data_sink_id
            if data_source_id is None and not opts.urn:
                raise TypeError("Missing required property 'data_source_id'")
            __props__['data_source_id'] = data_source_id
            if job_definition_name is None and not opts.urn:
                raise TypeError("Missing required property 'job_definition_name'")
            __props__['job_definition_name'] = job_definition_name
            __props__['last_modified_time'] = last_modified_time
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['run_location'] = run_location
            __props__['schedules'] = schedules
            if state is None and not opts.urn:
                raise TypeError("Missing required property 'state'")
            __props__['state'] = state
            __props__['user_confirmation'] = user_confirmation
            __props__['name'] = None
            __props__['type'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:hybriddata/latest:JobDefinition"), pulumi.Alias(type_="azure-nextgen:hybriddata/v20160601:JobDefinition")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(JobDefinition, __self__).__init__(
            'azure-nextgen:hybriddata/v20190601:JobDefinition',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'JobDefinition':
        """
        Get an existing JobDefinition resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return JobDefinition(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="customerSecrets")
    def customer_secrets(self) -> pulumi.Output[Optional[Sequence['outputs.CustomerSecretResponse']]]:
        """
        List of customer secrets containing a key identifier and key value. The key identifier is a way for the specific data source to understand the key. Value contains customer secret encrypted by the encryptionKeys.
        """
        return pulumi.get(self, "customer_secrets")

    @property
    @pulumi.getter(name="dataServiceInput")
    def data_service_input(self) -> pulumi.Output[Optional[Any]]:
        """
        A generic json used differently by each data service type.
        """
        return pulumi.get(self, "data_service_input")

    @property
    @pulumi.getter(name="dataSinkId")
    def data_sink_id(self) -> pulumi.Output[str]:
        """
        Data Sink Id associated to the job definition.
        """
        return pulumi.get(self, "data_sink_id")

    @property
    @pulumi.getter(name="dataSourceId")
    def data_source_id(self) -> pulumi.Output[str]:
        """
        Data Source Id associated to the job definition.
        """
        return pulumi.get(self, "data_source_id")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[Optional[str]]:
        """
        Last modified time of the job definition.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the object.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="runLocation")
    def run_location(self) -> pulumi.Output[Optional[str]]:
        """
        This is the preferred geo location for the job to run.
        """
        return pulumi.get(self, "run_location")

    @property
    @pulumi.getter
    def schedules(self) -> pulumi.Output[Optional[Sequence['outputs.ScheduleResponse']]]:
        """
        Schedule for running the job definition
        """
        return pulumi.get(self, "schedules")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        State of the job definition.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the object.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userConfirmation")
    def user_confirmation(self) -> pulumi.Output[Optional[str]]:
        """
        Enum to detect if user confirmation is required. If not passed will default to NotRequired.
        """
        return pulumi.get(self, "user_confirmation")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

