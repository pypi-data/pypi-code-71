# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['Workflow']


class Workflow(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_run_properties: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 max_concurrent_runs: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Glue Workflow resource.
        The workflow graph (DAG) can be build using the `glue.Trigger` resource.
        See the example below for creating a graph with four nodes (two triggers and two jobs).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.glue.Workflow("example")
        example_start = aws.glue.Trigger("example-start",
            type="ON_DEMAND",
            workflow_name=example.name,
            actions=[aws.glue.TriggerActionArgs(
                job_name="example-job",
            )])
        example_inner = aws.glue.Trigger("example-inner",
            type="CONDITIONAL",
            workflow_name=example.name,
            predicate=aws.glue.TriggerPredicateArgs(
                conditions=[aws.glue.TriggerPredicateConditionArgs(
                    job_name="example-job",
                    state="SUCCEEDED",
                )],
            ),
            actions=[aws.glue.TriggerActionArgs(
                job_name="another-example-job",
            )])
        ```

        ## Import

        Glue Workflows can be imported using `name`, e.g.

        ```sh
         $ pulumi import aws:glue/workflow:Workflow MyWorkflow MyWorkflow
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, Any]] default_run_properties: A map of default run properties for this workflow. These properties are passed to all jobs associated to the workflow.
        :param pulumi.Input[str] description: Description of the workflow.
        :param pulumi.Input[int] max_concurrent_runs: Prevents exceeding the maximum number of concurrent runs of any of the component jobs. If you leave this parameter blank, there is no limit to the number of concurrent workflow runs.
        :param pulumi.Input[str] name: The name you assign to this workflow.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags
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

            __props__['default_run_properties'] = default_run_properties
            __props__['description'] = description
            __props__['max_concurrent_runs'] = max_concurrent_runs
            __props__['name'] = name
            __props__['tags'] = tags
            __props__['arn'] = None
        super(Workflow, __self__).__init__(
            'aws:glue/workflow:Workflow',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            default_run_properties: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            max_concurrent_runs: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'Workflow':
        """
        Get an existing Workflow resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of Glue Workflow
        :param pulumi.Input[Mapping[str, Any]] default_run_properties: A map of default run properties for this workflow. These properties are passed to all jobs associated to the workflow.
        :param pulumi.Input[str] description: Description of the workflow.
        :param pulumi.Input[int] max_concurrent_runs: Prevents exceeding the maximum number of concurrent runs of any of the component jobs. If you leave this parameter blank, there is no limit to the number of concurrent workflow runs.
        :param pulumi.Input[str] name: The name you assign to this workflow.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["default_run_properties"] = default_run_properties
        __props__["description"] = description
        __props__["max_concurrent_runs"] = max_concurrent_runs
        __props__["name"] = name
        __props__["tags"] = tags
        return Workflow(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) of Glue Workflow
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="defaultRunProperties")
    def default_run_properties(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        A map of default run properties for this workflow. These properties are passed to all jobs associated to the workflow.
        """
        return pulumi.get(self, "default_run_properties")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the workflow.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="maxConcurrentRuns")
    def max_concurrent_runs(self) -> pulumi.Output[Optional[int]]:
        """
        Prevents exceeding the maximum number of concurrent runs of any of the component jobs. If you leave this parameter blank, there is no limit to the number of concurrent workflow runs.
        """
        return pulumi.get(self, "max_concurrent_runs")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name you assign to this workflow.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value map of resource tags
        """
        return pulumi.get(self, "tags")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

