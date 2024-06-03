import API_Settings.keypath
from API_Settings.keypath import *
import requests

def API_Movie():

    url = f"{API_Settings.keypath.webURL}/genre/movie/list?&language=pt-BR&api_key={API_Settings.keypath.key_API}"
    headers = {
        "accept": "application/json",
        "Authorization": f"{API_Settings.keypath.Code}"
    }

    response = requests.get(url)
    response = response.json()

    response_name = response['genres']
    outnumber = 0
    ListGener = ['Aleatorio']
    length = len(response_name)

    while True:
        if outnumber < length:
            FirstStep = response_name[outnumber]
            ListGener.append(FirstStep['name'])
            outnumber += 1
        else:
            return ListGener
            break
