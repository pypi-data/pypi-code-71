# coding: utf-8

"""
    Aspose.PDF Cloud API Reference


   Copyright (c) 2020 Aspose.PDF Cloud
 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:
 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.
 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.



    OpenAPI spec version: 3.0
    
"""


from pprint import pformat
from six import iteritems
import re


class StampInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'links': 'list[Link]',
        'id': 'str',
        'index_on_page': 'int',
        'page_index': 'int',
        'rect': 'Rectangle',
        'text': 'str',
        'visible': 'bool',
        'stamp_type': 'StampType'
    }

    attribute_map = {
        'links': 'Links',
        'id': 'Id',
        'index_on_page': 'IndexOnPage',
        'page_index': 'PageIndex',
        'rect': 'Rect',
        'text': 'Text',
        'visible': 'Visible',
        'stamp_type': 'StampType'
    }

    def __init__(self, links=None, id=None, index_on_page=None, page_index=None, rect=None, text=None, visible=None, stamp_type=None):
        """
        StampInfo - a model defined in Swagger
        """

        self._links = None
        self._id = None
        self._index_on_page = None
        self._page_index = None
        self._rect = None
        self._text = None
        self._visible = None
        self._stamp_type = None

        if links is not None:
          self.links = links
        if id is not None:
          self.id = id
        if index_on_page is not None:
          self.index_on_page = index_on_page
        if page_index is not None:
          self.page_index = page_index
        if rect is not None:
          self.rect = rect
        if text is not None:
          self.text = text
        if visible is not None:
          self.visible = visible
        self.stamp_type = stamp_type

    @property
    def links(self):
        """
        Gets the links of this StampInfo.
        Link to the document.

        :return: The links of this StampInfo.
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this StampInfo.
        Link to the document.

        :param links: The links of this StampInfo.
        :type: list[Link]
        """

        self._links = links

    @property
    def id(self):
        """
        Gets the id of this StampInfo.
        Gets ID of the stamp.

        :return: The id of this StampInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this StampInfo.
        Gets ID of the stamp.

        :param id: The id of this StampInfo.
        :type: str
        """

        self._id = id

    @property
    def index_on_page(self):
        """
        Gets the index_on_page of this StampInfo.
        Gets index on page of the stamp.

        :return: The index_on_page of this StampInfo.
        :rtype: int
        """
        return self._index_on_page

    @index_on_page.setter
    def index_on_page(self, index_on_page):
        """
        Sets the index_on_page of this StampInfo.
        Gets index on page of the stamp.

        :param index_on_page: The index_on_page of this StampInfo.
        :type: int
        """

        self._index_on_page = index_on_page

    @property
    def page_index(self):
        """
        Gets the page_index of this StampInfo.
        Gets PageIndex of the annotation.

        :return: The page_index of this StampInfo.
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        """
        Sets the page_index of this StampInfo.
        Gets PageIndex of the annotation.

        :param page_index: The page_index of this StampInfo.
        :type: int
        """

        self._page_index = page_index

    @property
    def rect(self):
        """
        Gets the rect of this StampInfo.
        Gets Rect of the annotation.

        :return: The rect of this StampInfo.
        :rtype: Rectangle
        """
        return self._rect

    @rect.setter
    def rect(self, rect):
        """
        Sets the rect of this StampInfo.
        Gets Rect of the annotation.

        :param rect: The rect of this StampInfo.
        :type: Rectangle
        """

        self._rect = rect

    @property
    def text(self):
        """
        Gets the text of this StampInfo.
        Get the text content.

        :return: The text of this StampInfo.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this StampInfo.
        Get the text content.

        :param text: The text of this StampInfo.
        :type: str
        """

        self._text = text

    @property
    def visible(self):
        """
        Gets the visible of this StampInfo.
        Gets the stamp is visible.

        :return: The visible of this StampInfo.
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """
        Sets the visible of this StampInfo.
        Gets the stamp is visible.

        :param visible: The visible of this StampInfo.
        :type: bool
        """

        self._visible = visible

    @property
    def stamp_type(self):
        """
        Gets the stamp_type of this StampInfo.
        Gets stamp type.

        :return: The stamp_type of this StampInfo.
        :rtype: StampType
        """
        return self._stamp_type

    @stamp_type.setter
    def stamp_type(self, stamp_type):
        """
        Sets the stamp_type of this StampInfo.
        Gets stamp type.

        :param stamp_type: The stamp_type of this StampInfo.
        :type: StampType
        """
        if stamp_type is None:
            raise ValueError("Invalid value for `stamp_type`, must not be `None`")

        self._stamp_type = stamp_type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, StampInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
