import requests
import json
from keypath import *

# api_key={chave_API}
# primary_release_year=1980&language=en
n = 0
url = f"{url}/genre/movie/list?&api_key={chave_API}"

headers = {
    "accept": "application/json",
    "Authorization": f"{Code}"
}
# . headers=headers
response = requests.get(url)
response = response.json()
response_name = response['genres']
tamanho = len(response_name)
while n < tamanho:
    abe = response_name[n]
    abaa = abe['name']
    print(abaa)
    n += 1
