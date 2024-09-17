from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.sensors.external_task_sensor import ExternalTaskSensor
from airflow.utils.dates import days_ago
from datetime import timedelta
from datetime import datetime

# Function to run movie.py
def run_movie_py():
    exec(open('C://Users//SHUBHAM MADHESIYA//Desktop//premji_invest//scripts//pipeline_2.py').read())  # Replace with the correct path

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['smkgp268@gmail.com'],
    'email_on_failure': True,  # Sends email if the task fails
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

# Define the DAG
dag2 = DAG(
    'run_movie_py_dag',
    default_args=default_args,
    description='Run movie.py every day at 8 PM if the first DAG is successful',
    schedule_interval='0 20 * * *',  # 8 PM every day
    start_date=datetime(2024, 9, 16),
    catchup=False,
)

# Sensor to check if run_file_py_dag has succeeded
wait_for_file_dag = ExternalTaskSensor(
    task_id='wait_for_run_file_py_dag',
    external_dag_id='run_file_py_dag',  # The DAG ID of the first DAG
    external_task_id='run_file_py',     # The task ID in the first DAG
    allowed_states=['success'],         # Wait until the task in the first DAG succeeds
    failed_states=['failed', 'skipped'],
    mode='poke',  # 'poke' mode or 'reschedule' mode
    timeout=3600,  # Timeout after 1 hour
    dag=dag2,
)

# Task to run movie.py
run_movie_task = PythonOperator(
    task_id='run_movie_py',
    python_callable=run_movie_py,
    dag=dag2,
)

# Set the dependency: movie.py should run only after file.py is successful
wait_for_file_dag >> run_movie_task
