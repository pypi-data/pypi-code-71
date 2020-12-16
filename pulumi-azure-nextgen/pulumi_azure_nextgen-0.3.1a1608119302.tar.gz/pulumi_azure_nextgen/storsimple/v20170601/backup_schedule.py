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

__all__ = ['BackupSchedule']


class BackupSchedule(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backup_policy_name: Optional[pulumi.Input[str]] = None,
                 backup_schedule_name: Optional[pulumi.Input[str]] = None,
                 backup_type: Optional[pulumi.Input['BackupType']] = None,
                 device_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input['Kind']] = None,
                 manager_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 retention_count: Optional[pulumi.Input[int]] = None,
                 schedule_recurrence: Optional[pulumi.Input[pulumi.InputType['ScheduleRecurrenceArgs']]] = None,
                 schedule_status: Optional[pulumi.Input['ScheduleStatus']] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        The backup schedule.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] backup_policy_name: The backup policy name.
        :param pulumi.Input[str] backup_schedule_name: The backup schedule name.
        :param pulumi.Input['BackupType'] backup_type: The type of backup which needs to be taken.
        :param pulumi.Input[str] device_name: The device name
        :param pulumi.Input['Kind'] kind: The Kind of the object. Currently only Series8000 is supported
        :param pulumi.Input[str] manager_name: The manager name
        :param pulumi.Input[str] resource_group_name: The resource group name
        :param pulumi.Input[int] retention_count: The number of backups to be retained.
        :param pulumi.Input[pulumi.InputType['ScheduleRecurrenceArgs']] schedule_recurrence: The schedule recurrence.
        :param pulumi.Input['ScheduleStatus'] schedule_status: The schedule status.
        :param pulumi.Input[str] start_time: The start time of the schedule.
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

            if backup_policy_name is None and not opts.urn:
                raise TypeError("Missing required property 'backup_policy_name'")
            __props__['backup_policy_name'] = backup_policy_name
            if backup_schedule_name is None and not opts.urn:
                raise TypeError("Missing required property 'backup_schedule_name'")
            __props__['backup_schedule_name'] = backup_schedule_name
            if backup_type is None and not opts.urn:
                raise TypeError("Missing required property 'backup_type'")
            __props__['backup_type'] = backup_type
            if device_name is None and not opts.urn:
                raise TypeError("Missing required property 'device_name'")
            __props__['device_name'] = device_name
            __props__['kind'] = kind
            if manager_name is None and not opts.urn:
                raise TypeError("Missing required property 'manager_name'")
            __props__['manager_name'] = manager_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            if retention_count is None and not opts.urn:
                raise TypeError("Missing required property 'retention_count'")
            __props__['retention_count'] = retention_count
            if schedule_recurrence is None and not opts.urn:
                raise TypeError("Missing required property 'schedule_recurrence'")
            __props__['schedule_recurrence'] = schedule_recurrence
            if schedule_status is None and not opts.urn:
                raise TypeError("Missing required property 'schedule_status'")
            __props__['schedule_status'] = schedule_status
            if start_time is None and not opts.urn:
                raise TypeError("Missing required property 'start_time'")
            __props__['start_time'] = start_time
            __props__['last_successful_run'] = None
            __props__['name'] = None
            __props__['type'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:storsimple/latest:BackupSchedule")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(BackupSchedule, __self__).__init__(
            'azure-nextgen:storsimple/v20170601:BackupSchedule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'BackupSchedule':
        """
        Get an existing BackupSchedule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return BackupSchedule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="backupType")
    def backup_type(self) -> pulumi.Output[str]:
        """
        The type of backup which needs to be taken.
        """
        return pulumi.get(self, "backup_type")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        The Kind of the object. Currently only Series8000 is supported
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="lastSuccessfulRun")
    def last_successful_run(self) -> pulumi.Output[str]:
        """
        The last successful backup run which was triggered for the schedule.
        """
        return pulumi.get(self, "last_successful_run")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the object.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="retentionCount")
    def retention_count(self) -> pulumi.Output[int]:
        """
        The number of backups to be retained.
        """
        return pulumi.get(self, "retention_count")

    @property
    @pulumi.getter(name="scheduleRecurrence")
    def schedule_recurrence(self) -> pulumi.Output['outputs.ScheduleRecurrenceResponse']:
        """
        The schedule recurrence.
        """
        return pulumi.get(self, "schedule_recurrence")

    @property
    @pulumi.getter(name="scheduleStatus")
    def schedule_status(self) -> pulumi.Output[str]:
        """
        The schedule status.
        """
        return pulumi.get(self, "schedule_status")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Output[str]:
        """
        The start time of the schedule.
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The hierarchical type of the object.
        """
        return pulumi.get(self, "type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

