import requests
from keypath import chave_API
#api_key={chave_API}
url = f"https://api.themoviedb.org/3/genre/movie/list?primary_release_year=1980&language=enapi_key={chave_API}"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzMjQ3NmRhNGZhYWJkNWYwNzRiYTA4ODVkYjRhMWIzMCIsInN1YiI6IjY1MmFmYTBkZWE4NGM3MDEwYzFiYWY4YiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.4ghy1utaf22jXRsorcEp5N269QwYPa7muL_e_X8YzS4"
}

response = requests.get(url, headers=headers)

print(response.text)