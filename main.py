import requests
from pprint import pprint

API_Key = '2b107b9569a3156beb6135abad37c62d'

city = input("Enter a city: ")

base_url = "https://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)
