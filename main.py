import tweepy

print("🤖 Starting bot...")

# 🔐 Twitter API credentials (July 1 - updated)
API_KEY = "281tbn64D9mUzDwULzULNsn0y"
API_KEY_SECRET = "P8VvqDXAbBOsVNOPLq2hMU6trtNZXDWdDV8EnYyAphHVXpRkwV"
ACCESS_TOKEN = "1940036600274239488-4CZYbSVVqx5oJIkx5QaJtvXCj2K6fo"
ACCESS_TOKEN_SECRET = "0XtfjpEr3rfPAdjggoZdynPXN2SlKFrnezIF1TMoO76h1"

# 🔑 Authenticate with Tweepy
auth = tweepy.OAuth1UserHandler(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# 🐦 Tweet content
tweet = "Suffer voluntarily, or be forced to suffer later."
print(f"📢 Tweet selected: {tweet}")

# 🚀 Post tweet
try:
    api.update_status(tweet)
    print("✅ Tweet posted successfully!")
except Exception as e:
    print("❌ Error occurred while tweeting:", e)
