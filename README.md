**Weather Data Pipeline using OpenWeatherMap API**
------------------------------------------------------------

This project demonstrates a real-time data pipeline that collects weather data using the [OpenWeatherMap API](https://openweathermap.org/api), stores it in Amazon S3, transforms it using AWS Glue, and loads the processed data into Amazon Redshift for analytics. The workflow is orchestrated using Apache Airflow.

 **Project Overview**
 ----------------------------

- Collects real-time weather data via REST API.
- Stores raw data as CSV files in an S3 data lake.
- Schedules and manages ETL processes using Apache Airflow DAGs.
- Performs data transformation and cleaning using AWS Glue.
- Loads transformed data into Amazon Redshift for analysis.
- Sends notifications using Amazon SNS upon job success or failure.

**Outcome**
----------------

The pipeline automatically ingests, processes, and stores weather data for analysis in Redshift. This helps demonstrate a real-world ETL workflow using AWS services and open data.
