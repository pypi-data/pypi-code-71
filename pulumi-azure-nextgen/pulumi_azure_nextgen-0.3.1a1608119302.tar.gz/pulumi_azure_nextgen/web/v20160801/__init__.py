# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from ._enums import *
from .get_web_app import *
from .get_web_app_deployment import *
from .get_web_app_deployment_slot import *
from .get_web_app_diagnostic_logs_configuration import *
from .get_web_app_domain_ownership_identifier import *
from .get_web_app_domain_ownership_identifier_slot import *
from .get_web_app_function import *
from .get_web_app_host_name_binding import *
from .get_web_app_host_name_binding_slot import *
from .get_web_app_hybrid_connection import *
from .get_web_app_hybrid_connection_slot import *
from .get_web_app_instance_function_slot import *
from .get_web_app_premier_add_on import *
from .get_web_app_premier_add_on_slot import *
from .get_web_app_public_certificate import *
from .get_web_app_public_certificate_slot import *
from .get_web_app_relay_service_connection import *
from .get_web_app_relay_service_connection_slot import *
from .get_web_app_site_extension import *
from .get_web_app_site_extension_slot import *
from .get_web_app_slot import *
from .get_web_app_slot_configuration_names import *
from .get_web_app_source_control import *
from .get_web_app_source_control_slot import *
from .get_web_app_vnet_connection import *
from .get_web_app_vnet_connection_slot import *
from .list_web_app_auth_settings import *
from .list_web_app_auth_settings_slot import *
from .list_web_app_backup_configuration import *
from .list_web_app_backup_configuration_slot import *
from .list_web_app_backup_status_secrets import *
from .list_web_app_backup_status_secrets_slot import *
from .list_web_app_connection_strings import *
from .list_web_app_connection_strings_slot import *
from .list_web_app_function_secrets import *
from .list_web_app_function_secrets_slot import *
from .list_web_app_hybrid_connection_keys import *
from .list_web_app_hybrid_connection_keys_slot import *
from .list_web_app_metadata import *
from .list_web_app_metadata_slot import *
from .list_web_app_publishing_credentials import *
from .list_web_app_publishing_credentials_slot import *
from .list_web_app_site_push_settings import *
from .list_web_app_site_push_settings_slot import *
from .list_web_app_sync_function_triggers import *
from .list_web_app_sync_function_triggers_slot import *
from .list_web_application_settings import *
from .list_web_application_settings_slot import *
from .web_app import *
from .web_app_deployment import *
from .web_app_deployment_slot import *
from .web_app_diagnostic_logs_configuration import *
from .web_app_domain_ownership_identifier import *
from .web_app_domain_ownership_identifier_slot import *
from .web_app_function import *
from .web_app_host_name_binding import *
from .web_app_host_name_binding_slot import *
from .web_app_hybrid_connection import *
from .web_app_hybrid_connection_slot import *
from .web_app_instance_function_slot import *
from .web_app_premier_add_on import *
from .web_app_premier_add_on_slot import *
from .web_app_public_certificate import *
from .web_app_public_certificate_slot import *
from .web_app_relay_service_connection import *
from .web_app_relay_service_connection_slot import *
from .web_app_site_extension import *
from .web_app_site_extension_slot import *
from .web_app_slot import *
from .web_app_slot_configuration_names import *
from .web_app_source_control import *
from .web_app_source_control_slot import *
from .web_app_vnet_connection import *
from .web_app_vnet_connection_slot import *
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
            if typ == "azure-nextgen:web/v20160801:WebApp":
                return WebApp(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:web/v20160801:WebAppDeployment":
                return WebAppDeployment(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:web/v20160801:WebAppDeploymentSlot":
                return WebAppDeploymentSlot(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:web/v20160801:WebAppDiagnosticLogsConfiguration":
                return WebAppDiagnosticLogsConfiguration(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:web/v20160801:WebAppDomainOwnershipIdentifier":
                return WebAppDomainOwnershipIdentifier(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:web/v20160801:WebAppDomainOwnershipIdentifierSlot":
                return WebAppDomainOwnershipIdentifierSlot(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:web/v20160801:WebAppFunction":
                return WebAppFunction(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:web/v20160801:WebAppHostNameBinding":
                return WebAppHostNameBinding(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:web/v20160801:WebAppHostNameBindingSlot":
                return WebAppHostNameBindingSlot(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:web/v20160801:WebAppHybridConnection":
                return WebAppHybridConnection(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:web/v20160801:WebAppHybridConnectionSlot":
                return WebAppHybridConnectionSlot(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:web/v20160801:WebAppInstanceFunctionSlot":
                return WebAppInstanceFunctionSlot(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:web/v20160801:WebAppPremierAddOn":
                return WebAppPremierAddOn(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:web/v20160801:WebAppPremierAddOnSlot":
                return WebAppPremierAddOnSlot(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:web/v20160801:WebAppPublicCertificate":
                return WebAppPublicCertificate(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:web/v20160801:WebAppPublicCertificateSlot":
                return WebAppPublicCertificateSlot(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:web/v20160801:WebAppRelayServiceConnection":
                return WebAppRelayServiceConnection(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:web/v20160801:WebAppRelayServiceConnectionSlot":
                return WebAppRelayServiceConnectionSlot(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:web/v20160801:WebAppSiteExtension":
                return WebAppSiteExtension(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:web/v20160801:WebAppSiteExtensionSlot":
                return WebAppSiteExtensionSlot(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:web/v20160801:WebAppSlot":
                return WebAppSlot(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:web/v20160801:WebAppSlotConfigurationNames":
                return WebAppSlotConfigurationNames(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:web/v20160801:WebAppSourceControl":
                return WebAppSourceControl(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:web/v20160801:WebAppSourceControlSlot":
                return WebAppSourceControlSlot(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:web/v20160801:WebAppVnetConnection":
                return WebAppVnetConnection(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-nextgen:web/v20160801:WebAppVnetConnectionSlot":
                return WebAppVnetConnectionSlot(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure-nextgen", "web/v20160801", _module_instance)

_register_module()
