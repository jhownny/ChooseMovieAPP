import requests
from keypath import *
# api_key={chave_API}

url = f"https://api.themoviedb.org/3/genre/movie/list?primary_release_year=1980&language=en&api_key={chave_API}"

headers = {
    "accept": "application/json",
    "Authorization": f"{Code}"
}

response = requests.get(url, headers=headers)

print(response.text)