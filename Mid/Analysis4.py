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
		
bestReputation = 0		
winner = None		
for f in files:
	with open('C:/midterm/'+f, 'r') as outfile:
		userData = json.load(outfile)
		data = userData["items"]
		rep = userData["items"][0]["reputation"]
		if rep > bestReputation:
			bestReputation = rep
			winner = f[18:][:-4]
			
print("User with the tag of python and highest reputation is "+ winner)