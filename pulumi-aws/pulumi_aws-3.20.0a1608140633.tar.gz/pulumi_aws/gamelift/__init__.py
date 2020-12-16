# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .alias import *
from .build import *
from .fleet import *
from .game_session_queue import *
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
            if typ == "aws:gamelift/alias:Alias":
                return Alias(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:gamelift/build:Build":
                return Build(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:gamelift/fleet:Fleet":
                return Fleet(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:gamelift/gameSessionQueue:GameSessionQueue":
                return GameSessionQueue(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("aws", "gamelift/alias", _module_instance)
    pulumi.runtime.register_resource_module("aws", "gamelift/build", _module_instance)
    pulumi.runtime.register_resource_module("aws", "gamelift/fleet", _module_instance)
    pulumi.runtime.register_resource_module("aws", "gamelift/gameSessionQueue", _module_instance)

_register_module()
