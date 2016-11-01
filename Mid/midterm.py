import requests
#from requests_oauthlib import OAuth2Session
from pprint import pprint
import argparse
import os
import json


parser = argparse.ArgumentParser()
parser.add_argument('search', help="enter a search term",
                   type=str)

args = parser.parse_args()
search_term = args.search




client_id = "8195"
client_secret = "z2n4vYJT4aQAwIT5bVOMfw(("
redirect_uri = "https://stackexchange.com/oauth/login_success"
api_key = "xGX9TXy)kd73rkw8j8mKhA(("
scope = 'no_expiry'

#resp = requests.get('https://stackexchange.com/oauth/dialog?client_id=8195&scope=no_expiry&redirect_uri=https://stackexchange.com/oauth/login_success/')


#r = requests.get("https://api.stackexchange.com/2.2/questions?key="+api_key+"&order=desc&sort=activity&tagged="+search_term+"&site=stackoverflow" )
#filename = "C:\\Midterm\\"+search_term+".txt"
#if not os.path.exists(os.path.dirname(filename)):
#    try:
#        os.makedirs(os.path.dirname(filename))
#    except OSError as exc: # Guard against race condition
#        if exc.errno != errno.EEXIST:
#            raise
#with open(filename, 'w', encoding = 'utf-8') as outfile:
#	json.dump(r.json(), outfile)
#myData = None	
filename = "C:\\Midterm\\python.txt"
with open(filename) as outfile:	
	myData = json.load(outfile)
	
x = myData['items']
userList = []
for j in x:
	ownerList = j['owner']
	userList.append(ownerList['user_id'])


fileProfiles = "C:\\Midterm\\pythonUserProfiles"
	
for userId in userList:
	userProfile = requests.get("https://api.stackexchange.com/2.2/users/"+str(userId)+"?order=desc&sort=reputation&site=stackoverflow&key="+api_key)
	profileData = userProfile.json()
	with open(fileProfiles+str(userId)+".txt", 'w', encoding = 'utf-8') as outfile:
		json.dump(userProfile.json(), outfile)
		



