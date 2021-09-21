from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from datetime import datetime, timedelta

def _checking_data():
    print('teste task01')




with DAG(
                dag_id="my_dag",
                description="DAG é minha",
                start_date=datetime(2021,9,19),
                schedule_interval='@daily',
                max_active_runs=1,
                tags=["mcola_my_dag"],
                catchup=True
 ) as dag:

    checking_data = PythonOperator(
        task_id="task_1",
        python_callable=_checking_data
        
    )    
