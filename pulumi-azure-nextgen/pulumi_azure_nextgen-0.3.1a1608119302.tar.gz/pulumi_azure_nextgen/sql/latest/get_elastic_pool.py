# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables

__all__ = [
    'GetElasticPoolResult',
    'AwaitableGetElasticPoolResult',
    'get_elastic_pool',
]

@pulumi.output_type
class GetElasticPoolResult:
    """
    Represents a database elastic pool.
    """
    def __init__(__self__, creation_date=None, database_dtu_max=None, database_dtu_min=None, dtu=None, edition=None, id=None, kind=None, location=None, name=None, state=None, storage_mb=None, tags=None, type=None, zone_redundant=None):
        if creation_date and not isinstance(creation_date, str):
            raise TypeError("Expected argument 'creation_date' to be a str")
        pulumi.set(__self__, "creation_date", creation_date)
        if database_dtu_max and not isinstance(database_dtu_max, int):
            raise TypeError("Expected argument 'database_dtu_max' to be a int")
        pulumi.set(__self__, "database_dtu_max", database_dtu_max)
        if database_dtu_min and not isinstance(database_dtu_min, int):
            raise TypeError("Expected argument 'database_dtu_min' to be a int")
        pulumi.set(__self__, "database_dtu_min", database_dtu_min)
        if dtu and not isinstance(dtu, int):
            raise TypeError("Expected argument 'dtu' to be a int")
        pulumi.set(__self__, "dtu", dtu)
        if edition and not isinstance(edition, str):
            raise TypeError("Expected argument 'edition' to be a str")
        pulumi.set(__self__, "edition", edition)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if storage_mb and not isinstance(storage_mb, int):
            raise TypeError("Expected argument 'storage_mb' to be a int")
        pulumi.set(__self__, "storage_mb", storage_mb)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if zone_redundant and not isinstance(zone_redundant, bool):
            raise TypeError("Expected argument 'zone_redundant' to be a bool")
        pulumi.set(__self__, "zone_redundant", zone_redundant)

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> str:
        """
        The creation date of the elastic pool (ISO8601 format).
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter(name="databaseDtuMax")
    def database_dtu_max(self) -> Optional[int]:
        """
        The maximum DTU any one database can consume.
        """
        return pulumi.get(self, "database_dtu_max")

    @property
    @pulumi.getter(name="databaseDtuMin")
    def database_dtu_min(self) -> Optional[int]:
        """
        The minimum DTU all databases are guaranteed.
        """
        return pulumi.get(self, "database_dtu_min")

    @property
    @pulumi.getter
    def dtu(self) -> Optional[int]:
        """
        The total shared DTU for the database elastic pool.
        """
        return pulumi.get(self, "dtu")

    @property
    @pulumi.getter
    def edition(self) -> Optional[str]:
        """
        The edition of the elastic pool.
        """
        return pulumi.get(self, "edition")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Kind of elastic pool.  This is metadata used for the Azure portal experience.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The state of the elastic pool.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="storageMB")
    def storage_mb(self) -> Optional[int]:
        """
        Gets storage limit for the database elastic pool in MB.
        """
        return pulumi.get(self, "storage_mb")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> Optional[bool]:
        """
        Whether or not this database elastic pool is zone redundant, which means the replicas of this database will be spread across multiple availability zones.
        """
        return pulumi.get(self, "zone_redundant")


class AwaitableGetElasticPoolResult(GetElasticPoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetElasticPoolResult(
            creation_date=self.creation_date,
            database_dtu_max=self.database_dtu_max,
            database_dtu_min=self.database_dtu_min,
            dtu=self.dtu,
            edition=self.edition,
            id=self.id,
            kind=self.kind,
            location=self.location,
            name=self.name,
            state=self.state,
            storage_mb=self.storage_mb,
            tags=self.tags,
            type=self.type,
            zone_redundant=self.zone_redundant)


def get_elastic_pool(elastic_pool_name: Optional[str] = None,
                     resource_group_name: Optional[str] = None,
                     server_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetElasticPoolResult:
    """
    Use this data source to access information about an existing resource.

    :param str elastic_pool_name: The name of the elastic pool to be retrieved.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    """
    __args__ = dict()
    __args__['elasticPoolName'] = elastic_pool_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverName'] = server_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-nextgen:sql/latest:getElasticPool', __args__, opts=opts, typ=GetElasticPoolResult).value

    return AwaitableGetElasticPoolResult(
        creation_date=__ret__.creation_date,
        database_dtu_max=__ret__.database_dtu_max,
        database_dtu_min=__ret__.database_dtu_min,
        dtu=__ret__.dtu,
        edition=__ret__.edition,
        id=__ret__.id,
        kind=__ret__.kind,
        location=__ret__.location,
        name=__ret__.name,
        state=__ret__.state,
        storage_mb=__ret__.storage_mb,
        tags=__ret__.tags,
        type=__ret__.type,
        zone_redundant=__ret__.zone_redundant)
