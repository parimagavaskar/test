import requests
from pprint import pprint
import argparse
import os
import json

parser = argparse.ArgumentParser()
parser.add_argument('search', help="enter a search term",
                   type=str)
args = parser.parse_args()

search_term = args.search


headers = {"User-agent": "curl/7.43.0","Content-Type":"application/json","user-key": "4f92a6faba984f348c8bbc58ef2bb676"}

cuisineFilename = "C:\\Users\\pgavaskar\\python project\\Cuisines\\cuisines_"+search_term+".txt"


filename = "C:\\Users\\pgavaskar\\python project\\Cities\\cities.txt"
with open(filename) as outfile:
	cityData = json.load(outfile)
for d in cityData:
	cityName = d["location_suggestions"][0]["city_name"]
	if cityName == search_term:
		entityID = d["location_suggestions"][0]["city_id"]
		cuisinesUrl	= "https://developers.zomato.com/api/v2.1/cuisines?city_id="+str(entityID)	
		cuisinesRequest = requests.get(cuisinesUrl, headers = headers).json()
		
		
		if not os.path.exists(os.path.dirname(cuisineFilename)):
			try:
				os.makedirs(os.path.dirname(cuisineFilename))
			except OSError as exc: # Guard against race condition
				if exc.errno != errno.EEXIST:
					raise
		with open(cuisineFilename, 'w', encoding = 'utf-8') as outfile:
			json.dump(cuisinesRequest, outfile) #Dumps information ab





