# # from fastapi import FastAPI, Query
# # import pandas as pd
# # import os
# # from glob import glob

# # app = FastAPI()

# # DATA_DIR = "/mnt/c/imarketpredict-api/iMarketPredict-Data1/imarketpredict-module1/data/intraday"  # <- folder with all CSVs

# # def get_latest_file():
# #     csv_files = glob(os.path.join(DATA_DIR, "*.csv"))
# #     if not csv_files:
# #         return None
# #     # Sort by modification time, newest last
# #     latest_file = max(csv_files, key=os.path.getmtime)
# #     return latest_file

# # def load_latest_data():
# #     latest_file = get_latest_file()
# #     if latest_file is None:
# #         return pd.DataFrame()
# #     df = pd.read_csv(latest_file)
# #     # Clean/replace NaN and Infinity values
# #     df = df.replace([float('inf'), float('-inf')], pd.NA)
# #     df = df.fillna("")  # or fillna(0) or another value you prefer
# #     return df
# # @app.get("/")
# # def read_root():
# #     return {"message": "iMarketPredict Module 1 API is running!"}

# # @app.get("/stocks/latest")
# # def get_latest_data():
# #     df = load_latest_data()
# #     if df.empty:
# #         return []
# #     return df.tail(100).to_dict(orient="records")

# # @app.get("/stocks/all")
# # def get_all_data():
# #     df = load_latest_data()
# #     if df.empty:
# #         return []
# #     return df.to_dict(orient="records")

# # @app.get("/stocks/filter")
# # def filter_data(
# #     ticker: str = Query(None),
# #     date: str = Query(None)
# # ):
# #     df = load_latest_data()
# #     if df.empty:
# #         return []
# #     if ticker and "Ticker" in df.columns:
# #         df = df[df["Ticker"] == ticker]
# #     if date and "Date" in df.columns:
# #         df = df[df["Date"] == date]
# #     return df.to_dict(orient="records")
# from fastapi import FastAPI, Query
# import yfinance as yf
# import pandas as pd

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "iMarketPredict Module 1 API is running!"}

# @app.get("/stocks/latest")
# def get_latest_data(
#     symbol: str = Query(default="7203.T", description="Ticker symbol, e.g., 7203.T for Toyota")
# ):
#     ticker = yf.Ticker(symbol)
#     hist = ticker.history(period="1d")
#     if hist.empty:
#         return {"error": f"No data found for {symbol}"}
#     latest_row = hist.tail(1).reset_index()
#     latest_row['Date'] = latest_row['Date'].astype(str)
#     return latest_row.to_dict(orient="records")[0]

# @app.get("/stocks/history")
# def get_stock_history(
#     symbol: str = Query(default="7203.T"),
#     period: str = Query(default="5d"),    # e.g., 1d, 5d, 1mo, 3mo, 1y
#     interval: str = Query(default="1d")   # e.g., 1m, 5m, 15m, 1h, 1d
# ):
#     ticker = yf.Ticker(symbol)
#     hist = ticker.history(period=period, interval=interval)
#     if hist.empty:
#         return {"error": f"No data found for {symbol}"}
#     hist = hist.reset_index()
#     hist['Date'] = hist['Date'].astype(str)
#     return hist.to_dict(orient="records")
from fastapi import FastAPI, Query
import yfinance as yf
import pandas as pd
import logging

app = FastAPI()

# Optional: Add basic logging
logging.basicConfig(level=logging.INFO)

@app.get("/")
def read_root():
    return {"message": "iMarketPredict Module 1 API is running!"}

@app.get("/stocks/latest")
def get_latest_data(
    symbol: str = Query(default="7203.T", description="Ticker symbol, e.g., 7203.T for Toyota")
):
    try:
        logging.info(f"Fetching latest data for symbol: {symbol}")
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period="1d")
        if hist.empty:
            logging.warning(f"No data found for symbol: {symbol}")
            return {"error": f"No data found for {symbol}"}
        latest_row = hist.tail(1).reset_index()
        latest_row['Date'] = latest_row['Date'].astype(str)
        return latest_row.to_dict(orient="records")[0]
    except Exception as e:
        logging.error(f"Error fetching data for {symbol}: {e}")
        return {"error": str(e)}

@app.get("/stocks/history")
def get_stock_history(
    symbol: str = Query(default="7203.T"),
    period: str = Query(default="5d"),    # e.g., 1d, 5d, 1mo, 3mo, 1y
    interval: str = Query(default="1d")   # e.g., 1m, 5m, 15m, 1h, 1d
):
    try:
        logging.info(f"Fetching history for symbol: {symbol}, period: {period}, interval: {interval}")
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period=period, interval=interval)
        if hist.empty:
            logging.warning(f"No data found for symbol: {symbol}")
            return {"error": f"No data found for {symbol}"}
        hist = hist.reset_index()
        hist['Date'] = hist['Date'].astype(str)
        return hist.to_dict(orient="records")
    except Exception as e:
        logging.error(f"Error fetching history for {symbol}: {e}")
        return {"error": str(e)}
