import requests
from pprint import pprint
import argparse
import os
import json
import glob
from operator import itemgetter
import csv
from csv import DictWriter as DictWriter

parser = argparse.ArgumentParser()
parser.add_argument('search', help="enter a search term",
                   type=str)
args = parser.parse_args()

search_term = args.search
entityID = 0
filename1 = "C:\\Users\\pgavaskar\\python project\\Cities\\cities.txt"
with open(filename1) as outfile:
	cityData = json.load(outfile)
for d in cityData:
	cityName = d["location_suggestions"][0]["city_name"]
	if cityName == search_term:
		entityID = d["location_suggestions"][0]["city_id"]


sorted_names = {}
filename = "C:\\Users\\pgavaskar\\python project\\Categories\\"+search_term+"\\"+search_term+"categories.txt"
catUrl = "https://developers.zomato.com/api/v2.1/collections?city_id="+str(entityID)
headers = {"User-agent": "curl/7.43.0","Content-Type":"application/json","user-key": "4f92a6faba984f348c8bbc58ef2bb676"}
req1 = requests.get(catUrl, headers = headers).json()

if not os.path.exists(os.path.dirname(filename)):
    try:
	
        os.makedirs(os.path.dirname(filename))
		
    except OSError as exc: # Guard against race condition
	
        if exc.errno != errno.EEXIST:
		
            raise
with open(filename, 'w', encoding = 'utf-8') as outfile:
	json.dump(req1, outfile)
	
	
	
	data = req1	
	col = data["collections"]
	for c in col:
		c_id = c["collection"]["collection_id"]
		count = c["collection"]["res_count"]
		title = c["collection"]["title"]
		sorted_names.update({title : float(count)})	
		
save_file = open("C:\\Users\\pgavaskar\\python project\\Restaurants\\"+search_term+"\\count_categories.csv", 'w', newline='', encoding='utf-8')	
try:
	fieldnames = ['category', 'count']
	writer = DictWriter(save_file,fieldnames=fieldnames)
	writer.writeheader()
	a = {}
	for key in sorted_names:
		a["category"] = key
		a["count"] = sorted_names[key]
		writer.writerow(a)
finally:
    save_file.close()
	 
