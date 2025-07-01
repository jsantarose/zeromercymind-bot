import tweepy

print("🤖 Starting bot...")

# 🔐 Twitter API credentials
API_KEY = "WoUER4rHr5lekW6TEqNBk13mG"
API_KEY_SECRET = "ozjpNix39cmhLkwSj0YvdhxMGGLlMEmXUGRPvpfIz1Ag4YBAnE"
ACCESS_TOKEN = "1940036600274239488-XfcdmDXijPWBiYPBmY7DrnWnBoHCCg"
ACCESS_TOKEN_SECRET = "C8OCxlco4uE00Jgapv6VqLOUkbXnA5YeVsaBULO1PhHJK"

# 🔑 Authenticate using OAuth 1.0a
auth = tweepy.OAuth1UserHandler(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# 🐦 The tweet content
tweet = "You weren’t made to blend in. You were made to lead warriors."
print(f"📢 Tweet selected: {tweet}")

# 🚀 Post the tweet
try:
    api.update_status(tweet)
    print("✅ Tweet posted successfully!")
except Exception as e:
    print("❌ Error occurred while tweeting:", e)
