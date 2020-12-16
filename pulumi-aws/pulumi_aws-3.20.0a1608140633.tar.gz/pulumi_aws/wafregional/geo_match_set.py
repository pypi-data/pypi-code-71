# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['GeoMatchSet']


class GeoMatchSet(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 geo_match_constraints: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GeoMatchSetGeoMatchConstraintArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a WAF Regional Geo Match Set Resource

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        geo_match_set = aws.wafregional.GeoMatchSet("geoMatchSet", geo_match_constraints=[
            aws.wafregional.GeoMatchSetGeoMatchConstraintArgs(
                type="Country",
                value="US",
            ),
            aws.wafregional.GeoMatchSetGeoMatchConstraintArgs(
                type="Country",
                value="CA",
            ),
        ])
        ```

        ## Import

        WAF Regional Geo Match Set can be imported using the id, e.g.

        ```sh
         $ pulumi import aws:wafregional/geoMatchSet:GeoMatchSet geo_match_set a1b2c3d4-d5f6-7777-8888-9999aaaabbbbcccc
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GeoMatchSetGeoMatchConstraintArgs']]]] geo_match_constraints: The Geo Match Constraint objects which contain the country that you want AWS WAF to search for.
        :param pulumi.Input[str] name: The name or description of the Geo Match Set.
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

            __props__['geo_match_constraints'] = geo_match_constraints
            __props__['name'] = name
        super(GeoMatchSet, __self__).__init__(
            'aws:wafregional/geoMatchSet:GeoMatchSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            geo_match_constraints: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GeoMatchSetGeoMatchConstraintArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'GeoMatchSet':
        """
        Get an existing GeoMatchSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GeoMatchSetGeoMatchConstraintArgs']]]] geo_match_constraints: The Geo Match Constraint objects which contain the country that you want AWS WAF to search for.
        :param pulumi.Input[str] name: The name or description of the Geo Match Set.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["geo_match_constraints"] = geo_match_constraints
        __props__["name"] = name
        return GeoMatchSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="geoMatchConstraints")
    def geo_match_constraints(self) -> pulumi.Output[Optional[Sequence['outputs.GeoMatchSetGeoMatchConstraint']]]:
        """
        The Geo Match Constraint objects which contain the country that you want AWS WAF to search for.
        """
        return pulumi.get(self, "geo_match_constraints")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name or description of the Geo Match Set.
        """
        return pulumi.get(self, "name")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

