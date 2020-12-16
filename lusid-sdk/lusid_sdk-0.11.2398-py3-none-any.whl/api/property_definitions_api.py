# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2398
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from lusid.api_client import ApiClient
from lusid.exceptions import (
    ApiTypeError,
    ApiValueError
)


class PropertyDefinitionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_property_definition(self, create_property_definition_request, **kwargs):  # noqa: E501
        """Create property definition  # noqa: E501

        Define a new property.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_property_definition(create_property_definition_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param CreatePropertyDefinitionRequest create_property_definition_request: The definition of the new property. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PropertyDefinition
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_property_definition_with_http_info(create_property_definition_request, **kwargs)  # noqa: E501

    def create_property_definition_with_http_info(self, create_property_definition_request, **kwargs):  # noqa: E501
        """Create property definition  # noqa: E501

        Define a new property.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_property_definition_with_http_info(create_property_definition_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param CreatePropertyDefinitionRequest create_property_definition_request: The definition of the new property. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PropertyDefinition, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['create_property_definition_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_property_definition" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'create_property_definition_request' is set
        if ('create_property_definition_request' not in local_var_params or
                local_var_params['create_property_definition_request'] is None):
            raise ApiValueError("Missing the required parameter `create_property_definition_request` when calling `create_property_definition`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_property_definition_request' in local_var_params:
            body_params = local_var_params['create_property_definition_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.11.2398'

        return self.api_client.call_api(
            '/api/propertydefinitions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PropertyDefinition',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_property_definition(self, domain, scope, code, **kwargs):  # noqa: E501
        """Delete property definition  # noqa: E501

        Delete the definition of the specified property.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_property_definition(domain, scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str domain: The domain of the property to be deleted. (required)
        :param str scope: The scope of the property to be deleted. (required)
        :param str code: The code of the property to be deleted. Together with the domain and scope this uniquely              identifies the property. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: DeletedEntityResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_property_definition_with_http_info(domain, scope, code, **kwargs)  # noqa: E501

    def delete_property_definition_with_http_info(self, domain, scope, code, **kwargs):  # noqa: E501
        """Delete property definition  # noqa: E501

        Delete the definition of the specified property.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_property_definition_with_http_info(domain, scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str domain: The domain of the property to be deleted. (required)
        :param str scope: The scope of the property to be deleted. (required)
        :param str code: The code of the property to be deleted. Together with the domain and scope this uniquely              identifies the property. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(DeletedEntityResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['domain', 'scope', 'code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_property_definition" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'domain' is set
        if ('domain' not in local_var_params or
                local_var_params['domain'] is None):
            raise ApiValueError("Missing the required parameter `domain` when calling `delete_property_definition`")  # noqa: E501

        if ('scope' in local_var_params and
                len(local_var_params['scope']) > 64):
            raise ApiValueError("Invalid value for parameter `scope` when calling `delete_property_definition`, length must be less than or equal to `64`")  # noqa: E501
        if ('scope' in local_var_params and
                len(local_var_params['scope']) < 1):
            raise ApiValueError("Invalid value for parameter `scope` when calling `delete_property_definition`, length must be greater than or equal to `1`")  # noqa: E501
        if 'scope' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['scope']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `delete_property_definition`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        if ('code' in local_var_params and
                len(local_var_params['code']) > 64):
            raise ApiValueError("Invalid value for parameter `code` when calling `delete_property_definition`, length must be less than or equal to `64`")  # noqa: E501
        if ('code' in local_var_params and
                len(local_var_params['code']) < 1):
            raise ApiValueError("Invalid value for parameter `code` when calling `delete_property_definition`, length must be greater than or equal to `1`")  # noqa: E501
        if 'code' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['code']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `code` when calling `delete_property_definition`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'domain' in local_var_params:
            path_params['domain'] = local_var_params['domain']  # noqa: E501
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.11.2398'

        return self.api_client.call_api(
            '/api/propertydefinitions/{domain}/{scope}/{code}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeletedEntityResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_multiple_property_definitions(self, property_keys, **kwargs):  # noqa: E501
        """Get multiple property definitions  # noqa: E501

        Retrieve the definition of one or more specified properties.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_multiple_property_definitions(property_keys, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param list[str] property_keys: One or more property keys which identify each property that a definition should              be retrieved for. The format for each property key is {domain}/{scope}/{code}, e.g. 'Portfolio/Manager/Id'. (required)
        :param datetime as_at: The asAt datetime at which to retrieve the property definitions. Defaults to return              the latest version of each definition if not specified.
        :param str filter: Expression to filter the result set.               For example, to filter on the Lifetime, use \"lifeTime eq 'Perpetual'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ResourceListOfPropertyDefinition
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_multiple_property_definitions_with_http_info(property_keys, **kwargs)  # noqa: E501

    def get_multiple_property_definitions_with_http_info(self, property_keys, **kwargs):  # noqa: E501
        """Get multiple property definitions  # noqa: E501

        Retrieve the definition of one or more specified properties.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_multiple_property_definitions_with_http_info(property_keys, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param list[str] property_keys: One or more property keys which identify each property that a definition should              be retrieved for. The format for each property key is {domain}/{scope}/{code}, e.g. 'Portfolio/Manager/Id'. (required)
        :param datetime as_at: The asAt datetime at which to retrieve the property definitions. Defaults to return              the latest version of each definition if not specified.
        :param str filter: Expression to filter the result set.               For example, to filter on the Lifetime, use \"lifeTime eq 'Perpetual'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ResourceListOfPropertyDefinition, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['property_keys', 'as_at', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_multiple_property_definitions" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'property_keys' is set
        if ('property_keys' not in local_var_params or
                local_var_params['property_keys'] is None):
            raise ApiValueError("Missing the required parameter `property_keys` when calling `get_multiple_property_definitions`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'as_at' in local_var_params:
            query_params.append(('asAt', local_var_params['as_at']))  # noqa: E501
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))  # noqa: E501
        if 'property_keys' in local_var_params:
            query_params.append(('propertyKeys', local_var_params['property_keys']))  # noqa: E501
            collection_formats['propertyKeys'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.11.2398'

        return self.api_client.call_api(
            '/api/propertydefinitions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourceListOfPropertyDefinition',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_property_definition(self, domain, scope, code, **kwargs):  # noqa: E501
        """Get property definition  # noqa: E501

        Retrieve the definition of a specified property.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_property_definition(domain, scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str domain: The domain of the specified property. (required)
        :param str scope: The scope of the specified property. (required)
        :param str code: The code of the specified property. Together with the domain and scope this uniquely              identifies the property. (required)
        :param datetime as_at: The asAt datetime at which to retrieve the property definition. Defaults to return              the latest version of the definition if not specified.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PropertyDefinition
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_property_definition_with_http_info(domain, scope, code, **kwargs)  # noqa: E501

    def get_property_definition_with_http_info(self, domain, scope, code, **kwargs):  # noqa: E501
        """Get property definition  # noqa: E501

        Retrieve the definition of a specified property.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_property_definition_with_http_info(domain, scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str domain: The domain of the specified property. (required)
        :param str scope: The scope of the specified property. (required)
        :param str code: The code of the specified property. Together with the domain and scope this uniquely              identifies the property. (required)
        :param datetime as_at: The asAt datetime at which to retrieve the property definition. Defaults to return              the latest version of the definition if not specified.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PropertyDefinition, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['domain', 'scope', 'code', 'as_at']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_property_definition" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'domain' is set
        if ('domain' not in local_var_params or
                local_var_params['domain'] is None):
            raise ApiValueError("Missing the required parameter `domain` when calling `get_property_definition`")  # noqa: E501

        if ('scope' in local_var_params and
                len(local_var_params['scope']) > 64):
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_property_definition`, length must be less than or equal to `64`")  # noqa: E501
        if ('scope' in local_var_params and
                len(local_var_params['scope']) < 1):
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_property_definition`, length must be greater than or equal to `1`")  # noqa: E501
        if 'scope' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['scope']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_property_definition`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        if ('code' in local_var_params and
                len(local_var_params['code']) > 64):
            raise ApiValueError("Invalid value for parameter `code` when calling `get_property_definition`, length must be less than or equal to `64`")  # noqa: E501
        if ('code' in local_var_params and
                len(local_var_params['code']) < 1):
            raise ApiValueError("Invalid value for parameter `code` when calling `get_property_definition`, length must be greater than or equal to `1`")  # noqa: E501
        if 'code' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['code']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `code` when calling `get_property_definition`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'domain' in local_var_params:
            path_params['domain'] = local_var_params['domain']  # noqa: E501
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501

        query_params = []
        if 'as_at' in local_var_params:
            query_params.append(('asAt', local_var_params['as_at']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.11.2398'

        return self.api_client.call_api(
            '/api/propertydefinitions/{domain}/{scope}/{code}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PropertyDefinition',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_property_definition(self, domain, scope, code, update_property_definition_request, **kwargs):  # noqa: E501
        """Update property definition  # noqa: E501

        Update the definition of a specified existing property. Not all elements within a property definition  are modifiable due to the potential implications for values already stored against the property.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_property_definition(domain, scope, code, update_property_definition_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str domain: The domain of the property being updated. (required)
        :param str scope: The scope of the property being updated. (required)
        :param str code: The code of the property being updated. Together with the domain and scope this uniquely              identifies the property. (required)
        :param UpdatePropertyDefinitionRequest update_property_definition_request: The updated definition of the property. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PropertyDefinition
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.update_property_definition_with_http_info(domain, scope, code, update_property_definition_request, **kwargs)  # noqa: E501

    def update_property_definition_with_http_info(self, domain, scope, code, update_property_definition_request, **kwargs):  # noqa: E501
        """Update property definition  # noqa: E501

        Update the definition of a specified existing property. Not all elements within a property definition  are modifiable due to the potential implications for values already stored against the property.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_property_definition_with_http_info(domain, scope, code, update_property_definition_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str domain: The domain of the property being updated. (required)
        :param str scope: The scope of the property being updated. (required)
        :param str code: The code of the property being updated. Together with the domain and scope this uniquely              identifies the property. (required)
        :param UpdatePropertyDefinitionRequest update_property_definition_request: The updated definition of the property. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PropertyDefinition, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['domain', 'scope', 'code', 'update_property_definition_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_property_definition" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'domain' is set
        if ('domain' not in local_var_params or
                local_var_params['domain'] is None):
            raise ApiValueError("Missing the required parameter `domain` when calling `update_property_definition`")  # noqa: E501
        # verify the required parameter 'update_property_definition_request' is set
        if ('update_property_definition_request' not in local_var_params or
                local_var_params['update_property_definition_request'] is None):
            raise ApiValueError("Missing the required parameter `update_property_definition_request` when calling `update_property_definition`")  # noqa: E501

        if ('scope' in local_var_params and
                len(local_var_params['scope']) > 64):
            raise ApiValueError("Invalid value for parameter `scope` when calling `update_property_definition`, length must be less than or equal to `64`")  # noqa: E501
        if ('scope' in local_var_params and
                len(local_var_params['scope']) < 1):
            raise ApiValueError("Invalid value for parameter `scope` when calling `update_property_definition`, length must be greater than or equal to `1`")  # noqa: E501
        if 'scope' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['scope']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `update_property_definition`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        if ('code' in local_var_params and
                len(local_var_params['code']) > 64):
            raise ApiValueError("Invalid value for parameter `code` when calling `update_property_definition`, length must be less than or equal to `64`")  # noqa: E501
        if ('code' in local_var_params and
                len(local_var_params['code']) < 1):
            raise ApiValueError("Invalid value for parameter `code` when calling `update_property_definition`, length must be greater than or equal to `1`")  # noqa: E501
        if 'code' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['code']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `code` when calling `update_property_definition`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'domain' in local_var_params:
            path_params['domain'] = local_var_params['domain']  # noqa: E501
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'update_property_definition_request' in local_var_params:
            body_params = local_var_params['update_property_definition_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.11.2398'

        return self.api_client.call_api(
            '/api/propertydefinitions/{domain}/{scope}/{code}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PropertyDefinition',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
