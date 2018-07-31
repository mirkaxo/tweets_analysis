#'''
#Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
#'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("tweets.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!
# json object or tweet are store in tweetData

#iterate list of tweets
for tweet in tweetData:
    #access the text of the tweet
    text=tweet["text"]

    #print polarity
    blob=TextBlob(text)
    print(blob.polarity)
