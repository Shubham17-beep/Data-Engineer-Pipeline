from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
from airflow.utils.email import send_email
from datetime import datetime

# Function to run file.py
def run_file_py():
    exec(open('C://Users//SHUBHAM MADHESIYA//Desktop//premji_invest//scripts//pipeline_1.py').read())

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['smkgp268@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag1 = DAG(
    'run_file_py_dag',
    default_args=default_args,
    description='Run file.py every day at 7 PM',
    schedule_interval='0 19 * * *',  # 7 PM every day
    start_date=datetime(2024, 9, 16),
    catchup=False,
)

# Task to run file.py
run_file_task = PythonOperator(
    task_id='run_file_py',
    python_callable=run_file_py,
    dag=dag1,
)

run_file_task
