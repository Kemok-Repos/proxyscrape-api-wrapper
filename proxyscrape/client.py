""" API Wrapper for Proxyscrape """
import requests
from multiprocessing.shared_memory import ShareableList


class ProxyScrape:
    """ Base class to make API calls """

    def __init__(self, api_key: str, cyclic: bool = False):
        self.api_key = api_key
        self.cyclic = cyclic
        self._proxy_data_name = f'ProxyScrapeData_{api_key}'
        self.url_base = "https://api.proxyscrape.com/v2/account/datacenter_shared/"
        try:
            self._proxy_data = ShareableList(name=self._proxy_data_name)
        except:
            self._proxy_data = None
            self.load()

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
        return requests.get(f'{self.url_base}/proxy-list', params=self.params).text.split()

    def load(self):
        """ Get a list of proxies """
        if self._proxy_data:
            self._proxy_data.shm.unlink()

        data = self.get_proxy_list() + [0]
        self._proxy_data = ShareableList(data, name=self._proxy_data_name)

    @property
    def proxy(self):
        return self._proxy_data[self._proxy_data[-1]]

    def next_proxy(self) -> str:
        """ returns the first ip not used previously,
        if cyclic is true all ip was used then returns the first and start again
        else if cyclic is false and all ip was used then start again after request ips"""
        if not len(self._proxy_data):
            self.load()
        if self._proxy_data[-1] < 999:
            self._proxy_data[-1] += 1
        elif self.cyclic:
            self._proxy_data[-1] = 0
        else:
            self.load()
        return self.proxy

    def __del__(self):
        if self._proxy_data:
            self._proxy_data.shm.close()
