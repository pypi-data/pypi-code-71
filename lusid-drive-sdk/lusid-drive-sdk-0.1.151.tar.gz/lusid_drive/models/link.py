# coding: utf-8

"""
    FINBOURNE Drive API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.151
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class Link(object):
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
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'relation': 'str',
        'href': 'str',
        'description': 'str',
        'method': 'str'
    }

    attribute_map = {
        'relation': 'relation',
        'href': 'href',
        'description': 'description',
        'method': 'method'
    }

    required_map = {
        'relation': 'required',
        'href': 'required',
        'description': 'optional',
        'method': 'required'
    }

    def __init__(self, relation=None, href=None, description=None, method=None):  # noqa: E501
        """
        Link - a model defined in OpenAPI

        :param relation:  (required)
        :type relation: str
        :param href:  (required)
        :type href: str
        :param description: 
        :type description: str
        :param method:  (required)
        :type method: str

        """  # noqa: E501

        self._relation = None
        self._href = None
        self._description = None
        self._method = None
        self.discriminator = None

        self.relation = relation
        self.href = href
        self.description = description
        self.method = method

    @property
    def relation(self):
        """Gets the relation of this Link.  # noqa: E501


        :return: The relation of this Link.  # noqa: E501
        :rtype: str
        """
        return self._relation

    @relation.setter
    def relation(self, relation):
        """Sets the relation of this Link.


        :param relation: The relation of this Link.  # noqa: E501
        :type: str
        """
        if relation is None:
            raise ValueError("Invalid value for `relation`, must not be `None`")  # noqa: E501

        self._relation = relation

    @property
    def href(self):
        """Gets the href of this Link.  # noqa: E501


        :return: The href of this Link.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Link.


        :param href: The href of this Link.  # noqa: E501
        :type: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href

    @property
    def description(self):
        """Gets the description of this Link.  # noqa: E501


        :return: The description of this Link.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Link.


        :param description: The description of this Link.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def method(self):
        """Gets the method of this Link.  # noqa: E501


        :return: The method of this Link.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this Link.


        :param method: The method of this Link.  # noqa: E501
        :type: str
        """
        if method is None:
            raise ValueError("Invalid value for `method`, must not be `None`")  # noqa: E501

        self._method = method

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
        if not isinstance(other, Link):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
