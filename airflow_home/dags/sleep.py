from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
import time


def sleep_0():
    time.sleep(0)


def sleep_2():
    time.sleep(2)


def sleep_4():
    time.sleep(4)


def sleep_8():
    time.sleep(8)


def sleep_16():
    time.sleep(16)


def sleep_32():
    time.sleep(32)


dag = DAG('sleep', description='Simple tutorial DAG',
          schedule_interval=None,
          start_date=datetime(2018, 9, 3),
          catchup=False)


t0 = PythonOperator(task_id='sleep_0', python_callable=sleep_0, dag=dag)
t2 = PythonOperator(task_id='sleep_2', python_callable=sleep_2, dag=dag)
t4 = PythonOperator(task_id='sleep_4', python_callable=sleep_4, dag=dag)
t8 = PythonOperator(task_id='sleep_8', python_callable=sleep_8, dag=dag)
t16 = PythonOperator(task_id='sleep_16', python_callable=sleep_16, dag=dag)
t32 = PythonOperator(task_id='sleep_32', python_callable=sleep_32, dag=dag)


t0 >> t2 >> t4 >> t8 >> t16 >> t32
