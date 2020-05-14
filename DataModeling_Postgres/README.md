# **Introduction**

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. Currently, the data resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app. In this project, I create a Postgres database schema and ETL pipeline to assist the analytics team in understanding what songs users are listening to. 


# **Database schema design and ETL process**

![Image of Song_ERD](./Song_ERD.png)


### **Files in repository**
***data***: The directory containing a collection of song files and log files.

***create_tables.py***: A python script to create tables according to the database schema design.

***sql_queries.py***: A python script used containing all SQL queries used for table creation. It is used by ***create_tables.py***

***etl.ipynb***: A jupyter-notebook processing ETL step by step. It is for development.

***etl.py***: A python script processing ETL. It contains all the codes developed in ***etl.ipynb***.

***test.ipynb***: A jupyter-notebook used for testing contents of tables during the process of table creation and ETL.


### **Table Creation**

Write statements in sql_queries.py to specify all columns for each of the five tables with the right data types and conditions. Run the command line below in terminal to create tables.

```
python3 create_tables.py
```

### **ETL**

Develop ETL for each table in the etl.ipynb notebook. Then implement etl.py, and then run the command line below in terminal to process the entire datasets.

```
python3 etl.py
```

### **Vaildation**

Run the jupyter-notebook ***test.ipynb*** to confirm that the records have been successfully inserted into each table.
