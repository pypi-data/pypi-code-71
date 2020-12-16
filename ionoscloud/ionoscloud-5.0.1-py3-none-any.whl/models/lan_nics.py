# coding: utf-8

"""
    CLOUD API

    An enterprise-grade Infrastructure is provided as a Service (IaaS) solution that can be managed through a browser-based \"Data Center Designer\" (DCD) tool or via an easy to use API.   The API allows you to perform a variety of management tasks such as spinning up additional servers, adding volumes, adjusting networking, and so forth. It is designed to allow users to leverage the same power and flexibility found within the DCD visual tool. Both tools are consistent with their concepts and lend well to making the experience smooth and intuitive.  # noqa: E501

    The version of the OpenAPI document: 5.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ionoscloud.configuration import Configuration


class LanNics(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'type': 'Type',
        'href': 'str',
        'items': 'list[Nic]',
        'offset': 'float',
        'limit': 'float',
        'links': 'PaginationLinks',
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'href': 'href',
        'items': 'items',
        'offset': 'offset',
        'limit': 'limit',
        'links': '_links',
    }

    def __init__(self, id=None, type=None, href=None, items=None, offset=None, limit=None, links=None, local_vars_configuration=None):  # noqa: E501
        """LanNics - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._type = None
        self._href = None
        self._items = None
        self._offset = None
        self._limit = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if href is not None:
            self.href = href
        if items is not None:
            self.items = items
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this LanNics.  # noqa: E501

        The resource's unique identifier  # noqa: E501

        :return: The id of this LanNics.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LanNics.

        The resource's unique identifier  # noqa: E501

        :param id: The id of this LanNics.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this LanNics.  # noqa: E501

        The type of object that has been created  # noqa: E501

        :return: The type of this LanNics.  # noqa: E501
        :rtype: Type
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LanNics.

        The type of object that has been created  # noqa: E501

        :param type: The type of this LanNics.  # noqa: E501
        :type type: Type
        """

        self._type = type

    @property
    def href(self):
        """Gets the href of this LanNics.  # noqa: E501

        URL to the object representation (absolute path)  # noqa: E501

        :return: The href of this LanNics.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this LanNics.

        URL to the object representation (absolute path)  # noqa: E501

        :param href: The href of this LanNics.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def items(self):
        """Gets the items of this LanNics.  # noqa: E501

        Array of items in that collection  # noqa: E501

        :return: The items of this LanNics.  # noqa: E501
        :rtype: list[Nic]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this LanNics.

        Array of items in that collection  # noqa: E501

        :param items: The items of this LanNics.  # noqa: E501
        :type items: list[Nic]
        """

        self._items = items

    @property
    def offset(self):
        """Gets the offset of this LanNics.  # noqa: E501

        the offset (if specified in the request)  # noqa: E501

        :return: The offset of this LanNics.  # noqa: E501
        :rtype: float
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this LanNics.

        the offset (if specified in the request)  # noqa: E501

        :param offset: The offset of this LanNics.  # noqa: E501
        :type offset: float
        """

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this LanNics.  # noqa: E501

        the limit (if specified in the request)  # noqa: E501

        :return: The limit of this LanNics.  # noqa: E501
        :rtype: float
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this LanNics.

        the limit (if specified in the request)  # noqa: E501

        :param limit: The limit of this LanNics.  # noqa: E501
        :type limit: float
        """

        self._limit = limit

    @property
    def links(self):
        """Gets the links of this LanNics.  # noqa: E501


        :return: The links of this LanNics.  # noqa: E501
        :rtype: PaginationLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this LanNics.


        :param links: The links of this LanNics.  # noqa: E501
        :type links: PaginationLinks
        """

        self._links = links

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LanNics):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LanNics):
            return True

        return self.to_dict() != other.to_dict()
