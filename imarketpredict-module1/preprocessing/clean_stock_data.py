import pandas as pd
import os

def clean_stock_data(input_path):
    print(f"🔧 Cleaning stock data: {input_path}")

    # Skip the second line with ^N225 headers
    df = pd.read_csv(input_path, skiprows=[1])

    # Ensure correct data types
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
    
    df.dropna(inplace=True)

    # Add percentage change
    if 'Close' in df.columns:
        df['Pct_Change'] = df['Close'].pct_change() * 100
        df.dropna(inplace=True)

        q_low = df['Close'].quantile(0.05)
        q_high = df['Close'].quantile(0.95)
        df = df[(df['Close'] > q_low) & (df['Close'] < q_high)]

    cleaned_path = input_path.replace(".csv", "_cleaned.csv")
    df.to_csv(cleaned_path, index=False)
    print(f"✅ Cleaned data saved to: {cleaned_path}")
    return df

if __name__ == "__main__":
    raw_file = "data_samples/N225_price_2025-07-08.csv"  # Update path if needed
    if os.path.exists(raw_file):
        clean_stock_data(raw_file)
    else:
        print("❌ Raw stock data file not found.")
