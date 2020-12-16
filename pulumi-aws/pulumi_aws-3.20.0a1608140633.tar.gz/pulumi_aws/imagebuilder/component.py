# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['Component']


class Component(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 change_description: Optional[pulumi.Input[str]] = None,
                 data: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 platform: Optional[pulumi.Input[str]] = None,
                 supported_os_versions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 uri: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages an Image Builder Component.

        ## Example Usage
        ### URI Document

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.imagebuilder.Component("example",
            platform="Linux",
            uri=f"s3://{aws_s3_bucket_object['example']['bucket']}/{aws_s3_bucket_object['example']['key']}",
            version="1.0.0")
        ```

        ## Import

        `aws_imagebuilder_components` resources can be imported by using the Amazon Resource Name (ARN), e.g.

        ```sh
         $ pulumi import aws:imagebuilder/component:Component example arn:aws:imagebuilder:us-east-1:123456789012:component/example/1.0.0/1
        ```

         Certain resource arguments, such as `uri`, cannot be read via the API and imported into Terraform. Terraform will display a difference for these arguments the first run after import if declared in the Terraform configuration for an imported resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] change_description: Change description of the component.
        :param pulumi.Input[str] description: Description of the component.
        :param pulumi.Input[str] kms_key_id: Amazon Resource Name (ARN) of the Key Management Service (KMS) Key used to encrypt the component.
        :param pulumi.Input[str] name: Name of the component.
        :param pulumi.Input[str] platform: Platform of the component.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] supported_os_versions: Set of Operating Systems (OS) supported by the component.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags for the component.
        :param pulumi.Input[str] uri: S3 URI with data of the component. Exactly one of `data` and `uri` can be specified.
        :param pulumi.Input[str] version: Version of the component.
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

            __props__['change_description'] = change_description
            __props__['data'] = data
            __props__['description'] = description
            __props__['kms_key_id'] = kms_key_id
            __props__['name'] = name
            if platform is None and not opts.urn:
                raise TypeError("Missing required property 'platform'")
            __props__['platform'] = platform
            __props__['supported_os_versions'] = supported_os_versions
            __props__['tags'] = tags
            __props__['uri'] = uri
            if version is None and not opts.urn:
                raise TypeError("Missing required property 'version'")
            __props__['version'] = version
            __props__['arn'] = None
            __props__['date_created'] = None
            __props__['encrypted'] = None
            __props__['owner'] = None
            __props__['type'] = None
        super(Component, __self__).__init__(
            'aws:imagebuilder/component:Component',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            change_description: Optional[pulumi.Input[str]] = None,
            data: Optional[pulumi.Input[str]] = None,
            date_created: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            encrypted: Optional[pulumi.Input[bool]] = None,
            kms_key_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            owner: Optional[pulumi.Input[str]] = None,
            platform: Optional[pulumi.Input[str]] = None,
            supported_os_versions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            type: Optional[pulumi.Input[str]] = None,
            uri: Optional[pulumi.Input[str]] = None,
            version: Optional[pulumi.Input[str]] = None) -> 'Component':
        """
        Get an existing Component resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: (Required) Amazon Resource Name (ARN) of the component.
        :param pulumi.Input[str] change_description: Change description of the component.
        :param pulumi.Input[str] date_created: Date the component was created.
        :param pulumi.Input[str] description: Description of the component.
        :param pulumi.Input[bool] encrypted: Encryption status of the component.
        :param pulumi.Input[str] kms_key_id: Amazon Resource Name (ARN) of the Key Management Service (KMS) Key used to encrypt the component.
        :param pulumi.Input[str] name: Name of the component.
        :param pulumi.Input[str] owner: Owner of the component.
        :param pulumi.Input[str] platform: Platform of the component.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] supported_os_versions: Set of Operating Systems (OS) supported by the component.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags for the component.
        :param pulumi.Input[str] type: Type of the component.
        :param pulumi.Input[str] uri: S3 URI with data of the component. Exactly one of `data` and `uri` can be specified.
        :param pulumi.Input[str] version: Version of the component.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["change_description"] = change_description
        __props__["data"] = data
        __props__["date_created"] = date_created
        __props__["description"] = description
        __props__["encrypted"] = encrypted
        __props__["kms_key_id"] = kms_key_id
        __props__["name"] = name
        __props__["owner"] = owner
        __props__["platform"] = platform
        __props__["supported_os_versions"] = supported_os_versions
        __props__["tags"] = tags
        __props__["type"] = type
        __props__["uri"] = uri
        __props__["version"] = version
        return Component(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        (Required) Amazon Resource Name (ARN) of the component.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="changeDescription")
    def change_description(self) -> pulumi.Output[Optional[str]]:
        """
        Change description of the component.
        """
        return pulumi.get(self, "change_description")

    @property
    @pulumi.getter
    def data(self) -> pulumi.Output[str]:
        return pulumi.get(self, "data")

    @property
    @pulumi.getter(name="dateCreated")
    def date_created(self) -> pulumi.Output[str]:
        """
        Date the component was created.
        """
        return pulumi.get(self, "date_created")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the component.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def encrypted(self) -> pulumi.Output[bool]:
        """
        Encryption status of the component.
        """
        return pulumi.get(self, "encrypted")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[Optional[str]]:
        """
        Amazon Resource Name (ARN) of the Key Management Service (KMS) Key used to encrypt the component.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the component.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Output[str]:
        """
        Owner of the component.
        """
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter
    def platform(self) -> pulumi.Output[str]:
        """
        Platform of the component.
        """
        return pulumi.get(self, "platform")

    @property
    @pulumi.getter(name="supportedOsVersions")
    def supported_os_versions(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Set of Operating Systems (OS) supported by the component.
        """
        return pulumi.get(self, "supported_os_versions")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value map of resource tags for the component.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the component.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def uri(self) -> pulumi.Output[Optional[str]]:
        """
        S3 URI with data of the component. Exactly one of `data` and `uri` can be specified.
        """
        return pulumi.get(self, "uri")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        Version of the component.
        """
        return pulumi.get(self, "version")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

