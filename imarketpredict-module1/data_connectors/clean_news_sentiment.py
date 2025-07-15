import pandas as pd
import os

# Load your CSV
input_path = "output_for_module2/news_sentiment_data.csv"
output_path = "output_for_module2/cleaned_news_sentiment_data.csv"

df = pd.read_csv(input_path)

# Lowercase text for filtering
df["text_lower"] = df["text"].str.lower()

# Define unwanted "comment-like" keywords
comment_keywords = [
    "i think", "i believe", "my opinion", "lol", "omg",
    "so sad", "so funny", "lmao", "imo", "😂", "😢", "😡", "wtf"
]

# Filter out rows where 'text' contains any comment keywords
df = df[~df["text_lower"].str.contains('|'.join(comment_keywords), na=False)]

# Drop helper column
df.drop(columns=["text_lower"], inplace=True)

# Save cleaned CSV
df.to_csv(output_path, index=False)
print(f"✅ Cleaned data (comments removed) saved to: {output_path}")
