from http.client import HTTPResponse
import urllib3

class HttpClient:
    def __init__(self, targetUrl):
        self.targetUrl = targetUrl
        self.http = urllib3.PoolManager()
    def get(self)->HTTPResponse:
        return self.http.request('GET',self.targetUrl)