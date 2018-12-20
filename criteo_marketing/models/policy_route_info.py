# coding: utf-8

"""
    Marketing API v.1.0

    IMPORTANT: This swagger links to Criteo production environment. Any test applied here will thus impact real campaigns.  # noqa: E501

    OpenAPI spec version: v.1.0
    Generated by: https://openapi-generator.tech
"""


import logging
import pprint
import re  # noqa: F401

import six

logger = logging.getLogger(__name__)


class PolicyRouteInfo(object):
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
        'route': 'str',
        'method': 'str',
        'controller_name': 'str',
        'action_name': 'str'
    }

    attribute_map = {
        'route': 'route',
        'method': 'method',
        'controller_name': 'controllerName',
        'action_name': 'actionName'
    }

    def __init__(self, route=None, method=None, controller_name=None, action_name=None):  # noqa: E501
        """PolicyRouteInfo - a model defined in OpenAPI"""  # noqa: E501

        self._route = None
        self._method = None
        self._controller_name = None
        self._action_name = None
        self.discriminator = None

        if route is not None:
            self.route = route
        if method is not None:
            self.method = method
        if controller_name is not None:
            self.controller_name = controller_name
        if action_name is not None:
            self.action_name = action_name

    @property
    def route(self):
        """Gets the route of this PolicyRouteInfo.  # noqa: E501


        :return: The route of this PolicyRouteInfo.  # noqa: E501
        :rtype: str
        """
        return self._route

    @route.setter
    def route(self, route):
        """Sets the route of this PolicyRouteInfo.


        :param route: The route of this PolicyRouteInfo.  # noqa: E501
        :type: str
        """

        self._route = route

    @property
    def method(self):
        """Gets the method of this PolicyRouteInfo.  # noqa: E501


        :return: The method of this PolicyRouteInfo.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this PolicyRouteInfo.


        :param method: The method of this PolicyRouteInfo.  # noqa: E501
        :type: str
        """

        self._method = method

    @property
    def controller_name(self):
        """Gets the controller_name of this PolicyRouteInfo.  # noqa: E501


        :return: The controller_name of this PolicyRouteInfo.  # noqa: E501
        :rtype: str
        """
        return self._controller_name

    @controller_name.setter
    def controller_name(self, controller_name):
        """Sets the controller_name of this PolicyRouteInfo.


        :param controller_name: The controller_name of this PolicyRouteInfo.  # noqa: E501
        :type: str
        """

        self._controller_name = controller_name

    @property
    def action_name(self):
        """Gets the action_name of this PolicyRouteInfo.  # noqa: E501


        :return: The action_name of this PolicyRouteInfo.  # noqa: E501
        :rtype: str
        """
        return self._action_name

    @action_name.setter
    def action_name(self, action_name):
        """Sets the action_name of this PolicyRouteInfo.


        :param action_name: The action_name of this PolicyRouteInfo.  # noqa: E501
        :type: str
        """

        self._action_name = action_name

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
        if not isinstance(other, PolicyRouteInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
