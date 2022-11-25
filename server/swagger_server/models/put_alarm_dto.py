# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class PutAlarmDto(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, product_instance_uri: str=None, description: str=None, severity: str=None, status: str=None):  # noqa: E501
        """PutAlarmDto - a model defined in Swagger

        :param product_instance_uri: The product_instance_uri of this PutAlarmDto.  # noqa: E501
        :type product_instance_uri: str
        :param description: The description of this PutAlarmDto.  # noqa: E501
        :type description: str
        :param severity: The severity of this PutAlarmDto.  # noqa: E501
        :type severity: str
        :param status: The status of this PutAlarmDto.  # noqa: E501
        :type status: str
        """
        self.swagger_types = {
            'product_instance_uri': str,
            'description': str,
            'severity': str,
            'status': str
        }

        self.attribute_map = {
            'product_instance_uri': 'ProductInstanceUri',
            'description': 'description',
            'severity': 'severity',
            'status': 'status'
        }

        self._product_instance_uri = product_instance_uri
        self._description = description
        self._severity = severity
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'PutAlarmDto':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PutAlarmDto of this PutAlarmDto.  # noqa: E501
        :rtype: PutAlarmDto
        """
        return util.deserialize_model(dikt, cls)

    @property
    def product_instance_uri(self) -> str:
        """Gets the product_instance_uri of this PutAlarmDto.


        :return: The product_instance_uri of this PutAlarmDto.
        :rtype: str
        """
        return self._product_instance_uri

    @product_instance_uri.setter
    def product_instance_uri(self, product_instance_uri: str):
        """Sets the product_instance_uri of this PutAlarmDto.


        :param product_instance_uri: The product_instance_uri of this PutAlarmDto.
        :type product_instance_uri: str
        """

        self._product_instance_uri = product_instance_uri

    @property
    def description(self) -> str:
        """Gets the description of this PutAlarmDto.


        :return: The description of this PutAlarmDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this PutAlarmDto.


        :param description: The description of this PutAlarmDto.
        :type description: str
        """

        self._description = description

    @property
    def severity(self) -> str:
        """Gets the severity of this PutAlarmDto.


        :return: The severity of this PutAlarmDto.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity: str):
        """Sets the severity of this PutAlarmDto.


        :param severity: The severity of this PutAlarmDto.
        :type severity: str
        """

        self._severity = severity

    @property
    def status(self) -> str:
        """Gets the status of this PutAlarmDto.


        :return: The status of this PutAlarmDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this PutAlarmDto.


        :param status: The status of this PutAlarmDto.
        :type status: str
        """

        self._status = status
