import requests
from pprint import pprint
import argparse
import os
import json
import glob
from operator import itemgetter
import csv
from csv import DictWriter as DictWriter
from textblob import TextBlob

parser = argparse.ArgumentParser()
parser.add_argument('search', help="enter a search term",
                   type=str)
args = parser.parse_args()

search_term = args.search
path = "C:\\Users\\pgavaskar\\python project\\Restaurants\\"+search_term+"\\"
sorted_names = {}
for filename in glob.glob(os.path.join(path, '*.txt')):
	
	with open(filename) as outfile:
		data = json.load(outfile)
		restaurants = data["restaurants"]
		for d in restaurants:
			rating_text = d["restaurant"]["user_rating"]["rating_text"]
			restaurant_name = d["restaurant"]["name"]
			analysis = TextBlob(rating_text)
			#print (analysis.sentiment)
			if analysis.sentiment.polarity < 0:
				sentiment = "negative"
			elif analysis.sentiment.polarity == 0:
				sentiment = "neutral"
			else:
				sentiment = "positive"
			#print (sentiment)
			sorted_names.update({restaurant_name : sentiment})	
			
save_file = open("C:\\Users\\pgavaskar\\python project\\Restaurants\\"+search_term+"\\review_results.csv", 'w', newline='', encoding='utf-8')	
try:
	fieldnames = ['restaurant', 'review']
	writer = DictWriter(save_file,fieldnames=fieldnames)
	writer.writeheader()
	a = {}
	for key in sorted_names:
		a["restaurant"] = key
		a["review"] = sorted_names[key]
		writer.writerow(a)
finally:
    save_file.close()