
from Components.httpClient import HttpClient
from Constants.constants import constants
import json

if __name__=='__main__':
    httpClient = HttpClient(constants.getApiEndpointUrl() + "/starships/9/")
    response = httpClient.get()
    print(json.loads(response.data.decode('utf-8')))