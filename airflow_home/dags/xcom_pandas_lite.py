from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
import time
import pandas as pd


datapoints = ['{:06d}'.format(i) for i in range(1)]


def create_df_for_dp(**kwargs):
    kwargs['task_instance'].xcom_push(key='sleep', value={'a': 15, 'b': 30})


def merge_dfs(**context):
    sleep_time = context['task_instance'].xcom_pull(key='sleep')['a']
    time.sleep(sleep_time)

    # push by returning
    return 1


def b_task(**context):
    sleep_time = context['task_instance'].xcom_pull(key='sleep')['b']
    time.sleep(sleep_time)

    # push by returning
    return 2


def ab_task(**context):
    a, b = context['task_instance'].xcom_pull(task_ids=['a_task', 'b_task'])
    print('{} + {}: {}'.format(a, b, a + b))
    return (a + b)


dag = DAG('xcom_add', description='Simple tutorial DAG',
          schedule_interval=None,
          start_date=datetime(2018, 9, 3),
          catchup=False)


t_src = PythonOperator(task_id='source_task', python_callable=source_task, provide_context=True, dag=dag)
t_a = PythonOperator(task_id='a_task', python_callable=a_task, provide_context=True, dag=dag)
t_b = PythonOperator(task_id='b_task', python_callable=b_task, provide_context=True, dag=dag)
t_ab = PythonOperator(task_id='ab_task', python_callable=ab_task, provide_context=True, dag=dag)


t_src.set_downstream(t_a)
t_src.set_downstream(t_b)

t_ab.set_upstream(t_a)
t_ab.set_upstream(t_b)
