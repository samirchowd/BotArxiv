import tweepy
import time
import datetime
import config
from scrape import *

# Setting up authentication
consumer_key = config.api_key
consumer_secret = config.api_secret_key

access_token = config.access_token
access_token_secret = config.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Instantiating API 
api = tweepy.API(auth)

# Defining subjects for links 
subjects = ["astro-ph", "cond-mat", "gr-qc", "hep-ex",
            "hep-lat", "hep-ph", "hep-th", "math-ph",
            "nlin", "nucl-ex", "nucl-th", "physics",
            "quant-ph", "math", "cs", "q-bio",
            "q-fin", "stat", "eess", "econ"
             ]

# Send tweets on a given array 
def send_tweets(subjects):
    """Tweets out the latest article in each category on Arxiv.org"""
    for s in subjects:
        try:
            print(make_tweet(s))
            api.update_status(make_tweet(s))
        except:
            pass

# Run daily indefinitely 
while(True):
    send_tweets(subjects)
    print("SUCESS: " + str(datetime.datetime.now()))
    print("NEXT PASS: " + str((datetime.datetime.now() + datetime.timedetla(days=1))))
    time.sleep(86400)
