# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from ._enums import *
from .attached_database_configuration import *
from .cluster import *
from .cluster_principal_assignment import *
from .data_connection import *
from .database import *
from .database_principal_assignment import *
from .get_attached_database_configuration import *
from .get_cluster import *
from .get_cluster_principal_assignment import *
from .get_data_connection import *
from .get_database import *
from .get_database_principal_assignment import *
from .list_cluster_follower_databases import *
from .list_database_principals import *
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
            if typ == "azure-nextgen:kusto/v20191109:AttachedDatabaseConfiguration":
                return AttachedDatabaseConfiguration(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:kusto/v20191109:Cluster":
                return Cluster(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:kusto/v20191109:ClusterPrincipalAssignment":
                return ClusterPrincipalAssignment(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:kusto/v20191109:DataConnection":
                return DataConnection(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:kusto/v20191109:Database":
                return Database(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:kusto/v20191109:DatabasePrincipalAssignment":
                return DatabasePrincipalAssignment(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure-nextgen", "kusto/v20191109", _module_instance)

_register_module()
