import tweepy

print("🤖 Starting bot...")

# 🔑 Twitter API credentials (copied from your screenshots)
API_KEY = "H64FEIVx7d05cdCUGLCIcwvmvA"
API_KEY_SECRET = "P8VvqDXAbOsVNOPLq2hMU6trtNZDWDgBV8EnYjAphHVXpRkW"
ACCESS_TOKEN = "1940036600274239488-7HOw6FRjAv4WyAwTSuUg05nhZPbSq7"
ACCESS_TOKEN_SECRET = "uc7vHW9zPvQvbi6RVewoLP6pQeqdJK5NTz6JhjVRIDvL0"

# 🛡️ Authenticate
auth = tweepy.OAuth1UserHandler(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# 🐦 Define tweet message
tweet = "Suffer voluntarily, or be forced to suffer later."
print(f"📢 Tweet selected: {tweet}")

# 🚀 Send tweet
try:
    api.update_status(tweet)
    print("✅ Tweet posted successfully!")
except Exception as e:
    print("❌ Error occurred while tweeting:", e)
