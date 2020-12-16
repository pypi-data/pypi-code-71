# coding: utf-8

"""
    CLOUD API

    An enterprise-grade Infrastructure is provided as a Service (IaaS) solution that can be managed through a browser-based \"Data Center Designer\" (DCD) tool or via an easy to use API.   The API allows you to perform a variety of management tasks such as spinning up additional servers, adding volumes, adjusting networking, and so forth. It is designed to allow users to leverage the same power and flexibility found within the DCD visual tool. Both tools are consistent with their concepts and lend well to making the experience smooth and intuitive.  # noqa: E501

    The version of the OpenAPI document: 5.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import ionoscloud
from ionoscloud.models.request_metadata import RequestMetadata  # noqa: E501
from ionoscloud.rest import ApiException

class TestRequestMetadata(unittest.TestCase):
    """RequestMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RequestMetadata
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ionoscloud.models.request_metadata.RequestMetadata()  # noqa: E501
        if include_optional :
            return RequestMetadata(
                created_date = '2015-12-04T14:34:09.809Z',
                created_by = 'user@example.com',
                etag = '45480eb3fbfc31f1d916c1eaa4abdcc3',
                request_status = ionoscloud.models.request_status.RequestStatus(
                    id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                    type = "request-status", 
                    href = '<RESOURCE-URI>', 
                    metadata = ionoscloud.models.request_status_metadata.RequestStatusMetadata(
                        status = 'QUEUED', 
                        message = '', 
                        etag = '45480eb3fbfc31f1d916c1eaa4abdcc3', 
                        targets = [
                            ionoscloud.models.request_target.RequestTarget(
                                target = ionoscloud.models.resource_reference.ResourceReference(
                                    id = '', 
                                    type = "resource", 
                                    href = '<RESOURCE-URI>', ), 
                                status = 'QUEUED', )
                            ], ), )
            )
        else :
            return RequestMetadata(
        )

    def testRequestMetadata(self):
        """Test RequestMetadata"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
