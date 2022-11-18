# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_alarms_controller_create(self):
        """Test case for alarms_controller_create

        
        """
        response = self.client.open(
            '/api/alarms',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_alarms_controller_delete(self):
        """Test case for alarms_controller_delete

        
        """
        response = self.client.open(
            '/api/alarms/{id}'.format(id=None),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_alarms_controller_find(self):
        """Test case for alarms_controller_find

        
        """
        query_string = [('ProductInstanceUri', None)]
        response = self.client.open(
            '/api/alarms',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_alarms_controller_update(self):
        """Test case for alarms_controller_update

        
        """
        response = self.client.open(
            '/api/alarms/{id}'.format(id=None),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_app_controller_get_hello(self):
        """Test case for app_controller_get_hello

        
        """
        response = self.client.open(
            '/api',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_assets_controller_create(self):
        """Test case for assets_controller_create

        
        """
        response = self.client.open(
            '/api/assets',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_assets_controller_delete(self):
        """Test case for assets_controller_delete

        
        """
        query_string = [('ProductInstanceUri', None)]
        response = self.client.open(
            '/api/assets',
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_assets_controller_find(self):
        """Test case for assets_controller_find

        
        """
        query_string = [('ProductInstanceUri', None),
                        ('PublisherInstanceUri', None)]
        response = self.client.open(
            '/api/assets',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_events_controller_create(self):
        """Test case for events_controller_create

        
        """
        response = self.client.open(
            '/api/events',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_events_controller_find(self):
        """Test case for events_controller_find

        
        """
        query_string = [('ProductInstanceUri', None)]
        response = self.client.open(
            '/api/events',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
