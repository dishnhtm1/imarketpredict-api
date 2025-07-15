import pandas as pd
from textblob import TextBlob
import os

# Make output directory if not exists
os.makedirs("output_for_module2", exist_ok=True)

### ✅ STOCK PRICES FILE
source_stock = "data_samples/N225_price_2025-07-09_5years.csv"
target_stock = "output_for_module2/stock_prices.csv"
pd.read_csv(source_stock).to_csv(target_stock, index=False)
print(f"✅ stock_prices.csv created: {target_stock}")

### ✅ SENTIMENT SCORES FILE
source_twitter = "data_samples/twitter_sentiment_2025-07-08.csv"
df = pd.read_csv(source_twitter)

# Simple polarity score from tweet text
def get_sentiment(text):
    try:
        return TextBlob(text).sentiment.polarity
    except:
        return 0

df["sentiment"] = df["Tweet"].apply(get_sentiment)



# Save sentiment_scores.csv
target_sentiment = "output_for_module2/sentiment_scores.csv"
df.to_csv(target_sentiment, index=False)
print(f"✅ sentiment_scores.csv created: {target_sentiment}")
