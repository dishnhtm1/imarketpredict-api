def fetch_intraday_stock_data():
    ticker = "7203.T"  # Toyota
    interval = "1m"
    today = datetime.today()
    start = today - timedelta(days=1)

    df = yf.download(
        tickers=ticker,
        start=start.strftime('%Y-%m-%d'),
        interval=interval,
        progress=False
    )

    if df.empty:
        print("❌ No intraday data available.")
        return

    df.reset_index(inplace=True)
    df["date"] = df["Datetime"].dt.strftime('%Y-%m-%d %H:%M')
    df_cleaned = df[["date", "Open", "High", "Low", "Close", "Volume"]].copy()
    df_cleaned.columns = ["date", "open", "high", "low", "close", "volume"]
    df_cleaned.insert(0, "ticker", ticker)

    os.makedirs("/home/meshaka/airflow/output", exist_ok=True)
    file_path = "/home/meshaka/airflow/output/7203_T_intraday.csv"

    if os.path.exists(file_path):
        df_cleaned.to_csv(file_path, mode='a', header=False, index=False)
    else:
        df_cleaned.to_csv(file_path, index=False)

    print(f"✅ Intraday data saved for {ticker}")
