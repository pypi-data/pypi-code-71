# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'GetPrebuiltEcrImageResult',
    'AwaitableGetPrebuiltEcrImageResult',
    'get_prebuilt_ecr_image',
]

@pulumi.output_type
class GetPrebuiltEcrImageResult:
    """
    A collection of values returned by getPrebuiltEcrImage.
    """
    def __init__(__self__, dns_suffix=None, id=None, image_tag=None, region=None, registry_id=None, registry_path=None, repository_name=None):
        if dns_suffix and not isinstance(dns_suffix, str):
            raise TypeError("Expected argument 'dns_suffix' to be a str")
        pulumi.set(__self__, "dns_suffix", dns_suffix)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if image_tag and not isinstance(image_tag, str):
            raise TypeError("Expected argument 'image_tag' to be a str")
        pulumi.set(__self__, "image_tag", image_tag)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if registry_id and not isinstance(registry_id, str):
            raise TypeError("Expected argument 'registry_id' to be a str")
        pulumi.set(__self__, "registry_id", registry_id)
        if registry_path and not isinstance(registry_path, str):
            raise TypeError("Expected argument 'registry_path' to be a str")
        pulumi.set(__self__, "registry_path", registry_path)
        if repository_name and not isinstance(repository_name, str):
            raise TypeError("Expected argument 'repository_name' to be a str")
        pulumi.set(__self__, "repository_name", repository_name)

    @property
    @pulumi.getter(name="dnsSuffix")
    def dns_suffix(self) -> Optional[str]:
        return pulumi.get(self, "dns_suffix")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="imageTag")
    def image_tag(self) -> Optional[str]:
        return pulumi.get(self, "image_tag")

    @property
    @pulumi.getter
    def region(self) -> Optional[str]:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> str:
        """
        The account ID containing the image. For example, `469771592824`.
        """
        return pulumi.get(self, "registry_id")

    @property
    @pulumi.getter(name="registryPath")
    def registry_path(self) -> str:
        """
        The Docker image URL. For example, `341280168497.dkr.ecr.ca-central-1.amazonaws.com/sagemaker-sparkml-serving:2.4`.
        """
        return pulumi.get(self, "registry_path")

    @property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> str:
        return pulumi.get(self, "repository_name")


class AwaitableGetPrebuiltEcrImageResult(GetPrebuiltEcrImageResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPrebuiltEcrImageResult(
            dns_suffix=self.dns_suffix,
            id=self.id,
            image_tag=self.image_tag,
            region=self.region,
            registry_id=self.registry_id,
            registry_path=self.registry_path,
            repository_name=self.repository_name)


def get_prebuilt_ecr_image(dns_suffix: Optional[str] = None,
                           image_tag: Optional[str] = None,
                           region: Optional[str] = None,
                           repository_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPrebuiltEcrImageResult:
    """
    Get information about prebuilt Amazon SageMaker Docker images.

    > **NOTE:** The AWS provider creates a validly constructed `registry_path` but does not verify that the `registry_path` corresponds to an existing image. For example, using a `registry_path` containing an `image_tag` that does not correspond to a Docker image in the ECR repository, will result in an error.

    ## Example Usage

    Basic usage:

    ```python
    import pulumi
    import pulumi_aws as aws

    test = aws.sagemaker.get_prebuilt_ecr_image(image_tag="2.2-1.0.11.0",
        repository_name="sagemaker-scikit-learn")
    ```


    :param str dns_suffix: The DNS suffix to use in the registry path. If not specified, the AWS provider sets it to the DNS suffix for the current region.
    :param str image_tag: The image tag for the Docker image. If not specified, the AWS provider sets the value to `1`, which for many repositories indicates the latest version. Some repositories, such as XGBoost, do not support `1` or `latest` and specific version must be used.
    :param str region: The region to use in the registry path. If not specified, the AWS provider sets it to the current region.
    :param str repository_name: The name of the repository, which is generally the algorithm or library. Values include `blazingtext`, `factorization-machines`, `forecasting-deepar`, `image-classification`, `ipinsights`, `kmeans`, `knn`, `lda`, `linear-learner`, `mxnet-inference-eia`, `mxnet-inference`, `mxnet-training`, `ntm`, `object-detection`, `object2vec`, `pca`, `pytorch-inference-eia`, `pytorch-inference`, `pytorch-training`, `randomcutforest`, `sagemaker-scikit-learn`, `sagemaker-sparkml-serving`, `sagemaker-xgboost`, `semantic-segmentation`, `seq2seq`, `tensorflow-inference-eia`, `tensorflow-inference`, and `tensorflow-training`.
    """
    __args__ = dict()
    __args__['dnsSuffix'] = dns_suffix
    __args__['imageTag'] = image_tag
    __args__['region'] = region
    __args__['repositoryName'] = repository_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:sagemaker/getPrebuiltEcrImage:getPrebuiltEcrImage', __args__, opts=opts, typ=GetPrebuiltEcrImageResult).value

    return AwaitableGetPrebuiltEcrImageResult(
        dns_suffix=__ret__.dns_suffix,
        id=__ret__.id,
        image_tag=__ret__.image_tag,
        region=__ret__.region,
        registry_id=__ret__.registry_id,
        registry_path=__ret__.registry_path,
        repository_name=__ret__.repository_name)
