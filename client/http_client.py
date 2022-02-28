""" Http client for requests """
import requests

class HttpClient:
    """ Base class to make http requests """
    def __init__(self):
        pass

    def request(self, verb:str, url:str, params:dict=None, custom_timeout:int=5):
        """ Make a http request """
        session = requests.Session()
        session.params = params

        try:
            response = session.request(verb, url, timeout=custom_timeout)
            response.raise_for_status()
        except requests.exceptions.Timeout as error_t:
            print("Timeout error:", error_t)
        except requests.exceptions.RequestException as error_re:
            print("Request error:", error_re)

        return {'status_code': response.status_code, 'text': response.text}
