""" proxyscrape client tests """
import unittest
from unittest.mock import patch
from client.proxyscrape import ProxyScrapeClientV2


class TestHttpClient(unittest.TestCase):
    """  Proxyscrape test class """

    @patch('client.proxyscrape.ProxyScrapeClientV2.get_proxy_list')
    def test_get_proxy_list_returns_a_dict(self, mock_get_proxy_list):
        """ load set a list of proxies into the client """
        mock_get_proxy_list.return_value = []
        client = ProxyScrapeClientV2('123')
        proxy_list = client.get_proxy_list()

        self.assertIsInstance(proxy_list, list)

    @patch('client.proxyscrape.ProxyScrapeClientV2.next_proxy')
    def test_get_proxy_returns_a_str(self, mock_next_proxy):
        """ get_proxy returns a random proxy from list """
        mock_next_proxy.return_value = ''
        client = ProxyScrapeClientV2('123')
        proxy = client.next_proxy()

        self.assertIsInstance(proxy, str)
