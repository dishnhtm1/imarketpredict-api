import tweepy
import pandas as pd
from textblob import TextBlob
from datetime import datetime

# Replace with your actual bearer token
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAADjb2wEAAAAAXPWbgczqXZ0t2YgoBq3EZsMCmtg%3DneIlcSQ1PYMVaSUjHw1ySATyWdkYi8F0QshbWy4cFeT9GsI5Y5"


client = tweepy.Client(bearer_token=BEARER_TOKEN)

query = "Nikkei OR Tokyo Stock Exchange OR Japan market lang:en -is:retweet"
tweets = client.search_recent_tweets(query=query, max_results=50, tweet_fields=["created_at", "text"])

data = []
ticker = "^N225"

for tweet in tweets.data:
    text = tweet.text
    sentiment = TextBlob(text).sentiment.polarity
    date = tweet.created_at.strftime('%Y-%m-%d')
    data.append({"ticker": ticker, "date": date, "tweet": text, "sentiment_score": sentiment})

df = pd.DataFrame(data)
df.to_csv("output_for_module2/real_english_sentiment_scores.csv", index=False)
print("✅ Saved real tweets with sentiment scores to: output_for_module2/real_english_sentiment_scores.csv")
