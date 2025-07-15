from fastapi import FastAPI, Query
import pandas as pd
import os
from glob import glob

app = FastAPI()

DATA_DIR = "/mnt/c/imarketpredict/imarketpredict-module1/data/intraday"  # <- folder with all CSVs

def get_latest_file():
    csv_files = glob(os.path.join(DATA_DIR, "*.csv"))
    if not csv_files:
        return None
    # Sort by modification time, newest last
    latest_file = max(csv_files, key=os.path.getmtime)
    return latest_file

def load_latest_data():
    latest_file = get_latest_file()
    if latest_file is None:
        return pd.DataFrame()
    df = pd.read_csv(latest_file)
    # Clean/replace NaN and Infinity values
    df = df.replace([float('inf'), float('-inf')], pd.NA)
    df = df.fillna("")  # or fillna(0) or another value you prefer
    return df
@app.get("/")
def read_root():
    return {"message": "iMarketPredict Module 1 API is running!"}

@app.get("/stocks/latest")
def get_latest_data():
    df = load_latest_data()
    if df.empty:
        return []
    return df.tail(100).to_dict(orient="records")

@app.get("/stocks/all")
def get_all_data():
    df = load_latest_data()
    if df.empty:
        return []
    return df.to_dict(orient="records")

@app.get("/stocks/filter")
def filter_data(
    ticker: str = Query(None),
    date: str = Query(None)
):
    df = load_latest_data()
    if df.empty:
        return []
    if ticker and "Ticker" in df.columns:
        df = df[df["Ticker"] == ticker]
    if date and "Date" in df.columns:
        df = df[df["Date"] == date]
    return df.to_dict(orient="records")