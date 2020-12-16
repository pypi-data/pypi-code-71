# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables

__all__ = [
    'ListConfigurationStoreKeyValueResult',
    'AwaitableListConfigurationStoreKeyValueResult',
    'list_configuration_store_key_value',
]

@pulumi.output_type
class ListConfigurationStoreKeyValueResult:
    """
    The result of a request to retrieve a key-value from the specified configuration store.
    """
    def __init__(__self__, content_type=None, e_tag=None, key=None, label=None, last_modified=None, locked=None, tags=None, value=None):
        if content_type and not isinstance(content_type, str):
            raise TypeError("Expected argument 'content_type' to be a str")
        pulumi.set(__self__, "content_type", content_type)
        if e_tag and not isinstance(e_tag, str):
            raise TypeError("Expected argument 'e_tag' to be a str")
        pulumi.set(__self__, "e_tag", e_tag)
        if key and not isinstance(key, str):
            raise TypeError("Expected argument 'key' to be a str")
        pulumi.set(__self__, "key", key)
        if label and not isinstance(label, str):
            raise TypeError("Expected argument 'label' to be a str")
        pulumi.set(__self__, "label", label)
        if last_modified and not isinstance(last_modified, str):
            raise TypeError("Expected argument 'last_modified' to be a str")
        pulumi.set(__self__, "last_modified", last_modified)
        if locked and not isinstance(locked, bool):
            raise TypeError("Expected argument 'locked' to be a bool")
        pulumi.set(__self__, "locked", locked)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if value and not isinstance(value, str):
            raise TypeError("Expected argument 'value' to be a str")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> str:
        """
        The content type of the key-value's value.
        Providing a proper content-type can enable transformations of values when they are retrieved by applications.
        """
        return pulumi.get(self, "content_type")

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> str:
        """
        An ETag indicating the state of a key-value within a configuration store.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The primary identifier of a key-value.
        The key is used in unison with the label to uniquely identify a key-value.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def label(self) -> str:
        """
        A value used to group key-values.
        The label is used in unison with the key to uniquely identify a key-value.
        """
        return pulumi.get(self, "label")

    @property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> str:
        """
        The last time a modifying operation was performed on the given key-value.
        """
        return pulumi.get(self, "last_modified")

    @property
    @pulumi.getter
    def locked(self) -> bool:
        """
        A value indicating whether the key-value is locked.
        A locked key-value may not be modified until it is unlocked.
        """
        return pulumi.get(self, "locked")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        A dictionary of tags that can help identify what a key-value may be applicable for.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value of the key-value.
        """
        return pulumi.get(self, "value")


class AwaitableListConfigurationStoreKeyValueResult(ListConfigurationStoreKeyValueResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListConfigurationStoreKeyValueResult(
            content_type=self.content_type,
            e_tag=self.e_tag,
            key=self.key,
            label=self.label,
            last_modified=self.last_modified,
            locked=self.locked,
            tags=self.tags,
            value=self.value)


def list_configuration_store_key_value(config_store_name: Optional[str] = None,
                                       key: Optional[str] = None,
                                       label: Optional[str] = None,
                                       resource_group_name: Optional[str] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListConfigurationStoreKeyValueResult:
    """
    Use this data source to access information about an existing resource.

    :param str config_store_name: The name of the configuration store.
    :param str key: The key to retrieve.
    :param str label: The label of the key.
    :param str resource_group_name: The name of the resource group to which the container registry belongs.
    """
    __args__ = dict()
    __args__['configStoreName'] = config_store_name
    __args__['key'] = key
    __args__['label'] = label
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-nextgen:appconfiguration/v20191101preview:listConfigurationStoreKeyValue', __args__, opts=opts, typ=ListConfigurationStoreKeyValueResult).value

    return AwaitableListConfigurationStoreKeyValueResult(
        content_type=__ret__.content_type,
        e_tag=__ret__.e_tag,
        key=__ret__.key,
        label=__ret__.label,
        last_modified=__ret__.last_modified,
        locked=__ret__.locked,
        tags=__ret__.tags,
        value=__ret__.value)
