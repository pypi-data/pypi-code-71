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
    'GetAssignmentResult',
    'AwaitableGetAssignmentResult',
    'get_assignment',
]

@pulumi.output_type
class GetAssignmentResult:
    """
    Represents a Blueprint assignment.
    """
    def __init__(__self__, blueprint_id=None, description=None, display_name=None, id=None, identity=None, location=None, locks=None, name=None, parameters=None, provisioning_state=None, resource_groups=None, status=None, type=None):
        if blueprint_id and not isinstance(blueprint_id, str):
            raise TypeError("Expected argument 'blueprint_id' to be a str")
        pulumi.set(__self__, "blueprint_id", blueprint_id)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if locks and not isinstance(locks, dict):
            raise TypeError("Expected argument 'locks' to be a dict")
        pulumi.set(__self__, "locks", locks)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if parameters and not isinstance(parameters, dict):
            raise TypeError("Expected argument 'parameters' to be a dict")
        pulumi.set(__self__, "parameters", parameters)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if resource_groups and not isinstance(resource_groups, dict):
            raise TypeError("Expected argument 'resource_groups' to be a dict")
        pulumi.set(__self__, "resource_groups", resource_groups)
        if status and not isinstance(status, dict):
            raise TypeError("Expected argument 'status' to be a dict")
        pulumi.set(__self__, "status", status)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="blueprintId")
    def blueprint_id(self) -> Optional[str]:
        """
        ID of the Blueprint definition resource.
        """
        return pulumi.get(self, "blueprint_id")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Multi-line explain this resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        One-liner string explain this resource.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        String Id used to locate any resource on Azure.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> 'outputs.ManagedServiceIdentityResponse':
        """
        Managed Service Identity for this Blueprint assignment
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The location of this Blueprint assignment.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def locks(self) -> Optional['outputs.AssignmentLockSettingsResponse']:
        """
        Defines how Blueprint-managed resources will be locked.
        """
        return pulumi.get(self, "locks")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of this resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> Mapping[str, 'outputs.ParameterValueBaseResponse']:
        """
        Blueprint parameter values.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        State of the assignment.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceGroups")
    def resource_groups(self) -> Mapping[str, 'outputs.ResourceGroupValueResponse']:
        """
        Names and locations of resource group placeholders.
        """
        return pulumi.get(self, "resource_groups")

    @property
    @pulumi.getter
    def status(self) -> 'outputs.AssignmentStatusResponse':
        """
        Status of Blueprint assignment. This field is readonly.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of this resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetAssignmentResult(GetAssignmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAssignmentResult(
            blueprint_id=self.blueprint_id,
            description=self.description,
            display_name=self.display_name,
            id=self.id,
            identity=self.identity,
            location=self.location,
            locks=self.locks,
            name=self.name,
            parameters=self.parameters,
            provisioning_state=self.provisioning_state,
            resource_groups=self.resource_groups,
            status=self.status,
            type=self.type)


def get_assignment(assignment_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAssignmentResult:
    """
    Use this data source to access information about an existing resource.

    :param str assignment_name: name of the assignment.
    """
    __args__ = dict()
    __args__['assignmentName'] = assignment_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-nextgen:blueprint/v20171111preview:getAssignment', __args__, opts=opts, typ=GetAssignmentResult).value

    return AwaitableGetAssignmentResult(
        blueprint_id=__ret__.blueprint_id,
        description=__ret__.description,
        display_name=__ret__.display_name,
        id=__ret__.id,
        identity=__ret__.identity,
        location=__ret__.location,
        locks=__ret__.locks,
        name=__ret__.name,
        parameters=__ret__.parameters,
        provisioning_state=__ret__.provisioning_state,
        resource_groups=__ret__.resource_groups,
        status=__ret__.status,
        type=__ret__.type)
