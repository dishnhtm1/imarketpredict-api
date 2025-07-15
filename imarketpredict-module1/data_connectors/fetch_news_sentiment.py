from gnews import GNews
from textblob import TextBlob
import pandas as pd
import os
from datetime import datetime

# Setup
google_news = GNews(language='en', country='US', max_results=10)
news_items = google_news.get_news('stock market')

# Create output directory
output_dir = "output_for_module2"
os.makedirs(output_dir, exist_ok=True)

# Extract and analyze
results = []
for item in news_items:
    title = item['title']
    published_date = item.get('published date') or datetime.now().strftime("%Y-%m-%d")
    if isinstance(published_date, str):
        date = published_date
    else:
        date = published_date.strftime("%Y-%m-%d")
    sentiment = TextBlob(title).sentiment.polarity
    results.append({
        'ticker': 'N225',
        'date': date,
        'text': title,
        'sentiment_score': sentiment
    })

# Save as CSV
df = pd.DataFrame(results)
output_path = os.path.join(output_dir, "news_sentiment_data.csv")
df.to_csv(output_path, index=False)
print(f"✅ Saved sentiment data to: {output_path}")
