# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from datetime import datetime, timedelta
# import yfinance as yf
# import pandas as pd
# import os

# # === DAG Default Arguments ===
# default_args = {
#     'owner': 'airflow',
#     'start_date': datetime(2025, 7, 1),
#     'retries': 1,
#     'retry_delay': timedelta(minutes=5)
# }

# # === Real-Time Fetch Function ===
# def fetch_intraday_stock_data():
#     ticker = "^N225"  # Nikkei 225
#     now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#     df = yf.download(tickers=ticker, period='1d', interval='1m')  # 1-minute interval

#     # ⚠️ Windows path mounted in WSL
#     output_folder = "/mnt/c/imarketpredict/imarketpredict-module1/data/intraday"
#     os.makedirs(output_folder, exist_ok=True)

#     # Save with timestamp in filename
#     # filename = f"{output_folder}/N225_intraday_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"
#     # df.to_csv(filename)
#     # print(f"✅ Saved real-time data to: {filename}")
# # Save with timestamp in filename
#     filename = f"{output_folder}/N225_intraday_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"
#     df.to_csv(filename, index_label="Datetime")
#     print(f"✅ Saved real-time data to: {filename}")

# # === DAG ===
# with DAG(
#     dag_id='fetch_intraday_stock_data',
#     default_args=default_args,
#     description='Fetch real-time intraday Nikkei 225 stock data every 15 minutes',
#     schedule_interval='*/15 * * * *',  # Every 15 minutes
#     catchup=False
# ) as dag:

#     fetch_task = PythonOperator(
#         task_id='fetch_intraday_data',
#         python_callable=fetch_intraday_stock_data
#     )
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import yfinance as yf
import pandas as pd
import os

# === DAG Default Arguments ===
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 7, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# === Real-Time Fetch Function ===
def fetch_intraday_stock_data():
    print("=== USING UPDATED DAG CODE ===")
    ticker = "^N225"  # Nikkei 225
    df = yf.download(tickers=ticker, period='1d', interval='1m')

    # Only proceed if data is downloaded
    if df.empty:
        print("❌ No data returned from yfinance!")
        return

    # Clean DataFrame: reset index to make Datetime a column
    df = df.copy()
    df.reset_index(inplace=True)
    df.columns.name = None

    # Save file
    output_folder = "/mnt/c/imarketpredict/iMarketPredict-Data/imarketpredict-module1/data/intraday"
    os.makedirs(output_folder, exist_ok=True)
    filename = f"{output_folder}/N225_intraday_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"
    df.to_csv(filename, index=False)
    print(f"✅ Saved real-time data to: {filename}")

# === DAG ===
with DAG(
    dag_id='fetch_intraday_stock_data',
    default_args=default_args,
    description='Fetch real-time intraday Nikkei 225 stock data every 15 minutes',
    schedule_interval='*/15 * * * *',  # Every 15 minutes
    catchup=False
) as dag:

    fetch_task = PythonOperator(
        task_id='fetch_intraday_data',
        python_callable=fetch_intraday_stock_data
    )
