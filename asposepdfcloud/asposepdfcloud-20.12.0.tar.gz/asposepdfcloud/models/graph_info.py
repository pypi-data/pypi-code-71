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


class GraphInfo(object):
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
        'line_width': 'float',
        'color': 'Color',
        'dash_array': 'list[int]',
        'dash_phase': 'int',
        'fill_color': 'Color',
        'is_doubled': 'bool',
        'skew_angle_x': 'float',
        'skew_angle_y': 'float',
        'scaling_rate_x': 'float',
        'scaling_rate_y': 'float',
        'rotation_angle': 'float'
    }

    attribute_map = {
        'line_width': 'LineWidth',
        'color': 'Color',
        'dash_array': 'DashArray',
        'dash_phase': 'DashPhase',
        'fill_color': 'FillColor',
        'is_doubled': 'IsDoubled',
        'skew_angle_x': 'SkewAngleX',
        'skew_angle_y': 'SkewAngleY',
        'scaling_rate_x': 'ScalingRateX',
        'scaling_rate_y': 'ScalingRateY',
        'rotation_angle': 'RotationAngle'
    }

    def __init__(self, line_width=None, color=None, dash_array=None, dash_phase=None, fill_color=None, is_doubled=None, skew_angle_x=None, skew_angle_y=None, scaling_rate_x=None, scaling_rate_y=None, rotation_angle=None):
        """
        GraphInfo - a model defined in Swagger
        """

        self._line_width = None
        self._color = None
        self._dash_array = None
        self._dash_phase = None
        self._fill_color = None
        self._is_doubled = None
        self._skew_angle_x = None
        self._skew_angle_y = None
        self._scaling_rate_x = None
        self._scaling_rate_y = None
        self._rotation_angle = None

        if line_width is not None:
          self.line_width = line_width
        if color is not None:
          self.color = color
        if dash_array is not None:
          self.dash_array = dash_array
        if dash_phase is not None:
          self.dash_phase = dash_phase
        if fill_color is not None:
          self.fill_color = fill_color
        if is_doubled is not None:
          self.is_doubled = is_doubled
        if skew_angle_x is not None:
          self.skew_angle_x = skew_angle_x
        if skew_angle_y is not None:
          self.skew_angle_y = skew_angle_y
        if scaling_rate_x is not None:
          self.scaling_rate_x = scaling_rate_x
        if scaling_rate_y is not None:
          self.scaling_rate_y = scaling_rate_y
        if rotation_angle is not None:
          self.rotation_angle = rotation_angle

    @property
    def line_width(self):
        """
        Gets the line_width of this GraphInfo.
        Gets or sets a float value that indicates the line width of the graph.

        :return: The line_width of this GraphInfo.
        :rtype: float
        """
        return self._line_width

    @line_width.setter
    def line_width(self, line_width):
        """
        Sets the line_width of this GraphInfo.
        Gets or sets a float value that indicates the line width of the graph.

        :param line_width: The line_width of this GraphInfo.
        :type: float
        """

        self._line_width = line_width

    @property
    def color(self):
        """
        Gets the color of this GraphInfo.
        Gets or sets a Color object that indicates the color of the graph.

        :return: The color of this GraphInfo.
        :rtype: Color
        """
        return self._color

    @color.setter
    def color(self, color):
        """
        Sets the color of this GraphInfo.
        Gets or sets a Color object that indicates the color of the graph.

        :param color: The color of this GraphInfo.
        :type: Color
        """

        self._color = color

    @property
    def dash_array(self):
        """
        Gets the dash_array of this GraphInfo.
        Gets or sets a dash array.

        :return: The dash_array of this GraphInfo.
        :rtype: list[int]
        """
        return self._dash_array

    @dash_array.setter
    def dash_array(self, dash_array):
        """
        Sets the dash_array of this GraphInfo.
        Gets or sets a dash array.

        :param dash_array: The dash_array of this GraphInfo.
        :type: list[int]
        """

        self._dash_array = dash_array

    @property
    def dash_phase(self):
        """
        Gets the dash_phase of this GraphInfo.
        Gets or sets a dash phase.

        :return: The dash_phase of this GraphInfo.
        :rtype: int
        """
        return self._dash_phase

    @dash_phase.setter
    def dash_phase(self, dash_phase):
        """
        Sets the dash_phase of this GraphInfo.
        Gets or sets a dash phase.

        :param dash_phase: The dash_phase of this GraphInfo.
        :type: int
        """

        self._dash_phase = dash_phase

    @property
    def fill_color(self):
        """
        Gets the fill_color of this GraphInfo.
        Gets or sets a Color object that indicates the fill color of the graph.

        :return: The fill_color of this GraphInfo.
        :rtype: Color
        """
        return self._fill_color

    @fill_color.setter
    def fill_color(self, fill_color):
        """
        Sets the fill_color of this GraphInfo.
        Gets or sets a Color object that indicates the fill color of the graph.

        :param fill_color: The fill_color of this GraphInfo.
        :type: Color
        """

        self._fill_color = fill_color

    @property
    def is_doubled(self):
        """
        Gets the is_doubled of this GraphInfo.
        Gets or sets is border doubled.

        :return: The is_doubled of this GraphInfo.
        :rtype: bool
        """
        return self._is_doubled

    @is_doubled.setter
    def is_doubled(self, is_doubled):
        """
        Sets the is_doubled of this GraphInfo.
        Gets or sets is border doubled.

        :param is_doubled: The is_doubled of this GraphInfo.
        :type: bool
        """

        self._is_doubled = is_doubled

    @property
    def skew_angle_x(self):
        """
        Gets the skew_angle_x of this GraphInfo.
        Gets or sets a float value that indicates the skew angle of the x-coordinate when transforming a coordinate system.

        :return: The skew_angle_x of this GraphInfo.
        :rtype: float
        """
        return self._skew_angle_x

    @skew_angle_x.setter
    def skew_angle_x(self, skew_angle_x):
        """
        Sets the skew_angle_x of this GraphInfo.
        Gets or sets a float value that indicates the skew angle of the x-coordinate when transforming a coordinate system.

        :param skew_angle_x: The skew_angle_x of this GraphInfo.
        :type: float
        """

        self._skew_angle_x = skew_angle_x

    @property
    def skew_angle_y(self):
        """
        Gets the skew_angle_y of this GraphInfo.
        Gets or sets a float value that indicates the skew angle of the y-coordinate when transforming a coordinate system.

        :return: The skew_angle_y of this GraphInfo.
        :rtype: float
        """
        return self._skew_angle_y

    @skew_angle_y.setter
    def skew_angle_y(self, skew_angle_y):
        """
        Sets the skew_angle_y of this GraphInfo.
        Gets or sets a float value that indicates the skew angle of the y-coordinate when transforming a coordinate system.

        :param skew_angle_y: The skew_angle_y of this GraphInfo.
        :type: float
        """

        self._skew_angle_y = skew_angle_y

    @property
    def scaling_rate_x(self):
        """
        Gets the scaling_rate_x of this GraphInfo.
        Gets or sets a float value that indicates the scaling rate of the x-coordinate when transforming a coordinate system.

        :return: The scaling_rate_x of this GraphInfo.
        :rtype: float
        """
        return self._scaling_rate_x

    @scaling_rate_x.setter
    def scaling_rate_x(self, scaling_rate_x):
        """
        Sets the scaling_rate_x of this GraphInfo.
        Gets or sets a float value that indicates the scaling rate of the x-coordinate when transforming a coordinate system.

        :param scaling_rate_x: The scaling_rate_x of this GraphInfo.
        :type: float
        """

        self._scaling_rate_x = scaling_rate_x

    @property
    def scaling_rate_y(self):
        """
        Gets the scaling_rate_y of this GraphInfo.
        Gets or sets a float value that indicates the scaling rate of the y-coordinate when transforming a coordinate system.

        :return: The scaling_rate_y of this GraphInfo.
        :rtype: float
        """
        return self._scaling_rate_y

    @scaling_rate_y.setter
    def scaling_rate_y(self, scaling_rate_y):
        """
        Sets the scaling_rate_y of this GraphInfo.
        Gets or sets a float value that indicates the scaling rate of the y-coordinate when transforming a coordinate system.

        :param scaling_rate_y: The scaling_rate_y of this GraphInfo.
        :type: float
        """

        self._scaling_rate_y = scaling_rate_y

    @property
    def rotation_angle(self):
        """
        Gets the rotation_angle of this GraphInfo.
        Gets or sets a float value that indicates the rotation angle of the coordinate system  when transforming a coordinate system.

        :return: The rotation_angle of this GraphInfo.
        :rtype: float
        """
        return self._rotation_angle

    @rotation_angle.setter
    def rotation_angle(self, rotation_angle):
        """
        Sets the rotation_angle of this GraphInfo.
        Gets or sets a float value that indicates the rotation angle of the coordinate system  when transforming a coordinate system.

        :param rotation_angle: The rotation_angle of this GraphInfo.
        :type: float
        """

        self._rotation_angle = rotation_angle

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
        if not isinstance(other, GraphInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
