""" API Wrapper for Proxyscrape """
from .http_client import HttpClient
from multiprocessing.shared_memory import ShareableList


class ProxyScrapeClientV2:
    """ Base class to make API calls """

    def __init__(self, api_key: str):
        self.api_key = api_key
        self._proxy_data_name = f'ProxyScrapeData_{api_key}'
        self.http = HttpClient("https://api.proxyscrape.com/v2/account/datacenter_shared/")
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
        response = self.http.get('proxy-list', self.params)
        return response.text.split()

    def load(self):
        """ Get a list of proxies """
        if self._proxy_data:
            self._proxy_data.shm.unlink()

        data = self.get_proxy_list() + [0]
        self._proxy_data = ShareableList(data, name=self._proxy_data_name)

    def next_proxy(self, cyclic: bool = False) -> str:
        """ returns the first ip not used previously,
        if cyclic is true all ip was used then returns the first and start again
        else if cyclic is false and all ip was used then start again after request ips"""
        if not len(self._proxy_data):
            self.load()
        ip = self._proxy_data[self._proxy_data[-1]]
        if self._proxy_data[-1] < 999:
            self._proxy_data[-1] += 1
        elif cyclic:
            self._proxy_data[-1] = 0
        else:
            self.load()
        return ip

    def __del__(self):
        if self._proxy_data:
            self._proxy_data.shm.close()
