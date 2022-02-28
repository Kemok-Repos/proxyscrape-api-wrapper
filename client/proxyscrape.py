""" API Wrapper for Proxyscrape """
import random
from .http_client import HttpClient

class ProxyScrape:
    """ Base class to make API calls """
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.proxyscrape.com/v2/account/datacenter_shared/"

    def get_proxy_list(self):
        """ Get a list of proxies """
        params = {'type': 'getproxies', 'country': 'all',
                'protocol': 'http', 'format': 'normal',
                'auth': self.api_key}

        response = HttpClient().request('GET', self.base_url+'proxy-list', params)

        return response['text'].split()

    def get_proxy(self):
        """ Get a proxy from list """
        return random.choice(self.get_proxy_list())
