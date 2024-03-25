from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime,timedelta

default_args = {
    'owner':'Pedro',
    'retries':5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
        dag_id='Data_pipeline',
        default_args=default_args,
        description='Extract Transform and load data from TMDB API',
        start_date=datetime(2024,3,25,12)
    ) as pipeline:
    extract= PythonOperator(
        task_id='Extract',
        python_callable=function
    ),
    transform=PythonOperator(
        task_id='Transform',
        python_callable=function
    )
    load=PythonOperator(
        task_id='Load',
        python_callable=function
    )

extract >> transform >> load