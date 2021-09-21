from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

from datetime import datetime, timedelta

default_args = {
    'start_date':days_ago(5),
    'retries':3,
    'retries_delay':timedelta(minutes=3)
    

}

with DAG(
    dag_id="my_dag_2",
    description="DAG é minha",
    default_args=default_args,
    #start_date=datetime(2021,1,1),
    schedule_interval='@daily',
    max_active_runs=4,
    
    catchup=True
    ) as dag:

    checking_data = BashOperator(
        task_id="bash_task",
        bash_command='exit 1'
    )



    #checking_data >> checking_data_2