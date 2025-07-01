import tweepy
import os
import random

# Load keys from environment
api_key = os.environ["API_KEY"]
api_secret = os.environ["API_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

# Auth
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Load tweet list
with open("tweets.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

# Load used tweets
used_path = "used.txt"
if os.path.exists(used_path):
    with open(used_path, "r", encoding="utf-8") as f:
        used = set(f.read().splitlines())
else:
    used = set()

# Get unused tweet
unused = [line for line in lines if line not in used]
if not unused:
    print("No more unused tweets.")
    exit()

tweet = random.choice(unused)

# Post
try:
    api.update_status(tweet)
    print("Tweeted:", tweet)
    with open(used_path, "a", encoding="utf-8") as f:
        f.write(tweet + "\n")
except Exception as e:
    print("Error:", e)
