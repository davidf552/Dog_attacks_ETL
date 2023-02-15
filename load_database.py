import psycopg2 
from dog_functions import *

conn = psycopg2.connect(
             host="localhost",
             database="first_test_db",
             port = "5432",
             user="user",
             password="password")

print("Database connection started")

cursor = conn.cursor()
create_dog_table(conn, cursor)

with open("dog_analysis.csv","r") as f:
    populate_dog_table(conn,cursor,f)
    

closing(conn,cursor)
