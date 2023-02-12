# Dog_attacks_ETL
This is a short project where data about confirmed dog attacks inside the country gets extracted from a file , then it gets cleaned using Dataframes and finally it is loaded into a PostgreSQL database.

## Introduction

This project consists on the following:


- Extract a dataset called "Dog_attacks.csv" from Kaggle.
- Insert the dataset into a data frame using Python.
- Manipulate the dataset so unnecessary data is filtered and to resolve some character issues.
- Load the data frame inside a PostgreSQL database.
- Access the database to resolve a few data-related questions.

## Extract

First we download the dataset from [Kaggle about fatal dog attacks in the US during the 2022 year.](https://www.kaggle.com/datasets/kabhishm/fatal-dog-attacks-in-the-us-202022)


Then, using the Pandas module from Python, the dataset is loaded into a dataframe. Data frames are a powerful tool to modify huge amounts of data in a way that will be difficult to do with Excel.



## Transform
The information inside the dataframe however, is not yet ready to deploy and requires a couple of changes.


![original_df](https://user-images.githubusercontent.com/103103116/218300814-5dc667db-782a-48a2-bfc9-b97b165b9363.PNG)



For example, **the date should be split into two fields**: one field called "Month" and another called "Day". This is done to make queries, and obtain results, quicker.
The number of dogs of each attack is important. However, the mentioned number is inside the "Dog type" field and must be extracted to another field.


The end result will be like this:
![modified](https://user-images.githubusercontent.com/103103116/218300832-6863792e-44c6-4602-af25-d6674f9fbfd8.PNG)



## Load
The modified dataframe obtained in the previous step will then be loaded to a database, according to the needs of the client. In this project, the DBMS will be PostgreSQL.


The database can be either locally hosted or deployed in the cloud. The only information needed are the database credentials and location.


Once the information is successfully loaded, a client-software is needed to access the database and make queries. This project uses pgAdmin 4 but using other programs will get the same result.
