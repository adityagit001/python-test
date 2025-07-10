import os
from dotenv import load_dotenv
import tweepy

# Load environment variables
load_dotenv()

# Get API credentials
bearer_token = os.getenv("BEARER_TOKEN")
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Authenticate with Tweepy v2
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Tweet message
tweet = "Hello Twitter with Tweepy v2! 🚀 #Python #XAPI"
response = client.create_tweet(text=tweet)

print("Tweet posted successfully!", response)
