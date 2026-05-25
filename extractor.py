import os
import logging
import psycopg2
import pandas as pd 
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

conn=psycopg2.connect(DATABASE_URL)

query='''SELECT * FROM "User";'''

df=pd.read_sql_query(query,conn)

print(df.head())

conn.close()

#transformation 

df["role"]=df["role"].str.lower()
df=df.drop_duplicates()

print(df.head())

df.to_csv("transformed_data.csv",index=False)
