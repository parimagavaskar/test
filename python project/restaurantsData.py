import requests
from pprint import pprint
import argparse
import os
import json
import collections


		
		
parser = argparse.ArgumentParser()
parser.add_argument('search', help="enter a search term",
                   type=str)
args = parser.parse_args()

search_term = args.search




entityID = 0
filename = "C:\\Users\\pgavaskar\\python project\\Cities\\cities.txt"
with open(filename) as outfile:
	cityData = json.load(outfile)
for d in cityData:
	cityName = d["location_suggestions"][0]["city_name"]
	if cityName == search_term:
		entityID = d["location_suggestions"][0]["city_id"]


headers = {"User-agent": "curl/7.43.0","Content-Type":"application/json","user-key": "4f92a6faba984f348c8bbc58ef2bb676"}
restaurantsUrl1 = "https://developers.zomato.com/api/v2.1/search?entity_id="+str(entityID)+"&entity_type=city&sort=cost&order=desc"


#data = []
req1 = requests.get(restaurantsUrl1, headers = headers).json()
#unwanted = ('results_found', 'results_start', 'results_shown')
#d["results"] = []

i = 0
restfilename = "C:\\Users\\pgavaskar\\python project\\Restaurants\\"+search_term+"\\"+search_term+str(i)+".txt"
if not os.path.exists(os.path.dirname(restfilename)):
    try:
	
        os.makedirs(os.path.dirname(restfilename))
		
    except OSError as exc: # Guard against race condition
	
        if exc.errno != errno.EEXIST:
		
            raise
with open(restfilename, 'w', encoding = 'utf-8') as outfile:
	json.dump(req1, outfile)
i = 1
start = 1
	
	
while i <= 4:
	start = i * 20
	restaurantUrl="https://developers.zomato.com/api/v2.1/search?entity_id="+str(entityID)+"&entity_type=city&start="+str(start)+"&sort=cost&order=desc"
	restfilename1 = "C:\\Users\\pgavaskar\\python project\\Restaurants\\"+search_term+"\\"+search_term+str(i)+".txt"
	r = requests.get(restaurantUrl, headers = headers).json()
	if not os.path.exists(os.path.dirname(restfilename1)):
		try:
			os.makedirs(os.path.dirname(restfilename1))
		except OSError as exc: # Guard against race condition
			if exc.errno != errno.EEXIST:
				raise
	with open(restfilename1, 'w', encoding = 'utf-8') as outfiles:
		json.dump(r, outfiles)	
		
	
			
		
		
		i = i + 1

		

