# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .get_authorization_token import *
from .get_credentials import *
from .get_image import *
from .get_repository import *
from .lifecycle_policy import *
from .repository import *
from .repository_policy import *
from ._inputs import *
from . import outputs

def _register_module():
    import pulumi
    from .. import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "aws:ecr/lifecyclePolicy:LifecyclePolicy":
                return LifecyclePolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:ecr/repository:Repository":
                return Repository(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:ecr/repositoryPolicy:RepositoryPolicy":
                return RepositoryPolicy(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("aws", "ecr/lifecyclePolicy", _module_instance)
    pulumi.runtime.register_resource_module("aws", "ecr/repository", _module_instance)
    pulumi.runtime.register_resource_module("aws", "ecr/repositoryPolicy", _module_instance)

_register_module()
