# import yfinance as yf
# import pandas as pd
# from datetime import datetime, timedelta
# import os

# # Set ticker and 5-year range
# ticker = "^N225"  # Nikkei 225 index
# start_date = (datetime.today() - timedelta(days=5*365)).strftime('%Y-%m-%d')
# end_date = datetime.today().strftime('%Y-%m-%d')

# # Create output folder
# output_dir = "data_samples"
# os.makedirs(output_dir, exist_ok=True)

# # Fetch historical stock data
# print(f"📥 Fetching {ticker} data from {start_date} to {end_date}...")
# df = yf.download(ticker, start=start_date, end=end_date, interval="1d")

# # Save to CSV
# output_file = os.path.join(output_dir, f"N225_price_{end_date}_5years.csv")
# df.to_csv(output_file)
# print(f"✅ Saved 5-year stock data to: {output_file}")
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import os

# Set ticker and date range
ticker = "^N225"  # Nikkei 225 index
start_date = (datetime.today() - timedelta(days=5*365)).strftime('%Y-%m-%d')
end_date = datetime.today().strftime('%Y-%m-%d')

# Output folder
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Fetch historical data
print(f"📥 Fetching {ticker} data from {start_date} to {end_date}...")
df = yf.download(ticker, start=start_date, end=end_date, interval="1d")

# Reset index to get 'Date' as column
df.reset_index(inplace=True)

# Rename and reorder columns
df_cleaned = df[["Date", "Open", "High", "Low", "Close", "Volume"]].copy()
df_cleaned.columns = ["date", "open", "high", "low", "close", "volume"]

# Add ticker column at the front
df_cleaned.insert(0, "ticker", "N225")

# Save to CSV
output_file = os.path.join(output_dir, "stock_prices.csv")
df_cleaned.to_csv(output_file, index=False)
print(f"✅ Saved cleaned stock price data to: {output_file}")
