# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from ._enums import *
from .certificate import *
from .dps_certificate import *
from .get_certificate import *
from .get_dps_certificate import *
from .get_iot_dps_resource import *
from .get_iot_dps_resource_private_endpoint_connection import *
from .get_iot_hub_resource import *
from .get_iot_hub_resource_event_hub_consumer_group import *
from .get_private_endpoint_connection import *
from .iot_dps_resource import *
from .iot_dps_resource_private_endpoint_connection import *
from .iot_hub_resource import *
from .iot_hub_resource_event_hub_consumer_group import *
from .list_iot_dps_resource_keys import *
from .list_iot_dps_resource_keys_for_key_name import *
from .list_iot_hub_resource_keys import *
from .list_iot_hub_resource_keys_for_key_name import *
from .private_endpoint_connection import *
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
            if typ == "azure-nextgen:devices/latest:Certificate":
                return Certificate(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:devices/latest:DpsCertificate":
                return DpsCertificate(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:devices/latest:IotDpsResource":
                return IotDpsResource(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:devices/latest:IotDpsResourcePrivateEndpointConnection":
                return IotDpsResourcePrivateEndpointConnection(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:devices/latest:IotHubResource":
                return IotHubResource(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:devices/latest:IotHubResourceEventHubConsumerGroup":
                return IotHubResourceEventHubConsumerGroup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:devices/latest:PrivateEndpointConnection":
                return PrivateEndpointConnection(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure-nextgen", "devices/latest", _module_instance)

_register_module()
