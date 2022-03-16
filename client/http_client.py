""" Http client for requests """
from requests import Session


class HttpClient:
    """ Base class to make http requests """
    def __init__(self, url_base: str = None, verbose: bool = False):
        self.url_base = url_base
        if url_base and not url_base.endswith('/'):
            self.url_base += '/'

    def get(self, path: str, params: dict, timeout: int = None):
        return self.request('GET', path, params, timeout)

    def post(self, path: str, data: dict = None, timeout: int = None):
        return self.request('POST', path, data, timeout)

    def put(self, path: str, data: dict = None, timeout: int = None):
        return self.request('PUT', path, data, timeout)

    def delete(self, path: str, timeout: int = None):
        return self.request('DELETE', path, timeout=timeout)

    def request(self, method: str, path: str, data: dict = None, timeout: int = None):
        if path.startswith('/'):
            path = path[1:]
        url = f"{self.url_base}{path}" if self.url_base else path
        if method.lower().strip() == 'get':
            return Session().request(method, url, params=data, timeout=timeout)
        return Session().request(method, url, data=data, timeout=timeout)
