from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

default_args = {
    'owner': 'imarketpredict-team',
    'start_date': datetime(2025, 7, 8),
    'retries': 1,
}

dag = DAG(
    'market_data_pipeline',
    default_args=default_args,
    schedule_interval='@daily',  # run once a day
    catchup=False
)

def run_script(script_path):
    subprocess.run(['python', script_path], check=True)

fetch_stock = PythonOperator(
    task_id='fetch_stock_data',
    python_callable=run_script,
    op_args=['data_connectors/fetch_stock_data.py'],
    dag=dag
)

clean_stock = PythonOperator(
    task_id='clean_stock_data',
    python_callable=run_script,
    op_args=['preprocessing/clean_stock_data.py'],
    dag=dag
)

fetch_news = PythonOperator(
    task_id='fetch_news_data',
    python_callable=run_script,
    op_args=['data_connectors/fetch_news_data.py'],
    dag=dag
)

fetch_twitter = PythonOperator(
    task_id='fetch_twitter_data',
    python_callable=run_script,
    op_args=['data_connectors/fetch_twitter_data.py'],
    dag=dag
)

# Set task dependencies
fetch_stock >> clean_stock >> [fetch_news, fetch_twitter]
