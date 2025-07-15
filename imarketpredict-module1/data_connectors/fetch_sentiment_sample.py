import pandas as pd
from textblob import TextBlob
from datetime import datetime
import os

# Sample Japanese market-related tweets (simulated)
tweets = [
    "株式市場が回復しています！投資家にとって良いニュースです。",
    "日経平均が下落中。不安が広がっています。",
    "トヨタの決算が予想以上だった。株価に好影響か？",
    "日本の経済指標が悪化。注意が必要。"
]

# Convert to sentiment scores using TextBlob (note: works best for English, replace later for Japanese NLP)
def get_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity  # Range: -1 to 1

# Prepare DataFrame
data = [{"tweet": tweet, "sentiment": get_sentiment(tweet)} for tweet in tweets]
df = pd.DataFrame(data)

# Create output folder
output_dir = "data_samples"
os.makedirs(output_dir, exist_ok=True)

# Save to CSV
today = datetime.today().strftime('%Y-%m-%d')
output_file = os.path.join(output_dir, f"N225_sentiment_{today}_sample.csv")
df.to_csv(output_file, index=False)

print(f"✅ Sentiment CSV saved: {output_file}")
