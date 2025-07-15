import yfinance as yf
import pandas as pd
from datetime import datetime
import os

def get_stock_data(ticker="^N225", period="1mo", interval="1d"):
    print(f"🔄 Fetching stock data for {ticker}...")
    
    # Download from Yahoo Finance
    df = yf.download(ticker, period=period, interval=interval)
    df.reset_index(inplace=True)

    # Ensure output folder exists
    os.makedirs("data_samples", exist_ok=True)

    # Save to CSV
    filename = f"data_samples/{ticker.replace('^', '')}_price_{datetime.today().strftime('%Y-%m-%d')}.csv"
    df.to_csv(filename, index=False)

    print(f"✅ Saved stock data to: {filename}")
    return df

# Only run when this file is executed directly
if __name__ == "__main__":
    get_stock_data()
