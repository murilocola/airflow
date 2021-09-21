from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash import BashOperator

from datetime import datetime, timedelta

def _checking_data():
    print('teste task01')

def _checking_teste():
    print('teste 2')


with DAG(
                dag_id="my_dag",
                description="DAG é minha",
                start_date=datetime(2021,9,19),
                schedule_interval='@daily',
                #max_active_runs=1,
                tags=["mcola_my_dag"],
                catchup=False
 ) as dag:

    checking_data = PythonOperator(
        task_id="task_1",
        python_callable=_checking_data
        
    )

    checking_teste = PythonOperator(
        task_id="task_2",
        python_callable=_checking_teste
    )    

    checking_bash = BashOperator(
        task_id="bash_task",
        bash_command='exit 0'
    )

    checking_bash_2 = BashOperator(
        task_id="bash_task_2",
        bash_command='exit 0'
    )

    #checking_data>>checking_teste>>checking_bash>>checking_bash_2
    [checking_data,checking_teste,checking_bash,checking_bash_2]

    #checking_bash_2<<checking_bash<<checking_teste<<checking_data
