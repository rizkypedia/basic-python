
from Components.car import Car
from Components.httpClient import HttpClient
import json

if __name__=='__main__':
    car = Car('Renault', 'coupe','1966')
    print(car.get_details())
    httpClient = HttpClient('https://swapi.dev/api/starships/9/')
    response = httpClient.get()
    print(json.loads(response.data.decode('utf-8')))