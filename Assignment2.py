import argparse
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from textblob import TextBlob
import requests
import os
import json
from requests_oauthlib import OAuth1
from nltk.corpus import stopwords
import string
import operator 
from collections import Counter
from nltk.tokenize import word_tokenize
import re
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize




parser = argparse.ArgumentParser()
parser.add_argument('search', help="enter a search term",
                    type=str)

args = parser.parse_args()
search_term = args.search

consumer_key = 'Vu3eDTvVdkxqs91GvZrmJnUOz'
consumer_secret = 'C5Eyy53iLy7TpvXip6yO8Qi6ukpYZSFvOA1kvkE6Slplm5LQwt'
access_token = '787788110029545472-mbG4P5jda3TgdQP4uTnyVQfLVSYwfwy'
access_token_secret = 'FcV7cXyI2f1eqCNOptUrxjMNeS83RGV9Hzt6VspVyvge5'
oauth = OAuth1(consumer_key,  
         consumer_secret,  
         access_token,  
         access_token_secret)
r = requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q="+search_term, auth=oauth) 
#print (r.json())
myData = r.json()
myStatuses = myData['statuses']
stop = set(stopwords.words('english'))
for items in myStatuses:
    myTexts = items['text']
    myTweets = items['retweeted']

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
	
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]



tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

def tokenize(s):
    return tokens_re.findall(s)
	
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens




	    




filename = "C:\\Users\\Pari\\"+search_term+".txt"
if not os.path.exists(os.path.dirname(filename)):
    try:
        os.makedirs(os.path.dirname(filename))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise
with open(filename, 'w') as outfile:
    json.dump(r.json(), outfile)
	
with open(filename, 'r') as f:
    
    count_all = Counter()
    for line in f:
        
        tweet = json.loads(line)
		
        terms_all = [term for term in preprocess(myTexts)]
        count_all.update(terms_all)
        commonWordsInText = count_all.most_common(5)
filenameData = "C:\\Users\\Pari\\"+search_term+"Analysis1"+".txt"
if not os.path.exists(os.path.dirname(filenameData)):
    try:
        os.makedirs(os.path.dirname(filenameData))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise
with open(filenameData, 'w', encoding='utf-8') as outfile: 
    for i in commonWordsInText:
        #filtered_words = [word for word in i if word not in stopwords.words('english')]
        stops = set(stopwords.words("english"))
        if i not in stops:
            json.dump(i, outfile)
        #outfile.write(i)
		
filenameDataRetweet = "C:\\Users\\Pari\\"+search_term+"Analysis2"+".txt"
if not os.path.exists(os.path.dirname(filenameDataRetweet)):
    try:
        os.makedirs(os.path.dirname(filenameDataRetweet))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise
with open(filenameDataRetweet, 'w',encoding='utf-8') as outfile:
    count=0
    text = None
    for j in myStatuses:
        myTweets = j['retweet_count']
        if myTweets > count:
            count = myTweets
            text = j['text']
            
    
    outfile.write(text)
    
filenameTime = "C:\\Users\\Pari\\"+search_term+"Analysis3"+".txt"
if not os.path.exists(os.path.dirname(filenameTime)):
    try:
        os.makedirs(os.path.dirname(filenameTime))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise
with open(filenameTime, 'w', encoding='utf-8') as outfile:
    
    
    for j in myStatuses:
        tz = j['user']['time_zone']
        if tz == "Pacific Time (US & Canada)":
            text = j['text']
            #json.dump(text, outfile)
            outfile.write(text)
            
            
with open(filename, 'r') as outfile:
    for tweet in outfile:
        analysis = TextBlob(tweet)
        senti = analysis.sentiment
filenameSenti = "C:\\Users\\Pari\\"+search_term+"Analysis4"+".txt"
if not os.path.exists(os.path.dirname(filenameSenti)):
    try:
        os.makedirs(os.path.dirname(filenameSenti))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise
with open(filenameSenti, 'w') as outfile:
    json.dump(senti, outfile)
    
    

    
filenameTime = "C:\\Users\\Pari\\"+search_term+"Analysis5"+".txt"
if not os.path.exists(os.path.dirname(filenameTime)):
    try:
        os.makedirs(os.path.dirname(filenameTime))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise
with open(filenameTime, 'w', encoding='utf-8') as outfile: 
    count=0
    text = None  
    for j in myStatuses:
        fav = j['user']['favourites_count']
        if fav > count:
            count = fav
            text = j['text']
    outfile.write(text)  


text = open(filename,'r', encoding='utf-8').read()
stop = set(stopwords.words('english'))

if text not in stop:
    wordcloud = WordCloud().generate(text)

    plt.imshow(wordcloud)
    plt.axis("off")

# lower max_font_size
    wordcloud = WordCloud(max_font_size=40).generate(text)
    plt.figure()
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
	






   

    
    
    

        
      
            
            
            



        
               
	

    
	

	
	


	
