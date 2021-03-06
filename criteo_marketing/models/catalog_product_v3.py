# coding: utf-8

"""
    Marketing API v.1.0

    IMPORTANT: This swagger links to Criteo production environment. Any test applied here will thus impact real campaigns.  # noqa: E501

    The version of the OpenAPI document: v.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class CatalogProductV3(object):
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
        'batch_id': 'int',
        'merchant_id': 'str',
        'method': 'str',
        'product_id': 'str',
        'product': 'GoogleProductV3',
        'feed_id': 'str'
    }

    attribute_map = {
        'batch_id': 'batchId',
        'merchant_id': 'merchantId',
        'method': 'method',
        'product_id': 'productId',
        'product': 'product',
        'feed_id': 'feedId'
    }

    def __init__(self, batch_id=None, merchant_id=None, method=None, product_id=None, product=None, feed_id=None):  # noqa: E501
        """CatalogProductV3 - a model defined in OpenAPI"""  # noqa: E501

        self._batch_id = None
        self._merchant_id = None
        self._method = None
        self._product_id = None
        self._product = None
        self._feed_id = None
        self.discriminator = None

        if batch_id is not None:
            self.batch_id = batch_id
        if merchant_id is not None:
            self.merchant_id = merchant_id
        if method is not None:
            self.method = method
        if product_id is not None:
            self.product_id = product_id
        if product is not None:
            self.product = product
        if feed_id is not None:
            self.feed_id = feed_id

    @property
    def batch_id(self):
        """Gets the batch_id of this CatalogProductV3.  # noqa: E501

        An entry ID, unique within the batch request.  # noqa: E501

        :return: The batch_id of this CatalogProductV3.  # noqa: E501
        :rtype: int
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        """Sets the batch_id of this CatalogProductV3.

        An entry ID, unique within the batch request.  # noqa: E501

        :param batch_id: The batch_id of this CatalogProductV3.  # noqa: E501
        :type: int
        """

        self._batch_id = batch_id

    @property
    def merchant_id(self):
        """Gets the merchant_id of this CatalogProductV3.  # noqa: E501

        The ID of the managing account.  # noqa: E501

        :return: The merchant_id of this CatalogProductV3.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this CatalogProductV3.

        The ID of the managing account.  # noqa: E501

        :param merchant_id: The merchant_id of this CatalogProductV3.  # noqa: E501
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def method(self):
        """Gets the method of this CatalogProductV3.  # noqa: E501

        The method of the batch entry.  # noqa: E501

        :return: The method of this CatalogProductV3.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this CatalogProductV3.

        The method of the batch entry.  # noqa: E501

        :param method: The method of this CatalogProductV3.  # noqa: E501
        :type: str
        """

        self._method = method

    @property
    def product_id(self):
        """Gets the product_id of this CatalogProductV3.  # noqa: E501

        The ID of the product to get or delete. Only defined if the method is get or delete.  # noqa: E501

        :return: The product_id of this CatalogProductV3.  # noqa: E501
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this CatalogProductV3.

        The ID of the product to get or delete. Only defined if the method is get or delete.  # noqa: E501

        :param product_id: The product_id of this CatalogProductV3.  # noqa: E501
        :type: str
        """

        self._product_id = product_id

    @property
    def product(self):
        """Gets the product of this CatalogProductV3.  # noqa: E501


        :return: The product of this CatalogProductV3.  # noqa: E501
        :rtype: GoogleProductV3
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this CatalogProductV3.


        :param product: The product of this CatalogProductV3.  # noqa: E501
        :type: GoogleProductV3
        """

        self._product = product

    @property
    def feed_id(self):
        """Gets the feed_id of this CatalogProductV3.  # noqa: E501

        The Content API feed id.  # noqa: E501

        :return: The feed_id of this CatalogProductV3.  # noqa: E501
        :rtype: str
        """
        return self._feed_id

    @feed_id.setter
    def feed_id(self, feed_id):
        """Sets the feed_id of this CatalogProductV3.

        The Content API feed id.  # noqa: E501

        :param feed_id: The feed_id of this CatalogProductV3.  # noqa: E501
        :type: str
        """

        self._feed_id = feed_id

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
        if not isinstance(other, CatalogProductV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
