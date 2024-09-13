import requests
import API_Settings.keypath
from API_Settings.keypath import *
from datetime import datetime

def API_GenerMovie():
    url = f"{API_Settings.keypath.webURL}/genre/movie/list?&language=pt-BR&api_key={API_Settings.keypath.key_API}"
    headers = {
        "accept": "application/json",
        "Authorization": f"{API_Settings.keypath.Code}"
    }

    response = requests.get(url).json()
    genres = response['genres']
    genre_list = ['Movies']

    for genre in genres:
        genre_list.append(genre['name'])

    return genre_list

def API_YearMovie():
    current_year = datetime.now().year
    year_list = []
    start_year = 1985

    while True:
        if len(year_list) < (current_year - start_year + 1):
            year_list.append(str(start_year + len(year_list)))
        else:
            return year_list
            break