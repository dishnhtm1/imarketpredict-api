# fetch_twitter_data.py
import os
import tweepy
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime

# Load your bearer token from .env
load_dotenv()
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")

# Initialize Tweepy Client
client = tweepy.Client(bearer_token=bearer_token)

# Your query – feel free to customize
query = "Nikkei OR 日経 -is:retweet lang:ja"
tweets = client.search_recent_tweets(query=query, max_results=10)

# Extract text
tweet_data = []
for tweet in tweets.data:
    tweet_data.append(tweet.text)

# Save to CSV
timestamp = datetime.now().strftime("%Y-%m-%d")
save_path = f"data_samples/twitter_sentiment_{timestamp}.csv"
df = pd.DataFrame(tweet_data, columns=["Tweet"])
df.to_csv(save_path, index=False, encoding='utf-8-sig')

print(f"✅ Saved Twitter data to: {save_path}")
