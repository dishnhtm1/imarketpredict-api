import pandas as pd

# Load your CSV file
df = pd.read_csv("output_for_module2/news_sentiment_data.csv")

# Drop the 'text' column
df.drop(columns=["text"], inplace=True)

# Save the cleaned CSV
df.to_csv("output_for_module2/cleaned_sentiment_only.csv", index=False)

print("✅ Cleaned CSV saved as 'cleaned_sentiment_only.csv'")
