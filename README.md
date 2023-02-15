# Dog_attacks_ETL
This is a short project where data about confirmed dog attacks inside the country gets extracted from a file , then it gets cleaned using Dataframes and finally it is loaded into a PostgreSQL database.

## Introduction

This project consists on the following:


- [Extract](#extract) a dataset called "Dog_attacks.csv" from Kaggle.
- [Insert](#extract) the dataset into a data frame using Python.
- [Manipulate](#transform) the dataset so unnecessary data is filtered and to resolve some character issues.
- [Load](#load) the data frame inside a PostgreSQL database.
- [Access](#data) the database to resolve a few data-related questions.

## Extract

First we download the dataset from [Kaggle about fatal dog attacks in the US during the 2022 year.](https://www.kaggle.com/datasets/kabhishm/fatal-dog-attacks-in-the-us-202022)


![original](https://user-images.githubusercontent.com/103103116/218973164-7b5da192-0404-45fd-afd4-62533bf5fa86.PNG)


Then, using the Pandas module from Python, the dataset is loaded into a dataframe. Data frames are a powerful tool to modify huge amounts of data in a way that will be difficult to do with Excel.


![dataframe](https://user-images.githubusercontent.com/103103116/218973926-6dd5b705-3e6d-4951-b5cf-0b7e42b3685d.PNG)



[Return](#introduction)

## Transform
The information inside the dataframe however, is not yet ready to deploy and requires a couple of changes.


![original_df](https://user-images.githubusercontent.com/103103116/218300814-5dc667db-782a-48a2-bfc9-b97b165b9363.PNG)



For example, **the date should be split into two fields**: one field called "Month" and another called "Day". This is done to make queries, and obtain results, quicker.
The number of dogs of each attack is important. However, the mentioned number is inside the "Dog type" field and must be extracted to another field.


The end result will be like this:
![modified](https://user-images.githubusercontent.com/103103116/218300832-6863792e-44c6-4602-af25-d6674f9fbfd8.PNG)


[Return](#introduction)


## Load
The modified dataframe obtained in the previous step will then be loaded to a database, according to the needs of the client. The database can be either locally hosted or deployed in the cloud.
In this project, the database system will be PostgreSQL and the loading will be done using a Python script.


Once the information is successfully loaded, a client-software is needed to access the database and make queries. This project uses pgAdmin 4 as a client.

![database](https://user-images.githubusercontent.com/103103116/218972517-43d9bafb-223e-4016-8779-81fef6776d0e.PNG)

[Return](#introduction)
### Data
In this section, the database will be queried to provide some information:


- The total of dog attacks per month during the year 2022.

![attacks_month](https://user-images.githubusercontent.com/103103116/218970311-88f16ef2-3735-415f-b9d1-67fdde0bda66.PNG)


- The total of dog attacks per state during the year 2022.

![attacks_state](https://user-images.githubusercontent.com/103103116/218970508-9ed9b76e-f241-4652-a36d-0f2a5e015a1a.PNG)

- The average of dog attacks per state during the year 2022.

![average](https://user-images.githubusercontent.com/103103116/218970612-8807ed61-19d9-494a-91fd-32191dd6de79.PNG)

- The average of dog attacks per month during the year 2022.

![avg_month](https://user-images.githubusercontent.com/103103116/218970733-c11edf8d-0163-4eac-96f4-e5e49454e405.PNG)


- The top 3 states with dog attacks during the year 2022.

![top_three](https://user-images.githubusercontent.com/103103116/218971332-2b89eef5-7b00-488f-a275-fc63cc16cf28.PNG)


[Return](#introduction)
