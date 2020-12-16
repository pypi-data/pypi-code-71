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

__all__ = ['Distribution']


class Distribution(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aliases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 custom_error_responses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DistributionCustomErrorResponseArgs']]]]] = None,
                 default_cache_behavior: Optional[pulumi.Input[pulumi.InputType['DistributionDefaultCacheBehaviorArgs']]] = None,
                 default_root_object: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 http_version: Optional[pulumi.Input[str]] = None,
                 is_ipv6_enabled: Optional[pulumi.Input[bool]] = None,
                 logging_config: Optional[pulumi.Input[pulumi.InputType['DistributionLoggingConfigArgs']]] = None,
                 ordered_cache_behaviors: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DistributionOrderedCacheBehaviorArgs']]]]] = None,
                 origin_groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DistributionOriginGroupArgs']]]]] = None,
                 origins: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DistributionOriginArgs']]]]] = None,
                 price_class: Optional[pulumi.Input[str]] = None,
                 restrictions: Optional[pulumi.Input[pulumi.InputType['DistributionRestrictionsArgs']]] = None,
                 retain_on_delete: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 viewer_certificate: Optional[pulumi.Input[pulumi.InputType['DistributionViewerCertificateArgs']]] = None,
                 wait_for_deployment: Optional[pulumi.Input[bool]] = None,
                 web_acl_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates an Amazon CloudFront web distribution.

        For information about CloudFront distributions, see the
        [Amazon CloudFront Developer Guide](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html). For specific information about creating
        CloudFront web distributions, see the [POST Distribution](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateDistribution.html) page in the Amazon
        CloudFront API Reference.

        > **NOTE:** CloudFront distributions take about 15 minutes to a deployed state
        after creation or modification. During this time, deletes to resources will be
        blocked. If you need to delete a distribution that is enabled and you do not
        want to wait, you need to use the `retain_on_delete` flag.

        ## Example Usage

        The following example below creates a CloudFront distribution with an S3 origin.

        ```python
        import pulumi
        import pulumi_aws as aws

        bucket = aws.s3.Bucket("bucket",
            acl="private",
            tags={
                "Name": "My bucket",
            })
        s3_origin_id = "myS3Origin"
        s3_distribution = aws.cloudfront.Distribution("s3Distribution",
            origins=[aws.cloudfront.DistributionOriginArgs(
                domain_name=bucket.bucket_regional_domain_name,
                origin_id=s3_origin_id,
                s3_origin_config=aws.cloudfront.DistributionOriginS3OriginConfigArgs(
                    origin_access_identity="origin-access-identity/cloudfront/ABCDEFG1234567",
                ),
            )],
            enabled=True,
            is_ipv6_enabled=True,
            comment="Some comment",
            default_root_object="index.html",
            logging_config=aws.cloudfront.DistributionLoggingConfigArgs(
                include_cookies=False,
                bucket="mylogs.s3.amazonaws.com",
                prefix="myprefix",
            ),
            aliases=[
                "mysite.example.com",
                "yoursite.example.com",
            ],
            default_cache_behavior=aws.cloudfront.DistributionDefaultCacheBehaviorArgs(
                allowed_methods=[
                    "DELETE",
                    "GET",
                    "HEAD",
                    "OPTIONS",
                    "PATCH",
                    "POST",
                    "PUT",
                ],
                cached_methods=[
                    "GET",
                    "HEAD",
                ],
                target_origin_id=s3_origin_id,
                forwarded_values=aws.cloudfront.DistributionDefaultCacheBehaviorForwardedValuesArgs(
                    query_string=False,
                    cookies=aws.cloudfront.DistributionDefaultCacheBehaviorForwardedValuesCookiesArgs(
                        forward="none",
                    ),
                ),
                viewer_protocol_policy="allow-all",
                min_ttl=0,
                default_ttl=3600,
                max_ttl=86400,
            ),
            ordered_cache_behaviors=[
                aws.cloudfront.DistributionOrderedCacheBehaviorArgs(
                    path_pattern="/content/immutable/*",
                    allowed_methods=[
                        "GET",
                        "HEAD",
                        "OPTIONS",
                    ],
                    cached_methods=[
                        "GET",
                        "HEAD",
                        "OPTIONS",
                    ],
                    target_origin_id=s3_origin_id,
                    forwarded_values=aws.cloudfront.DistributionOrderedCacheBehaviorForwardedValuesArgs(
                        query_string=False,
                        headers=["Origin"],
                        cookies=aws.cloudfront.DistributionOrderedCacheBehaviorForwardedValuesCookiesArgs(
                            forward="none",
                        ),
                    ),
                    min_ttl=0,
                    default_ttl=86400,
                    max_ttl=31536000,
                    compress=True,
                    viewer_protocol_policy="redirect-to-https",
                ),
                aws.cloudfront.DistributionOrderedCacheBehaviorArgs(
                    path_pattern="/content/*",
                    allowed_methods=[
                        "GET",
                        "HEAD",
                        "OPTIONS",
                    ],
                    cached_methods=[
                        "GET",
                        "HEAD",
                    ],
                    target_origin_id=s3_origin_id,
                    forwarded_values=aws.cloudfront.DistributionOrderedCacheBehaviorForwardedValuesArgs(
                        query_string=False,
                        cookies=aws.cloudfront.DistributionOrderedCacheBehaviorForwardedValuesCookiesArgs(
                            forward="none",
                        ),
                    ),
                    min_ttl=0,
                    default_ttl=3600,
                    max_ttl=86400,
                    compress=True,
                    viewer_protocol_policy="redirect-to-https",
                ),
            ],
            price_class="PriceClass_200",
            restrictions=aws.cloudfront.DistributionRestrictionsArgs(
                geo_restriction=aws.cloudfront.DistributionRestrictionsGeoRestrictionArgs(
                    restriction_type="whitelist",
                    locations=[
                        "US",
                        "CA",
                        "GB",
                        "DE",
                    ],
                ),
            ),
            tags={
                "Environment": "production",
            },
            viewer_certificate=aws.cloudfront.DistributionViewerCertificateArgs(
                cloudfront_default_certificate=True,
            ))
        ```

        The following example below creates a Cloudfront distribution with an origin group for failover routing:

        ```python
        import pulumi
        import pulumi_aws as aws

        s3_distribution = aws.cloudfront.Distribution("s3Distribution",
            origin_groups=[aws.cloudfront.DistributionOriginGroupArgs(
                origin_id="groupS3",
                failover_criteria=aws.cloudfront.DistributionOriginGroupFailoverCriteriaArgs(
                    status_codes=[
                        403,
                        404,
                        500,
                        502,
                    ],
                ),
                members=[
                    aws.cloudfront.DistributionOriginGroupMemberArgs(
                        origin_id="primaryS3",
                    ),
                    aws.cloudfront.DistributionOriginGroupMemberArgs(
                        origin_id="failoverS3",
                    ),
                ],
            )],
            origins=[
                aws.cloudfront.DistributionOriginArgs(
                    domain_name=aws_s3_bucket["primary"]["bucket_regional_domain_name"],
                    origin_id="primaryS3",
                    s3_origin_config=aws.cloudfront.DistributionOriginS3OriginConfigArgs(
                        origin_access_identity=aws_cloudfront_origin_access_identity["default"]["cloudfront_access_identity_path"],
                    ),
                ),
                aws.cloudfront.DistributionOriginArgs(
                    domain_name=aws_s3_bucket["failover"]["bucket_regional_domain_name"],
                    origin_id="failoverS3",
                    s3_origin_config=aws.cloudfront.DistributionOriginS3OriginConfigArgs(
                        origin_access_identity=aws_cloudfront_origin_access_identity["default"]["cloudfront_access_identity_path"],
                    ),
                ),
            ],
            default_cache_behavior=aws.cloudfront.DistributionDefaultCacheBehaviorArgs(
                target_origin_id="groupS3",
            ))
        # ... other configuration ...
        ```

        ## Import

        Cloudfront Distributions can be imported using the `id`, e.g.

        ```sh
         $ pulumi import aws:cloudfront/distribution:Distribution distribution E74FTE3EXAMPLE
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] aliases: Extra CNAMEs (alternate domain names), if any, for
               this distribution.
        :param pulumi.Input[str] comment: Any comments you want to include about the
               distribution.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DistributionCustomErrorResponseArgs']]]] custom_error_responses: One or more custom error response elements (multiples allowed).
        :param pulumi.Input[pulumi.InputType['DistributionDefaultCacheBehaviorArgs']] default_cache_behavior: The default cache behavior for this distribution (maximum
               one).
        :param pulumi.Input[str] default_root_object: The object that you want CloudFront to
               return (for example, index.html) when an end user requests the root URL.
        :param pulumi.Input[bool] enabled: Whether the distribution is enabled to accept end
               user requests for content.
        :param pulumi.Input[str] http_version: The maximum HTTP version to support on the
               distribution. Allowed values are `http1.1` and `http2`. The default is
               `http2`.
        :param pulumi.Input[bool] is_ipv6_enabled: Whether the IPv6 is enabled for the distribution.
        :param pulumi.Input[pulumi.InputType['DistributionLoggingConfigArgs']] logging_config: The logging
               configuration that controls how logs are written
               to your distribution (maximum one).
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DistributionOrderedCacheBehaviorArgs']]]] ordered_cache_behaviors: An ordered list of cache behaviors
               resource for this distribution. List from top to bottom
               in order of precedence. The topmost cache behavior will have precedence 0.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DistributionOriginGroupArgs']]]] origin_groups: One or more origin_group for this
               distribution (multiples allowed).
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DistributionOriginArgs']]]] origins: One or more origins for this
               distribution (multiples allowed).
        :param pulumi.Input[str] price_class: The price class for this distribution. One of
               `PriceClass_All`, `PriceClass_200`, `PriceClass_100`
        :param pulumi.Input[pulumi.InputType['DistributionRestrictionsArgs']] restrictions: The restriction
               configuration for this distribution (maximum one).
        :param pulumi.Input[bool] retain_on_delete: Disables the distribution instead of
               deleting it when destroying the resource. If this is set,
               the distribution needs to be deleted manually afterwards. Default: `false`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        :param pulumi.Input[pulumi.InputType['DistributionViewerCertificateArgs']] viewer_certificate: The SSL
               configuration for this distribution (maximum
               one).
        :param pulumi.Input[bool] wait_for_deployment: If enabled, the resource will wait for
               the distribution status to change from `InProgress` to `Deployed`. Setting
               this to`false` will skip the process. Default: `true`.
        :param pulumi.Input[str] web_acl_id: A unique identifier that specifies the AWS WAF web ACL,
               if any, to associate with this distribution.
               To specify a web ACL created using the latest version of AWS WAF (WAFv2), use the ACL ARN,
               for example `aws_wafv2_web_acl.example.arn`. To specify a web
               ACL created using AWS WAF Classic, use the ACL ID, for example `aws_waf_web_acl.example.id`.
               The WAF Web ACL must exist in the WAF Global (CloudFront) region and the
               credentials configuring this argument must have `waf:GetWebACL` permissions assigned.
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

            __props__['aliases'] = aliases
            __props__['comment'] = comment
            __props__['custom_error_responses'] = custom_error_responses
            if default_cache_behavior is None and not opts.urn:
                raise TypeError("Missing required property 'default_cache_behavior'")
            __props__['default_cache_behavior'] = default_cache_behavior
            __props__['default_root_object'] = default_root_object
            if enabled is None and not opts.urn:
                raise TypeError("Missing required property 'enabled'")
            __props__['enabled'] = enabled
            __props__['http_version'] = http_version
            __props__['is_ipv6_enabled'] = is_ipv6_enabled
            __props__['logging_config'] = logging_config
            __props__['ordered_cache_behaviors'] = ordered_cache_behaviors
            __props__['origin_groups'] = origin_groups
            if origins is None and not opts.urn:
                raise TypeError("Missing required property 'origins'")
            __props__['origins'] = origins
            __props__['price_class'] = price_class
            if restrictions is None and not opts.urn:
                raise TypeError("Missing required property 'restrictions'")
            __props__['restrictions'] = restrictions
            __props__['retain_on_delete'] = retain_on_delete
            __props__['tags'] = tags
            if viewer_certificate is None and not opts.urn:
                raise TypeError("Missing required property 'viewer_certificate'")
            __props__['viewer_certificate'] = viewer_certificate
            __props__['wait_for_deployment'] = wait_for_deployment
            __props__['web_acl_id'] = web_acl_id
            __props__['arn'] = None
            __props__['caller_reference'] = None
            __props__['domain_name'] = None
            __props__['etag'] = None
            __props__['hosted_zone_id'] = None
            __props__['in_progress_validation_batches'] = None
            __props__['last_modified_time'] = None
            __props__['status'] = None
            __props__['trusted_signers'] = None
        super(Distribution, __self__).__init__(
            'aws:cloudfront/distribution:Distribution',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            aliases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            caller_reference: Optional[pulumi.Input[str]] = None,
            comment: Optional[pulumi.Input[str]] = None,
            custom_error_responses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DistributionCustomErrorResponseArgs']]]]] = None,
            default_cache_behavior: Optional[pulumi.Input[pulumi.InputType['DistributionDefaultCacheBehaviorArgs']]] = None,
            default_root_object: Optional[pulumi.Input[str]] = None,
            domain_name: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            etag: Optional[pulumi.Input[str]] = None,
            hosted_zone_id: Optional[pulumi.Input[str]] = None,
            http_version: Optional[pulumi.Input[str]] = None,
            in_progress_validation_batches: Optional[pulumi.Input[int]] = None,
            is_ipv6_enabled: Optional[pulumi.Input[bool]] = None,
            last_modified_time: Optional[pulumi.Input[str]] = None,
            logging_config: Optional[pulumi.Input[pulumi.InputType['DistributionLoggingConfigArgs']]] = None,
            ordered_cache_behaviors: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DistributionOrderedCacheBehaviorArgs']]]]] = None,
            origin_groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DistributionOriginGroupArgs']]]]] = None,
            origins: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DistributionOriginArgs']]]]] = None,
            price_class: Optional[pulumi.Input[str]] = None,
            restrictions: Optional[pulumi.Input[pulumi.InputType['DistributionRestrictionsArgs']]] = None,
            retain_on_delete: Optional[pulumi.Input[bool]] = None,
            status: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            trusted_signers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DistributionTrustedSignerArgs']]]]] = None,
            viewer_certificate: Optional[pulumi.Input[pulumi.InputType['DistributionViewerCertificateArgs']]] = None,
            wait_for_deployment: Optional[pulumi.Input[bool]] = None,
            web_acl_id: Optional[pulumi.Input[str]] = None) -> 'Distribution':
        """
        Get an existing Distribution resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] aliases: Extra CNAMEs (alternate domain names), if any, for
               this distribution.
        :param pulumi.Input[str] arn: The ARN (Amazon Resource Name) for the distribution. For example: `arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5`, where `123456789012` is your AWS account ID.
        :param pulumi.Input[str] caller_reference: Internal value used by CloudFront to allow future
               updates to the distribution configuration.
        :param pulumi.Input[str] comment: Any comments you want to include about the
               distribution.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DistributionCustomErrorResponseArgs']]]] custom_error_responses: One or more custom error response elements (multiples allowed).
        :param pulumi.Input[pulumi.InputType['DistributionDefaultCacheBehaviorArgs']] default_cache_behavior: The default cache behavior for this distribution (maximum
               one).
        :param pulumi.Input[str] default_root_object: The object that you want CloudFront to
               return (for example, index.html) when an end user requests the root URL.
        :param pulumi.Input[str] domain_name: The DNS domain name of either the S3 bucket, or
               web site of your custom origin.
        :param pulumi.Input[bool] enabled: Whether the distribution is enabled to accept end
               user requests for content.
        :param pulumi.Input[str] etag: The current version of the distribution's information. For example:
               `E2QWRUHAPOMQZL`.
        :param pulumi.Input[str] hosted_zone_id: The CloudFront Route 53 zone ID that can be used to
               route an [Alias Resource Record Set](http://docs.aws.amazon.com/Route53/latest/APIReference/CreateAliasRRSAPI.html) to. This attribute is simply an
               alias for the zone ID `Z2FDTNDATAQYW2`.
        :param pulumi.Input[str] http_version: The maximum HTTP version to support on the
               distribution. Allowed values are `http1.1` and `http2`. The default is
               `http2`.
        :param pulumi.Input[int] in_progress_validation_batches: The number of invalidation batches
               currently in progress.
        :param pulumi.Input[bool] is_ipv6_enabled: Whether the IPv6 is enabled for the distribution.
        :param pulumi.Input[str] last_modified_time: The date and time the distribution was last modified.
        :param pulumi.Input[pulumi.InputType['DistributionLoggingConfigArgs']] logging_config: The logging
               configuration that controls how logs are written
               to your distribution (maximum one).
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DistributionOrderedCacheBehaviorArgs']]]] ordered_cache_behaviors: An ordered list of cache behaviors
               resource for this distribution. List from top to bottom
               in order of precedence. The topmost cache behavior will have precedence 0.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DistributionOriginGroupArgs']]]] origin_groups: One or more origin_group for this
               distribution (multiples allowed).
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DistributionOriginArgs']]]] origins: One or more origins for this
               distribution (multiples allowed).
        :param pulumi.Input[str] price_class: The price class for this distribution. One of
               `PriceClass_All`, `PriceClass_200`, `PriceClass_100`
        :param pulumi.Input[pulumi.InputType['DistributionRestrictionsArgs']] restrictions: The restriction
               configuration for this distribution (maximum one).
        :param pulumi.Input[bool] retain_on_delete: Disables the distribution instead of
               deleting it when destroying the resource. If this is set,
               the distribution needs to be deleted manually afterwards. Default: `false`.
        :param pulumi.Input[str] status: The current status of the distribution. `Deployed` if the
               distribution's information is fully propagated throughout the Amazon
               CloudFront system.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DistributionTrustedSignerArgs']]]] trusted_signers: List of AWS account IDs (or `self`) that you want to allow to create signed URLs for private content.
               See the [CloudFront User Guide](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-trusted-signers.html) for more information about this feature.
        :param pulumi.Input[pulumi.InputType['DistributionViewerCertificateArgs']] viewer_certificate: The SSL
               configuration for this distribution (maximum
               one).
        :param pulumi.Input[bool] wait_for_deployment: If enabled, the resource will wait for
               the distribution status to change from `InProgress` to `Deployed`. Setting
               this to`false` will skip the process. Default: `true`.
        :param pulumi.Input[str] web_acl_id: A unique identifier that specifies the AWS WAF web ACL,
               if any, to associate with this distribution.
               To specify a web ACL created using the latest version of AWS WAF (WAFv2), use the ACL ARN,
               for example `aws_wafv2_web_acl.example.arn`. To specify a web
               ACL created using AWS WAF Classic, use the ACL ID, for example `aws_waf_web_acl.example.id`.
               The WAF Web ACL must exist in the WAF Global (CloudFront) region and the
               credentials configuring this argument must have `waf:GetWebACL` permissions assigned.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["aliases"] = aliases
        __props__["arn"] = arn
        __props__["caller_reference"] = caller_reference
        __props__["comment"] = comment
        __props__["custom_error_responses"] = custom_error_responses
        __props__["default_cache_behavior"] = default_cache_behavior
        __props__["default_root_object"] = default_root_object
        __props__["domain_name"] = domain_name
        __props__["enabled"] = enabled
        __props__["etag"] = etag
        __props__["hosted_zone_id"] = hosted_zone_id
        __props__["http_version"] = http_version
        __props__["in_progress_validation_batches"] = in_progress_validation_batches
        __props__["is_ipv6_enabled"] = is_ipv6_enabled
        __props__["last_modified_time"] = last_modified_time
        __props__["logging_config"] = logging_config
        __props__["ordered_cache_behaviors"] = ordered_cache_behaviors
        __props__["origin_groups"] = origin_groups
        __props__["origins"] = origins
        __props__["price_class"] = price_class
        __props__["restrictions"] = restrictions
        __props__["retain_on_delete"] = retain_on_delete
        __props__["status"] = status
        __props__["tags"] = tags
        __props__["trusted_signers"] = trusted_signers
        __props__["viewer_certificate"] = viewer_certificate
        __props__["wait_for_deployment"] = wait_for_deployment
        __props__["web_acl_id"] = web_acl_id
        return Distribution(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def aliases(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Extra CNAMEs (alternate domain names), if any, for
        this distribution.
        """
        return pulumi.get(self, "aliases")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN (Amazon Resource Name) for the distribution. For example: `arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5`, where `123456789012` is your AWS account ID.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="callerReference")
    def caller_reference(self) -> pulumi.Output[str]:
        """
        Internal value used by CloudFront to allow future
        updates to the distribution configuration.
        """
        return pulumi.get(self, "caller_reference")

    @property
    @pulumi.getter
    def comment(self) -> pulumi.Output[Optional[str]]:
        """
        Any comments you want to include about the
        distribution.
        """
        return pulumi.get(self, "comment")

    @property
    @pulumi.getter(name="customErrorResponses")
    def custom_error_responses(self) -> pulumi.Output[Optional[Sequence['outputs.DistributionCustomErrorResponse']]]:
        """
        One or more custom error response elements (multiples allowed).
        """
        return pulumi.get(self, "custom_error_responses")

    @property
    @pulumi.getter(name="defaultCacheBehavior")
    def default_cache_behavior(self) -> pulumi.Output['outputs.DistributionDefaultCacheBehavior']:
        """
        The default cache behavior for this distribution (maximum
        one).
        """
        return pulumi.get(self, "default_cache_behavior")

    @property
    @pulumi.getter(name="defaultRootObject")
    def default_root_object(self) -> pulumi.Output[Optional[str]]:
        """
        The object that you want CloudFront to
        return (for example, index.html) when an end user requests the root URL.
        """
        return pulumi.get(self, "default_root_object")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[str]:
        """
        The DNS domain name of either the S3 bucket, or
        web site of your custom origin.
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[bool]:
        """
        Whether the distribution is enabled to accept end
        user requests for content.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        The current version of the distribution's information. For example:
        `E2QWRUHAPOMQZL`.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> pulumi.Output[str]:
        """
        The CloudFront Route 53 zone ID that can be used to
        route an [Alias Resource Record Set](http://docs.aws.amazon.com/Route53/latest/APIReference/CreateAliasRRSAPI.html) to. This attribute is simply an
        alias for the zone ID `Z2FDTNDATAQYW2`.
        """
        return pulumi.get(self, "hosted_zone_id")

    @property
    @pulumi.getter(name="httpVersion")
    def http_version(self) -> pulumi.Output[Optional[str]]:
        """
        The maximum HTTP version to support on the
        distribution. Allowed values are `http1.1` and `http2`. The default is
        `http2`.
        """
        return pulumi.get(self, "http_version")

    @property
    @pulumi.getter(name="inProgressValidationBatches")
    def in_progress_validation_batches(self) -> pulumi.Output[int]:
        """
        The number of invalidation batches
        currently in progress.
        """
        return pulumi.get(self, "in_progress_validation_batches")

    @property
    @pulumi.getter(name="isIpv6Enabled")
    def is_ipv6_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether the IPv6 is enabled for the distribution.
        """
        return pulumi.get(self, "is_ipv6_enabled")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[str]:
        """
        The date and time the distribution was last modified.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> pulumi.Output[Optional['outputs.DistributionLoggingConfig']]:
        """
        The logging
        configuration that controls how logs are written
        to your distribution (maximum one).
        """
        return pulumi.get(self, "logging_config")

    @property
    @pulumi.getter(name="orderedCacheBehaviors")
    def ordered_cache_behaviors(self) -> pulumi.Output[Optional[Sequence['outputs.DistributionOrderedCacheBehavior']]]:
        """
        An ordered list of cache behaviors
        resource for this distribution. List from top to bottom
        in order of precedence. The topmost cache behavior will have precedence 0.
        """
        return pulumi.get(self, "ordered_cache_behaviors")

    @property
    @pulumi.getter(name="originGroups")
    def origin_groups(self) -> pulumi.Output[Optional[Sequence['outputs.DistributionOriginGroup']]]:
        """
        One or more origin_group for this
        distribution (multiples allowed).
        """
        return pulumi.get(self, "origin_groups")

    @property
    @pulumi.getter
    def origins(self) -> pulumi.Output[Sequence['outputs.DistributionOrigin']]:
        """
        One or more origins for this
        distribution (multiples allowed).
        """
        return pulumi.get(self, "origins")

    @property
    @pulumi.getter(name="priceClass")
    def price_class(self) -> pulumi.Output[Optional[str]]:
        """
        The price class for this distribution. One of
        `PriceClass_All`, `PriceClass_200`, `PriceClass_100`
        """
        return pulumi.get(self, "price_class")

    @property
    @pulumi.getter
    def restrictions(self) -> pulumi.Output['outputs.DistributionRestrictions']:
        """
        The restriction
        configuration for this distribution (maximum one).
        """
        return pulumi.get(self, "restrictions")

    @property
    @pulumi.getter(name="retainOnDelete")
    def retain_on_delete(self) -> pulumi.Output[Optional[bool]]:
        """
        Disables the distribution instead of
        deleting it when destroying the resource. If this is set,
        the distribution needs to be deleted manually afterwards. Default: `false`.
        """
        return pulumi.get(self, "retain_on_delete")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The current status of the distribution. `Deployed` if the
        distribution's information is fully propagated throughout the Amazon
        CloudFront system.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="trustedSigners")
    def trusted_signers(self) -> pulumi.Output[Sequence['outputs.DistributionTrustedSigner']]:
        """
        List of AWS account IDs (or `self`) that you want to allow to create signed URLs for private content.
        See the [CloudFront User Guide](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-trusted-signers.html) for more information about this feature.
        """
        return pulumi.get(self, "trusted_signers")

    @property
    @pulumi.getter(name="viewerCertificate")
    def viewer_certificate(self) -> pulumi.Output['outputs.DistributionViewerCertificate']:
        """
        The SSL
        configuration for this distribution (maximum
        one).
        """
        return pulumi.get(self, "viewer_certificate")

    @property
    @pulumi.getter(name="waitForDeployment")
    def wait_for_deployment(self) -> pulumi.Output[Optional[bool]]:
        """
        If enabled, the resource will wait for
        the distribution status to change from `InProgress` to `Deployed`. Setting
        this to`false` will skip the process. Default: `true`.
        """
        return pulumi.get(self, "wait_for_deployment")

    @property
    @pulumi.getter(name="webAclId")
    def web_acl_id(self) -> pulumi.Output[Optional[str]]:
        """
        A unique identifier that specifies the AWS WAF web ACL,
        if any, to associate with this distribution.
        To specify a web ACL created using the latest version of AWS WAF (WAFv2), use the ACL ARN,
        for example `aws_wafv2_web_acl.example.arn`. To specify a web
        ACL created using AWS WAF Classic, use the ACL ID, for example `aws_waf_web_acl.example.id`.
        The WAF Web ACL must exist in the WAF Global (CloudFront) region and the
        credentials configuring this argument must have `waf:GetWebACL` permissions assigned.
        """
        return pulumi.get(self, "web_acl_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

