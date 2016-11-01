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



filename = "C:\\Midterm\\python.txt"
with open(filename) as outfile:	
	myData = json.load(outfile)
	
allItems = myData['items']


questionIdList=[]
for item in allItems:
	questionIdList.append(item["question_id"])
	
fileProfiles = "C:\\Midterm\\pythonAnswers"
for id in questionIdList:
	resp = requests.get("https://api.stackexchange.com/2.2/questions/"+str(id)+"/answers?order=desc&sort=activity&site=stackoverflow&filter=!-*f(6t*ZbDla&key="+api_key)
	answerData = resp.json()
	with open(fileProfiles+str(id)+".txt", 'w', encoding = 'utf-8') as outfile:
		json.dump(resp.json(), outfile)
		
		
path = 'C:/midterm/'
files = []
for i in os.listdir(path):
    if os.path.isfile(os.path.join(path,i)) and 'pythonAnswers' in i:
        files.append(i)
		
highestVotes = 0
winningFile = None		
for f in files:
	with open('C:/midterm/'+f, 'r') as outfile:
		userData = json.load(outfile)
		data = userData["items"]
		for d in data:
			votes = d["up_vote_count"]
			if votes > highestVotes:
				highestVotes = votes
				winningFile = f
			
winner = f[13:][:-4]
print("User who was upvoted the most is"+ winner )