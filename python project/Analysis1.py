import requests
from pprint import pprint
import argparse
import os
import json
import glob
from operator import itemgetter
import csv
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from pandas import Series, DataFrame
import pandas as pd
import seaborn as sns


parser = argparse.ArgumentParser()
parser.add_argument('search', help="enter a search term",
                   type=str)
args = parser.parse_args()

search_term = args.search

sorted_names = {'restaurant': 0}
sorted_restaurants = []
max = 0
highest_rated_restaurant = ""
restName = ""
i = 0

ratingsList = []
path = "C:\\Users\\pgavaskar\\python project\\Restaurants\\"+search_term+"\\"



for filename in glob.glob(os.path.join(path, '*.txt')):
	with open(filename) as outfile:
		data = json.load(outfile)
		restaurants = data["restaurants"]
		for d in restaurants:
			
			
			rating = d["restaurant"]["user_rating"]["aggregate_rating"]
			highest_rated_restaurant = d["restaurant"]["name"]
			
			sorted_names.update({highest_rated_restaurant : float(rating)})
sortData = sorted(sorted_names.items(), key=itemgetter(1), reverse=True)


with open("C:\\Users\\pgavaskar\\python project\\Restaurants\\"+search_term+"\\ratings.csv",'a') as out:
    csv_out=csv.writer(out)
    
    #csv_out.writerow(["restaurant_name","rating"])
    for row in sortData:
		
        csv_out.writerow(row)
	

			
#df = pd.read_csv("C:\\Users\\pgavaskar\\python project\\Restaurants\\"+search_term+"\\ratings.csv" , encoding = "ISO-8859-1", header = None)
#df2 = df.ix[2:]
#df2[1].apply(lambda x: float(x))

#sns.set_color_codes("pastel")
#sns.barplot(x=df[0], y=df[1], data=df,
#          label="Analysis 1", color="b")

