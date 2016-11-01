import requests
#from requests_oauthlib import OAuth2Session
from pprint import pprint
import argparse
import os
import json
from collections import Counter

client_id = "8195"
client_secret = "z2n4vYJT4aQAwIT5bVOMfw(("
redirect_uri = "https://stackexchange.com/oauth/login_success"
api_key = "xGX9TXy)kd73rkw8j8mKhA(("
scope = 'no_expiry'

resp = requests.get("https://api.stackexchange.com/2.2/badges/recipients?fromdate=786240000&todate=1477872000&site=stackoverflow&key="+api_key)
filename = "C:\\Midterm\\Badges.txt"
if not os.path.exists(os.path.dirname(filename)):
    try:
        os.makedirs(os.path.dirname(filename))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise
with open(filename, 'w', encoding = 'utf-8') as outfile:
	json.dump(resp.json(), outfile)
	
	
namesList=[]	
with open('C:/midterm/Badges.txt', 'r') as outfile:
	userData = json.load(outfile)
	data = userData["items"]
	for d in data:
		namesList.append(d["name"])
	counts = Counter(namesList)
	print(counts)
	