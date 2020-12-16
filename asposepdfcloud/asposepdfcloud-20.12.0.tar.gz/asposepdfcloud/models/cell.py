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


class Cell(object):
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
        'is_no_border': 'bool',
        'margin': 'MarginInfo',
        'border': 'BorderInfo',
        'background_color': 'Color',
        'background_image_file': 'str',
        'background_image_storage_file': 'str',
        'alignment': 'HorizontalAlignment',
        'default_cell_text_state': 'TextState',
        'paragraphs': 'list[TextRect]',
        'is_word_wrapped': 'bool',
        'vertical_alignment': 'VerticalAlignment',
        'col_span': 'int',
        'row_span': 'int',
        'width': 'float',
        'html_fragment': 'str',
        'images': 'list[ImageFragment]'
    }

    attribute_map = {
        'is_no_border': 'IsNoBorder',
        'margin': 'Margin',
        'border': 'Border',
        'background_color': 'BackgroundColor',
        'background_image_file': 'BackgroundImageFile',
        'background_image_storage_file': 'BackgroundImageStorageFile',
        'alignment': 'Alignment',
        'default_cell_text_state': 'DefaultCellTextState',
        'paragraphs': 'Paragraphs',
        'is_word_wrapped': 'IsWordWrapped',
        'vertical_alignment': 'VerticalAlignment',
        'col_span': 'ColSpan',
        'row_span': 'RowSpan',
        'width': 'Width',
        'html_fragment': 'HtmlFragment',
        'images': 'Images'
    }

    def __init__(self, is_no_border=None, margin=None, border=None, background_color=None, background_image_file=None, background_image_storage_file=None, alignment=None, default_cell_text_state=None, paragraphs=None, is_word_wrapped=None, vertical_alignment=None, col_span=None, row_span=None, width=None, html_fragment=None, images=None):
        """
        Cell - a model defined in Swagger
        """

        self._is_no_border = None
        self._margin = None
        self._border = None
        self._background_color = None
        self._background_image_file = None
        self._background_image_storage_file = None
        self._alignment = None
        self._default_cell_text_state = None
        self._paragraphs = None
        self._is_word_wrapped = None
        self._vertical_alignment = None
        self._col_span = None
        self._row_span = None
        self._width = None
        self._html_fragment = None
        self._images = None

        if is_no_border is not None:
          self.is_no_border = is_no_border
        if margin is not None:
          self.margin = margin
        if border is not None:
          self.border = border
        if background_color is not None:
          self.background_color = background_color
        if background_image_file is not None:
          self.background_image_file = background_image_file
        if background_image_storage_file is not None:
          self.background_image_storage_file = background_image_storage_file
        if alignment is not None:
          self.alignment = alignment
        if default_cell_text_state is not None:
          self.default_cell_text_state = default_cell_text_state
        if paragraphs is not None:
          self.paragraphs = paragraphs
        if is_word_wrapped is not None:
          self.is_word_wrapped = is_word_wrapped
        if vertical_alignment is not None:
          self.vertical_alignment = vertical_alignment
        if col_span is not None:
          self.col_span = col_span
        if row_span is not None:
          self.row_span = row_span
        if width is not None:
          self.width = width
        if html_fragment is not None:
          self.html_fragment = html_fragment
        if images is not None:
          self.images = images

    @property
    def is_no_border(self):
        """
        Gets the is_no_border of this Cell.
        Gets or sets the cell have border.

        :return: The is_no_border of this Cell.
        :rtype: bool
        """
        return self._is_no_border

    @is_no_border.setter
    def is_no_border(self, is_no_border):
        """
        Sets the is_no_border of this Cell.
        Gets or sets the cell have border.

        :param is_no_border: The is_no_border of this Cell.
        :type: bool
        """

        self._is_no_border = is_no_border

    @property
    def margin(self):
        """
        Gets the margin of this Cell.
        Gets or sets the padding.

        :return: The margin of this Cell.
        :rtype: MarginInfo
        """
        return self._margin

    @margin.setter
    def margin(self, margin):
        """
        Sets the margin of this Cell.
        Gets or sets the padding.

        :param margin: The margin of this Cell.
        :type: MarginInfo
        """

        self._margin = margin

    @property
    def border(self):
        """
        Gets the border of this Cell.
        Gets or sets the border.

        :return: The border of this Cell.
        :rtype: BorderInfo
        """
        return self._border

    @border.setter
    def border(self, border):
        """
        Sets the border of this Cell.
        Gets or sets the border.

        :param border: The border of this Cell.
        :type: BorderInfo
        """

        self._border = border

    @property
    def background_color(self):
        """
        Gets the background_color of this Cell.
        Gets or sets the background color.

        :return: The background_color of this Cell.
        :rtype: Color
        """
        return self._background_color

    @background_color.setter
    def background_color(self, background_color):
        """
        Sets the background_color of this Cell.
        Gets or sets the background color.

        :param background_color: The background_color of this Cell.
        :type: Color
        """

        self._background_color = background_color

    @property
    def background_image_file(self):
        """
        Gets the background_image_file of this Cell.
        Gets or sets the background image file.

        :return: The background_image_file of this Cell.
        :rtype: str
        """
        return self._background_image_file

    @background_image_file.setter
    def background_image_file(self, background_image_file):
        """
        Sets the background_image_file of this Cell.
        Gets or sets the background image file.

        :param background_image_file: The background_image_file of this Cell.
        :type: str
        """

        self._background_image_file = background_image_file

    @property
    def background_image_storage_file(self):
        """
        Gets the background_image_storage_file of this Cell.
        Gets or sets path of the background image file from storage.

        :return: The background_image_storage_file of this Cell.
        :rtype: str
        """
        return self._background_image_storage_file

    @background_image_storage_file.setter
    def background_image_storage_file(self, background_image_storage_file):
        """
        Sets the background_image_storage_file of this Cell.
        Gets or sets path of the background image file from storage.

        :param background_image_storage_file: The background_image_storage_file of this Cell.
        :type: str
        """

        self._background_image_storage_file = background_image_storage_file

    @property
    def alignment(self):
        """
        Gets the alignment of this Cell.
        Gets or sets the alignment.

        :return: The alignment of this Cell.
        :rtype: HorizontalAlignment
        """
        return self._alignment

    @alignment.setter
    def alignment(self, alignment):
        """
        Sets the alignment of this Cell.
        Gets or sets the alignment.

        :param alignment: The alignment of this Cell.
        :type: HorizontalAlignment
        """

        self._alignment = alignment

    @property
    def default_cell_text_state(self):
        """
        Gets the default_cell_text_state of this Cell.
        Gets or sets the default cell text state.

        :return: The default_cell_text_state of this Cell.
        :rtype: TextState
        """
        return self._default_cell_text_state

    @default_cell_text_state.setter
    def default_cell_text_state(self, default_cell_text_state):
        """
        Sets the default_cell_text_state of this Cell.
        Gets or sets the default cell text state.

        :param default_cell_text_state: The default_cell_text_state of this Cell.
        :type: TextState
        """

        self._default_cell_text_state = default_cell_text_state

    @property
    def paragraphs(self):
        """
        Gets the paragraphs of this Cell.
        Gets or sets the cell's formatted text.

        :return: The paragraphs of this Cell.
        :rtype: list[TextRect]
        """
        return self._paragraphs

    @paragraphs.setter
    def paragraphs(self, paragraphs):
        """
        Sets the paragraphs of this Cell.
        Gets or sets the cell's formatted text.

        :param paragraphs: The paragraphs of this Cell.
        :type: list[TextRect]
        """

        self._paragraphs = paragraphs

    @property
    def is_word_wrapped(self):
        """
        Gets the is_word_wrapped of this Cell.
        Gets or sets the cell's text word wrapped.

        :return: The is_word_wrapped of this Cell.
        :rtype: bool
        """
        return self._is_word_wrapped

    @is_word_wrapped.setter
    def is_word_wrapped(self, is_word_wrapped):
        """
        Sets the is_word_wrapped of this Cell.
        Gets or sets the cell's text word wrapped.

        :param is_word_wrapped: The is_word_wrapped of this Cell.
        :type: bool
        """

        self._is_word_wrapped = is_word_wrapped

    @property
    def vertical_alignment(self):
        """
        Gets the vertical_alignment of this Cell.
        Gets or sets the vertical alignment.

        :return: The vertical_alignment of this Cell.
        :rtype: VerticalAlignment
        """
        return self._vertical_alignment

    @vertical_alignment.setter
    def vertical_alignment(self, vertical_alignment):
        """
        Sets the vertical_alignment of this Cell.
        Gets or sets the vertical alignment.

        :param vertical_alignment: The vertical_alignment of this Cell.
        :type: VerticalAlignment
        """

        self._vertical_alignment = vertical_alignment

    @property
    def col_span(self):
        """
        Gets the col_span of this Cell.
        Gets or sets the column span.

        :return: The col_span of this Cell.
        :rtype: int
        """
        return self._col_span

    @col_span.setter
    def col_span(self, col_span):
        """
        Sets the col_span of this Cell.
        Gets or sets the column span.

        :param col_span: The col_span of this Cell.
        :type: int
        """

        self._col_span = col_span

    @property
    def row_span(self):
        """
        Gets the row_span of this Cell.
        Gets or sets the row span.

        :return: The row_span of this Cell.
        :rtype: int
        """
        return self._row_span

    @row_span.setter
    def row_span(self, row_span):
        """
        Sets the row_span of this Cell.
        Gets or sets the row span.

        :param row_span: The row_span of this Cell.
        :type: int
        """

        self._row_span = row_span

    @property
    def width(self):
        """
        Gets the width of this Cell.
        Gets or sets the column width.

        :return: The width of this Cell.
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width of this Cell.
        Gets or sets the column width.

        :param width: The width of this Cell.
        :type: float
        """

        self._width = width

    @property
    def html_fragment(self):
        """
        Gets the html_fragment of this Cell.
        Gets or sets Html fragment.

        :return: The html_fragment of this Cell.
        :rtype: str
        """
        return self._html_fragment

    @html_fragment.setter
    def html_fragment(self, html_fragment):
        """
        Sets the html_fragment of this Cell.
        Gets or sets Html fragment.

        :param html_fragment: The html_fragment of this Cell.
        :type: str
        """

        self._html_fragment = html_fragment

    @property
    def images(self):
        """
        Gets the images of this Cell.
        Gets or sets ImageFragment list.

        :return: The images of this Cell.
        :rtype: list[ImageFragment]
        """
        return self._images

    @images.setter
    def images(self, images):
        """
        Sets the images of this Cell.
        Gets or sets ImageFragment list.

        :param images: The images of this Cell.
        :type: list[ImageFragment]
        """

        self._images = images

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
        if not isinstance(other, Cell):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
