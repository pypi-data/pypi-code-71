# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from ._enums import *
from .access_policy import *
from .environment import *
from .event_source import *
from .get_access_policy import *
from .get_environment import *
from .get_event_source import *
from .get_reference_data_set import *
from .reference_data_set import *
from ._inputs import *
from . import outputs

def _register_module():
    import pulumi
    from ... import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "azure-nextgen:timeseriesinsights/latest:AccessPolicy":
                return AccessPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:timeseriesinsights/latest:Environment":
                return Environment(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:timeseriesinsights/latest:EventSource":
                return EventSource(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:timeseriesinsights/latest:ReferenceDataSet":
                return ReferenceDataSet(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure-nextgen", "timeseriesinsights/latest", _module_instance)

_register_module()
