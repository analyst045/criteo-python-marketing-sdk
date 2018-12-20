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


class InlineResponse200(object):
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
        'access_token': 'str',
        'token_type': 'str',
        'expires_in': 'int'
    }

    attribute_map = {
        'access_token': 'access_token',
        'token_type': 'token_type',
        'expires_in': 'expires_in'
    }

    def __init__(self, access_token=None, token_type=None, expires_in=None):  # noqa: E501
        """InlineResponse200 - a model defined in OpenAPI"""  # noqa: E501

        self._access_token = None
        self._token_type = None
        self._expires_in = None
        self.discriminator = None

        if access_token is not None:
            self.access_token = access_token
        if token_type is not None:
            self.token_type = token_type
        if expires_in is not None:
            self.expires_in = expires_in

    @property
    def access_token(self):
        """Gets the access_token of this InlineResponse200.  # noqa: E501

        JWT to be used in to authenticate requests.  # noqa: E501

        :return: The access_token of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this InlineResponse200.

        JWT to be used in to authenticate requests.  # noqa: E501

        :param access_token: The access_token of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def token_type(self):
        """Gets the token_type of this InlineResponse200.  # noqa: E501

        Always bearer.  # noqa: E501

        :return: The token_type of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """Sets the token_type of this InlineResponse200.

        Always bearer.  # noqa: E501

        :param token_type: The token_type of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._token_type = token_type

    @property
    def expires_in(self):
        """Gets the expires_in of this InlineResponse200.  # noqa: E501

        Expiration time express in seconds.  # noqa: E501

        :return: The expires_in of this InlineResponse200.  # noqa: E501
        :rtype: int
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """Sets the expires_in of this InlineResponse200.

        Expiration time express in seconds.  # noqa: E501

        :param expires_in: The expires_in of this InlineResponse200.  # noqa: E501
        :type: int
        """

        self._expires_in = expires_in

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
        if not isinstance(other, InlineResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
