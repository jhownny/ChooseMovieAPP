import API_Settings.keypath
from API_Settings.keypath import *

import requests

import PuxandoFilmesAPI

url = f"{API_Settings.keypath.siteURL}/discover/movie?include_adult=true&include_video=false&language=pt&page=1&with_genres=action&api_key={API_Settings.keypath.chave_API}"
headers = {
    "accept": "application/json",
    "Authorization": f"{API_Settings.keypath.Code}"
}

response = requests.get(url)
response = response.json()

print(response)
