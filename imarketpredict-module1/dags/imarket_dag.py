from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import yfinance as yf
import pandas as pd

def fetch_stock_data():
    ticker = "^N225"
    data = yf.download(ticker, start="2020-01-01", end=datetime.today().strftime("%Y-%m-%d"))
    data.to_csv(f"/home/meshaka/airflow/outputs/N225_stock_{datetime.today().strftime('%Y-%m-%d')}.csv")

default_args = {
    'owner': 'meshaka',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='fetch_stock_prices',
    default_args=default_args,
    description='Fetch daily Nikkei 225 stock prices',
    schedule_interval='@daily',  # or '@once' to test immediately
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:

    fetch_task = PythonOperator(
        task_id='fetch_n225_stock_data',
        python_callable=fetch_stock_data
    )
