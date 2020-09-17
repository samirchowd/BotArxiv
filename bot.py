import tweepy
import config
# from scrape import *

consumer_key = config.api_key
consumer_secret = config.api_secret_key

access_token = config.access_token
access_token_secret = config.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
api.update_status('Arxiv Bot reporting in live!')