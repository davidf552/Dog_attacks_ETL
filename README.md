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

First we download the dataset from ![Kaggle about fatal dog attacks in the US during the 2022 year.](https://www.kaggle.com/datasets/kabhishm/fatal-dog-attacks-in-the-us-202022)


Then, using the Pandas module from Python, the dataset is loaded into a dataframe. Data frames are a powerful tool to modify huge amounts of data in a way that will be difficult to do with Excel.

