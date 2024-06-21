from airflow import DAG
from airflow.providers.amazon.aws.operators.glue import GlueJobOperator
from airflow.sensors.external_task_sensor import ExternalTaskSensor
from datetime import datetime, timedelta

default_args={
    'owner':'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023,8,12),
    'retries':1,
    'retry_delay':timedelta(minutes=5),
} 
dag =DAG('transform_redshift_dag', default_args=default_args, schedule_interval="@once", catchup=False)

# Task to upload the script to S3
upload_script = S3CreateObjectOperator(
    task_id='upload_script',
    s3_bucket='aws-glue-assets-637423317099-ap-southeast-1',
    s3_key='scripts/weather_data_ingestion.py',
    data=open('weather_data_ingestion.py').read(),
    replace=True,
    aws_conn_id='aws_default',
    dag=dag,
)

# Task to run the Glue job
transform_task = GlueJobOperator(
    task_id='transform_task',
    job_name='glue_transform_task',
    script_location='s3://aws-glue-assets-637423317099-ap-southeast-1/scripts/weather_data_ingestion.py',
    s3_bucket='aws-glue-assets-637423317099-ap-southeast-1',
    aws_conn_id='aws_default',
    region_name='ap-southeast-1',
    iam_role_name='my-role-for-proj',
    create_job_kwargs={
        'GlueVersion': '4.0',
        'NumberOfWorkers': 2,
        'WorkerType': 'G.1X',
        'Connections': {'Connections': ['Redshift connection']}
    },
    dag=dag,
)

# Set the task dependencies
upload_script >> transform_task