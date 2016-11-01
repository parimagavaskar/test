import requests
#from requests_oauthlib import OAuth2Session
from pprint import pprint
import argparse
import os
import json







client_id = "8195"
client_secret = "z2n4vYJT4aQAwIT5bVOMfw(("
redirect_uri = "https://stackexchange.com/oauth/login_success"
api_key = "xGX9TXy)kd73rkw8j8mKhA(("
scope = 'no_expiry'



path = 'C:/midterm/'
files = []
for i in os.listdir(path):
    if os.path.isfile(os.path.join(path,i)) and 'pythonUserProfiles' in i:
        files.append(i)
		
		
count = 0
highestView = 0
winningFile = None
topViewed = None
for f in files:
	
	with open('C:/midterm/'+f, 'r') as outfile:
		userData = json.load(outfile)
		badges = userData["items"][0]["badge_counts"]
		bronze = badges['bronze'] * 1
		silver = badges['silver'] * 2
		gold = badges['gold'] * 3
		score = bronze + silver + gold
		if score > count:
			count = score
			winningFile=f
		
			
print(f[18:][:-4])
winner = f[18:][:-4]
viewList = []

with open("C:\midterm\python.txt", 'r') as outfile:
		viewData = json.load(outfile)
		viewData = viewData["items"]
		highestViewCount=0
		title = None
		for question in viewData:
			if question["view_count"] > highestViewCount:
				highestViewCount = question["view_count"]
				title = question["title"]
		print("Question with highest view count is: " + title)
			
		







			
			
