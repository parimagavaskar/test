import requests
from pprint import pprint
import argparse
import os
import json
import glob
from operator import itemgetter
import csv

parser = argparse.ArgumentParser()
parser.add_argument('search', help="enter a search term",
                   type=str)
parser.add_argument('cuisine' , help="enter a cuisine", type=str)
args = parser.parse_args()

cuisine_term = args.cuisine
search_term = args.search

sorted_names = {}
filename = "C:\\Users\\pgavaskar\\python project\\Cuisines\\cuisines_"+search_term+".txt"
with open(filename) as outfile:
	cuisine_data = json.load(outfile)
	
#for l in cuisine_data:
#	cuisine_list = l['cuisines']
#	for d in cuisine_list:
#		cuisine_name = d['cuisine']['cuisine_name']
#		if cuisine_name == cuisine_term:
#			cuisine_id = d['cuisine']['cuisine_id']
			
path = "C:\\Users\\pgavaskar\\python project\\Restaurants\\"+search_term+"\\"

for filename in glob.glob(os.path.join(path, '*.txt')):
	
	with open(filename) as outfile:
		data = json.load(outfile)
		restaurants = data["restaurants"]
		for d in restaurants:
			cuisine = d["restaurant"]["cuisines"]
			
			if cuisine_term in cuisine:
				
				restaurant_name = d["restaurant"]["name"]
				
				cost = d["restaurant"]["average_cost_for_two"]
				
				
				sorted_names.update({restaurant_name : float(cost)})
				
sortData = sorted(sorted_names.items(), key=itemgetter(1), reverse=True)
with open("C:\\Users\\pgavaskar\\python project\\Restaurants\\"+search_term+"\\costs_cusines.csv",'w') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(["restaurant_name","cost"])
    for row in sortData:
        csv_out.writerow(row)	





