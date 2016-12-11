import requests
from pprint import pprint
import argparse
import os
import json

#parser = argparse.ArgumentParser()
#parser.add_argument('search', help="enter a search term",
#                   type=str)

#args = parser.parse_args()
#search_term = args.search

headers = {"User-agent": "curl/7.43.0","Content-Type":"application/json","user-key": "4f92a6faba984f348c8bbc58ef2bb676"}
cityUrl1 = "https://developers.zomato.com/api/v2.1/locations?query=mumbai"
cityUrl2 = "https://developers.zomato.com/api/v2.1/locations?query=boston"
cityUrl3 = "https://developers.zomato.com/api/v2.1/locations?query=delhi"
cityUrl4 = "https://developers.zomato.com/api/v2.1/locations?query=philadelphia"
cityUrl5 = "https://developers.zomato.com/api/v2.1/locations?query=chicago"

r1 = requests.get(cityUrl1, headers=headers).json()
r2 = requests.get(cityUrl2, headers=headers).json()
r3 = requests.get(cityUrl3, headers=headers).json()
r4 = requests.get(cityUrl4, headers=headers).json()
r5 = requests.get(cityUrl5, headers=headers).json()
cityData = []
cityData.append(r1)
cityData.append(r2)
cityData.append(r3)
cityData.append(r4)
cityData.append(r5)

filename = "C:\\Users\\pgavaskar\\python project\\Cities\\cities.txt"
if not os.path.exists(os.path.dirname(filename)):
    try:
        os.makedirs(os.path.dirname(filename))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise
with open(filename, 'w', encoding = 'utf-8') as outfile:
	json.dump(cityData, outfile) #Dumps information about the city entered by user.