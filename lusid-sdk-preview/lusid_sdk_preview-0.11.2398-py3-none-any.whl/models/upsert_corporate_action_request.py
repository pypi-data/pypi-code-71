# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2398
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class UpsertCorporateActionRequest(object):
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
        'corporate_action_code': 'str',
        'description': 'str',
        'announcement_date': 'datetime',
        'ex_date': 'datetime',
        'record_date': 'datetime',
        'payment_date': 'datetime',
        'transitions': 'list[CorporateActionTransitionRequest]'
    }

    attribute_map = {
        'corporate_action_code': 'corporateActionCode',
        'description': 'description',
        'announcement_date': 'announcementDate',
        'ex_date': 'exDate',
        'record_date': 'recordDate',
        'payment_date': 'paymentDate',
        'transitions': 'transitions'
    }

    required_map = {
        'corporate_action_code': 'required',
        'description': 'optional',
        'announcement_date': 'required',
        'ex_date': 'required',
        'record_date': 'required',
        'payment_date': 'required',
        'transitions': 'required'
    }

    def __init__(self, corporate_action_code=None, description=None, announcement_date=None, ex_date=None, record_date=None, payment_date=None, transitions=None):  # noqa: E501
        """
        UpsertCorporateActionRequest - a model defined in OpenAPI

        :param corporate_action_code:  (required)
        :type corporate_action_code: str
        :param description: 
        :type description: str
        :param announcement_date:  (required)
        :type announcement_date: datetime
        :param ex_date:  (required)
        :type ex_date: datetime
        :param record_date:  (required)
        :type record_date: datetime
        :param payment_date:  (required)
        :type payment_date: datetime
        :param transitions:  (required)
        :type transitions: list[lusid.CorporateActionTransitionRequest]

        """  # noqa: E501

        self._corporate_action_code = None
        self._description = None
        self._announcement_date = None
        self._ex_date = None
        self._record_date = None
        self._payment_date = None
        self._transitions = None
        self.discriminator = None

        self.corporate_action_code = corporate_action_code
        self.description = description
        self.announcement_date = announcement_date
        self.ex_date = ex_date
        self.record_date = record_date
        self.payment_date = payment_date
        self.transitions = transitions

    @property
    def corporate_action_code(self):
        """Gets the corporate_action_code of this UpsertCorporateActionRequest.  # noqa: E501


        :return: The corporate_action_code of this UpsertCorporateActionRequest.  # noqa: E501
        :rtype: str
        """
        return self._corporate_action_code

    @corporate_action_code.setter
    def corporate_action_code(self, corporate_action_code):
        """Sets the corporate_action_code of this UpsertCorporateActionRequest.


        :param corporate_action_code: The corporate_action_code of this UpsertCorporateActionRequest.  # noqa: E501
        :type: str
        """
        if corporate_action_code is None:
            raise ValueError("Invalid value for `corporate_action_code`, must not be `None`")  # noqa: E501

        self._corporate_action_code = corporate_action_code

    @property
    def description(self):
        """Gets the description of this UpsertCorporateActionRequest.  # noqa: E501


        :return: The description of this UpsertCorporateActionRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpsertCorporateActionRequest.


        :param description: The description of this UpsertCorporateActionRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def announcement_date(self):
        """Gets the announcement_date of this UpsertCorporateActionRequest.  # noqa: E501


        :return: The announcement_date of this UpsertCorporateActionRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._announcement_date

    @announcement_date.setter
    def announcement_date(self, announcement_date):
        """Sets the announcement_date of this UpsertCorporateActionRequest.


        :param announcement_date: The announcement_date of this UpsertCorporateActionRequest.  # noqa: E501
        :type: datetime
        """
        if announcement_date is None:
            raise ValueError("Invalid value for `announcement_date`, must not be `None`")  # noqa: E501

        self._announcement_date = announcement_date

    @property
    def ex_date(self):
        """Gets the ex_date of this UpsertCorporateActionRequest.  # noqa: E501


        :return: The ex_date of this UpsertCorporateActionRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._ex_date

    @ex_date.setter
    def ex_date(self, ex_date):
        """Sets the ex_date of this UpsertCorporateActionRequest.


        :param ex_date: The ex_date of this UpsertCorporateActionRequest.  # noqa: E501
        :type: datetime
        """
        if ex_date is None:
            raise ValueError("Invalid value for `ex_date`, must not be `None`")  # noqa: E501

        self._ex_date = ex_date

    @property
    def record_date(self):
        """Gets the record_date of this UpsertCorporateActionRequest.  # noqa: E501


        :return: The record_date of this UpsertCorporateActionRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._record_date

    @record_date.setter
    def record_date(self, record_date):
        """Sets the record_date of this UpsertCorporateActionRequest.


        :param record_date: The record_date of this UpsertCorporateActionRequest.  # noqa: E501
        :type: datetime
        """
        if record_date is None:
            raise ValueError("Invalid value for `record_date`, must not be `None`")  # noqa: E501

        self._record_date = record_date

    @property
    def payment_date(self):
        """Gets the payment_date of this UpsertCorporateActionRequest.  # noqa: E501


        :return: The payment_date of this UpsertCorporateActionRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._payment_date

    @payment_date.setter
    def payment_date(self, payment_date):
        """Sets the payment_date of this UpsertCorporateActionRequest.


        :param payment_date: The payment_date of this UpsertCorporateActionRequest.  # noqa: E501
        :type: datetime
        """
        if payment_date is None:
            raise ValueError("Invalid value for `payment_date`, must not be `None`")  # noqa: E501

        self._payment_date = payment_date

    @property
    def transitions(self):
        """Gets the transitions of this UpsertCorporateActionRequest.  # noqa: E501


        :return: The transitions of this UpsertCorporateActionRequest.  # noqa: E501
        :rtype: list[CorporateActionTransitionRequest]
        """
        return self._transitions

    @transitions.setter
    def transitions(self, transitions):
        """Sets the transitions of this UpsertCorporateActionRequest.


        :param transitions: The transitions of this UpsertCorporateActionRequest.  # noqa: E501
        :type: list[CorporateActionTransitionRequest]
        """
        if transitions is None:
            raise ValueError("Invalid value for `transitions`, must not be `None`")  # noqa: E501

        self._transitions = transitions

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
        if not isinstance(other, UpsertCorporateActionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
