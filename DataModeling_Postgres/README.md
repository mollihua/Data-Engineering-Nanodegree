**Introduction**

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. Currently, the data resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app. In this project, I create a Postgres database schema and ETL pipeline to assist the analytics team in understanding what songs users are listening to. 


**Table Creation**

Write statements in sql_queries.py to specify all columns for each of the five tables with the right data types and conditions. Run "python3 create_tables.py" in terminal to create tables.


**ETL**
Develop ETL for each table in the etl.ipynb notebook. Then implement etl.py, and then run "python3 etl.py" in terminal to process the entire datasets.


**Vaildation**
Run the jupyter-notebook test.ipynb to confirm that the records have been successfully inserted into each table.