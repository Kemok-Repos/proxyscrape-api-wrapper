""" Http client tests """

import unittest
import requests
from unittest.mock import patch
from client.http_client import HttpClient


class TestHttpClient(unittest.TestCase):
    """  HttpClient test class """

    @patch('client.http_client.HttpClient.request')
    def test_request_returns_dict_when_url_and_verb_given(self, mock_request):
        """ Tests get a dictionary from request """
        mock_request.return_value = {}
        response = HttpClient().request('GET', 'https://anyurltotest.inhere')

        self.assertIsInstance(response, dict)

    def test_request_raise_typeerror_exception_when_missing_arguments(self):
        """ Raise TypeError when missing arguments"""
        with self.assertRaises(TypeError):
            HttpClient().request()

    @patch('client.http_client.HttpClient.request')
    def test_request_raise_timeout_exception(self, mock_request):
        """ Raise exception when timeout occurs """
        mock_request.side_effect = requests.exceptions.Timeout()

        self.assertRaises(requests.exceptions.Timeout, mock_request)

    @patch('client.http_client.HttpClient.request')
    def test_request_raise_request_exception(self, mock_request):
        """ Raise exception when theres a request error  """
        mock_request.side_effect = requests.exceptions.RequestException()

        self.assertRaises(requests.exceptions.RequestException, mock_request)
        