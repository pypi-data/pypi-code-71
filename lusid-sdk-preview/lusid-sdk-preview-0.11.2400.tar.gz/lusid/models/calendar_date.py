# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2400
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class CalendarDate(object):
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
        'href': 'str',
        'calendar_identifier': 'ResourceId',
        'date_identifier': 'str',
        'from_utc': 'datetime',
        'to_utc': 'datetime',
        'local_date': 'str',
        'timezone': 'str',
        'description': 'str',
        'type': 'str',
        'attributes': 'DateAttributes',
        'source_data': 'dict(str, str)'
    }

    attribute_map = {
        'href': 'href',
        'calendar_identifier': 'calendarIdentifier',
        'date_identifier': 'dateIdentifier',
        'from_utc': 'fromUtc',
        'to_utc': 'toUtc',
        'local_date': 'localDate',
        'timezone': 'timezone',
        'description': 'description',
        'type': 'type',
        'attributes': 'attributes',
        'source_data': 'sourceData'
    }

    required_map = {
        'href': 'optional',
        'calendar_identifier': 'required',
        'date_identifier': 'required',
        'from_utc': 'required',
        'to_utc': 'required',
        'local_date': 'required',
        'timezone': 'required',
        'description': 'required',
        'type': 'required',
        'attributes': 'required',
        'source_data': 'required'
    }

    def __init__(self, href=None, calendar_identifier=None, date_identifier=None, from_utc=None, to_utc=None, local_date=None, timezone=None, description=None, type=None, attributes=None, source_data=None):  # noqa: E501
        """
        CalendarDate - a model defined in OpenAPI

        :param href: 
        :type href: str
        :param calendar_identifier:  (required)
        :type calendar_identifier: lusid.ResourceId
        :param date_identifier:  (required)
        :type date_identifier: str
        :param from_utc:  (required)
        :type from_utc: datetime
        :param to_utc:  (required)
        :type to_utc: datetime
        :param local_date:  (required)
        :type local_date: str
        :param timezone:  (required)
        :type timezone: str
        :param description:  (required)
        :type description: str
        :param type:  (required)
        :type type: str
        :param attributes:  (required)
        :type attributes: lusid.DateAttributes
        :param source_data:  (required)
        :type source_data: dict(str, str)

        """  # noqa: E501

        self._href = None
        self._calendar_identifier = None
        self._date_identifier = None
        self._from_utc = None
        self._to_utc = None
        self._local_date = None
        self._timezone = None
        self._description = None
        self._type = None
        self._attributes = None
        self._source_data = None
        self.discriminator = None

        self.href = href
        self.calendar_identifier = calendar_identifier
        self.date_identifier = date_identifier
        self.from_utc = from_utc
        self.to_utc = to_utc
        self.local_date = local_date
        self.timezone = timezone
        self.description = description
        self.type = type
        self.attributes = attributes
        self.source_data = source_data

    @property
    def href(self):
        """Gets the href of this CalendarDate.  # noqa: E501


        :return: The href of this CalendarDate.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this CalendarDate.


        :param href: The href of this CalendarDate.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def calendar_identifier(self):
        """Gets the calendar_identifier of this CalendarDate.  # noqa: E501


        :return: The calendar_identifier of this CalendarDate.  # noqa: E501
        :rtype: ResourceId
        """
        return self._calendar_identifier

    @calendar_identifier.setter
    def calendar_identifier(self, calendar_identifier):
        """Sets the calendar_identifier of this CalendarDate.


        :param calendar_identifier: The calendar_identifier of this CalendarDate.  # noqa: E501
        :type: ResourceId
        """
        if calendar_identifier is None:
            raise ValueError("Invalid value for `calendar_identifier`, must not be `None`")  # noqa: E501

        self._calendar_identifier = calendar_identifier

    @property
    def date_identifier(self):
        """Gets the date_identifier of this CalendarDate.  # noqa: E501


        :return: The date_identifier of this CalendarDate.  # noqa: E501
        :rtype: str
        """
        return self._date_identifier

    @date_identifier.setter
    def date_identifier(self, date_identifier):
        """Sets the date_identifier of this CalendarDate.


        :param date_identifier: The date_identifier of this CalendarDate.  # noqa: E501
        :type: str
        """
        if date_identifier is None:
            raise ValueError("Invalid value for `date_identifier`, must not be `None`")  # noqa: E501

        self._date_identifier = date_identifier

    @property
    def from_utc(self):
        """Gets the from_utc of this CalendarDate.  # noqa: E501


        :return: The from_utc of this CalendarDate.  # noqa: E501
        :rtype: datetime
        """
        return self._from_utc

    @from_utc.setter
    def from_utc(self, from_utc):
        """Sets the from_utc of this CalendarDate.


        :param from_utc: The from_utc of this CalendarDate.  # noqa: E501
        :type: datetime
        """
        if from_utc is None:
            raise ValueError("Invalid value for `from_utc`, must not be `None`")  # noqa: E501

        self._from_utc = from_utc

    @property
    def to_utc(self):
        """Gets the to_utc of this CalendarDate.  # noqa: E501


        :return: The to_utc of this CalendarDate.  # noqa: E501
        :rtype: datetime
        """
        return self._to_utc

    @to_utc.setter
    def to_utc(self, to_utc):
        """Sets the to_utc of this CalendarDate.


        :param to_utc: The to_utc of this CalendarDate.  # noqa: E501
        :type: datetime
        """
        if to_utc is None:
            raise ValueError("Invalid value for `to_utc`, must not be `None`")  # noqa: E501

        self._to_utc = to_utc

    @property
    def local_date(self):
        """Gets the local_date of this CalendarDate.  # noqa: E501


        :return: The local_date of this CalendarDate.  # noqa: E501
        :rtype: str
        """
        return self._local_date

    @local_date.setter
    def local_date(self, local_date):
        """Sets the local_date of this CalendarDate.


        :param local_date: The local_date of this CalendarDate.  # noqa: E501
        :type: str
        """
        if local_date is None:
            raise ValueError("Invalid value for `local_date`, must not be `None`")  # noqa: E501

        self._local_date = local_date

    @property
    def timezone(self):
        """Gets the timezone of this CalendarDate.  # noqa: E501


        :return: The timezone of this CalendarDate.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this CalendarDate.


        :param timezone: The timezone of this CalendarDate.  # noqa: E501
        :type: str
        """
        if timezone is None:
            raise ValueError("Invalid value for `timezone`, must not be `None`")  # noqa: E501

        self._timezone = timezone

    @property
    def description(self):
        """Gets the description of this CalendarDate.  # noqa: E501


        :return: The description of this CalendarDate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CalendarDate.


        :param description: The description of this CalendarDate.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def type(self):
        """Gets the type of this CalendarDate.  # noqa: E501


        :return: The type of this CalendarDate.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CalendarDate.


        :param type: The type of this CalendarDate.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def attributes(self):
        """Gets the attributes of this CalendarDate.  # noqa: E501


        :return: The attributes of this CalendarDate.  # noqa: E501
        :rtype: DateAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this CalendarDate.


        :param attributes: The attributes of this CalendarDate.  # noqa: E501
        :type: DateAttributes
        """
        if attributes is None:
            raise ValueError("Invalid value for `attributes`, must not be `None`")  # noqa: E501

        self._attributes = attributes

    @property
    def source_data(self):
        """Gets the source_data of this CalendarDate.  # noqa: E501


        :return: The source_data of this CalendarDate.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._source_data

    @source_data.setter
    def source_data(self, source_data):
        """Sets the source_data of this CalendarDate.


        :param source_data: The source_data of this CalendarDate.  # noqa: E501
        :type: dict(str, str)
        """
        if source_data is None:
            raise ValueError("Invalid value for `source_data`, must not be `None`")  # noqa: E501

        self._source_data = source_data

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
        if not isinstance(other, CalendarDate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
