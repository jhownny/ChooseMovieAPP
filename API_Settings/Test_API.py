import requests
import json
import API_Settings.keypath


#url = f"https://{API_Settings.keypath.siteURL}/configuration/languages"
#
#headers = {
#    "accept": "application/json",
#    "Authorization": f"{API_Settings.keypath.Code}"
#}
#
#response = requests.get(url, headers=headers)
#response = response.json()
#
#for i in response:
#    print(i)



# api_key={chave_API}
# primary_release_year=1980&language=en

#url = f"{API_Settings.keypath.siteURL}/genre/movie/list?&api_key={API_Settings.keypath.chave_API}"
#headers = {
#    "accept": "application/json",
#    "Authorization": f"{API_Settings.keypath.Code}"
#}
## . headers=headers
#response = requests.get(url)
#response = response.json()
#response_name = response['genres']
#n = 0
#aba = []
#lenth = len(response_name)
#while n < lenth:
#    abe = response_name[n]
#    aba.append(abe['name'])
#    n += 1
#    if n == (lenth - 1):
#        print(aba)
#