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
hashtag = {"astro-ph" : "#AstroPhysics", 
           "cond-mat" : "#CondensedMatter" , 
           "gr-qc" : "#GeneralRelativity #QuantumCosmology", 
           "hep-ex" : "#HighEnergyPhysics #Expirement",
           "hep-lat" : "#HighEnergyPhysics #Lattice", 
           "hep-ph" : "#HighEnergyPhysics #Phenomenology", 
           "hep-th" : "#HighEnergyPhysics #Theory", 
           "math-ph" : "#MathematicalPhysics",
           "nlin" : "#NonLinear", 
           "nucl-ex" : "#NuclearExperiment", 
           "nucl-th" : "#NuclearTheory", 
           "physics" : "#Physics",
           "quant-ph" : "#QuantumPhysics", 
           "math" : "#Math",
           "cs" : "#ComputerScience #cs", 
           "q-bio" : "#QuantitativeBio #bio #biology",
           "q-fin" : "#QuantitativeFinance #quant #finance", 
           "stat" : "#stats #statistics", 
           "eess" : "#ElectricalEngineering #engineering", 
           "econ" : "#econ #economics"
           }
# Send tweets on a given array 
def send_tweets(subjects, hashtag):
    """Tweets out the latest article in each category on Arxiv.org"""
    for s in subjects:
        try:
            print(make_tweet(s, hashtag[s]))
            api.update_status(make_tweet(s, hashtag[s]))
        except:
            print("FAILED: {}".format(s))

send_tweets(subjects, hashtag)

# Run daily indefinitely 
#while(True):
#   send_tweets(subjects)
#    print("SUCESS: " + str(datetime.datetime.now()))
#    print("NEXT PASS: " + str((datetime.datetime.now() + datetime.timedelta(days=1))))
#    time.sleep(86400)
