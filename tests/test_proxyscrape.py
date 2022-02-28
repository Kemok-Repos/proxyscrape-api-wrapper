""" Http client tests """

import unittest
from unittest.mock import patch
from client.proxyscrape import ProxyScrape

class TestHttpClient(unittest.TestCase):
    """  Proxyscrape test class """

    @patch('client.proxyscrape.ProxyScrape.get_proxy_list')
    def test_get_proxy_list_returns_a_dict(self, mock_get_proxy_list):
        """ get_proxy_list returns a list of proxies """
        mock_get_proxy_list.return_value = []
        client = ProxyScrape('123')
        proxy_list = client.get_proxy_list()

        self.assertIsInstance(proxy_list, list)


    @patch('client.proxyscrape.ProxyScrape.get_proxy')
    def test_get_proxy_returns_a_str(self, mock_get_proxy):
        """ get_proxy returns a random proxy from list """
        mock_get_proxy.return_value = ''
        client = ProxyScrape('123')
        proxy = client.get_proxy()

        self.assertIsInstance(proxy, str)
