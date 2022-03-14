""" API Wrapper for Proxyscrape """
import random
from .http_client import HttpClient
from multiprocessing.shared_memory import ShareableList, SharedMemory


class ProxyScrape:
    proxy_index = SharedMemory(name='ProxyScrapeIndex')
    proxy_list = ShareableList([], name='ProxyScrapeList')

    """ Base class to make API calls """
    def __init__(self, api_key: str, api_url: str = None):
        self.api_key = api_key
        self.http = HttpClient(api_url or "https://api.proxyscrape.com/v2/account/datacenter_shared/")

    @property
    def params(self):
        return {
            'type': 'getproxies',
            'country': 'all',
            'protocol': 'http',
            'format': 'normal',
            'auth': self.api_key
        }

    def get_proxy_list(self):
        """ Get a list of proxies """
        response = self.http.get('proxy-list', self.params)
        self.proxy_list = response.text.split()
        self.proxy_index = 0

    @property
    def proxy(self):
        """ Get a proxy from list """
        ip = self.proxy_List[self.proxy_index]
        self.proxy_index += 1
        return ip
