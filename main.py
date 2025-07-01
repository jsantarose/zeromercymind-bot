import tweepy
import random

# Twitter API credentials (newly regenerated)
API_KEY = "H64FEIVx7d05cdCUGLCIcwmvA"
API_SECRET = "P8VvqDXAbOsVN0PLq2hMU6trtNZXDWdBVBEnYApHhVXpRkW"
ACCESS_TOKEN = "1940036600274239488-7HOw8FRj4v4WyAwTSuUg05nhZfPbSq7"
ACCESS_SECRET = "uc7vHW9zPvQvbi6RVevoLP6pQeqdJK5NTz6JjhVRIDvL0"

# Quotes list
quotes = [
    "Suffer voluntarily, or be forced to suffer later.",
    "You weren't made to blend in. You were made to lead warriors.",
    "Discipline is mercy to your future self.",
    "Nobody is coming. Get up anyway.",
    "Train your mind to obey you like a weapon.",
    "Zero mercy. Total focus. Daily execution."
]

def tweet_random_quote():
    print("🤖 Starting bot...")

    try:
        auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
        api = tweepy.API(auth)

        tweet = random.choice(quotes)
        print(f"🗣 Tweet selected: {tweet}")
        api.update_status(tweet)
        print("✅ Tweet sent successfully.")
    except tweepy.TweepyException as e:
        print(f"❌ Error occurred while tweeting: {e}")

if __name__ == "__main__":
    tweet_random_quote()

