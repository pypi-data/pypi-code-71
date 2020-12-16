# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from ._enums import *
from .agent_pool import *
from .get_agent_pool import *
from .get_task import *
from .get_task_run import *
from .list_agent_pool_queue_status import *
from .list_registry_build_source_upload_url import *
from .list_run_log_sas_url import *
from .list_task_details import *
from .list_task_run_details import *
from .task import *
from .task_run import *
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
            if typ == "azure-nextgen:containerregistry/v20190601preview:AgentPool":
                return AgentPool(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:containerregistry/v20190601preview:Task":
                return Task(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:containerregistry/v20190601preview:TaskRun":
                return TaskRun(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure-nextgen", "containerregistry/v20190601preview", _module_instance)

_register_module()
