import psycopg2
import pandas
from sqlalchemy import create_engine
import sqlite3

from psycopg2_lib import psycopg_queries
from sqlite_lib import sqlite_queries
from duckdb_lib import duckdb_queries
from pandas_lib import pandas_queries
from sqlalchemy_lib import sqlalchemy_queries
from config import *

# filling the database in Postgres
data = pandas.read_csv(f"{data_folder}/{dataset}")
data["tpep_pickup_datetime"] = pandas.to_datetime(data["tpep_pickup_datetime"])
data["tpep_dropoff_datetime"] = pandas.to_datetime(data["tpep_dropoff_datetime"]) 
data = data.rename(columns={"Unnamed: 0": "id"})
data = data.drop(columns=["Airport_fee"])

path = f"postgresql://{username}:{password}@{hostname}:{port}/{name_database}"
engine = create_engine(path)
data.to_sql("trips", engine, if_exists="replace", chunksize=10000)
engine.dispose()

# creating SQLite database
connection = sqlite3.connect(f"{data_folder}/postgres.db")
data.to_sql("trips", connection, if_exists="replace", chunksize=10000)
connection.close()

# running queries and getting results
if PSYCOPG2:
    print("Psycopg2 measurements: ", *psycopg_queries(), end='\n\n')

if SQLITE3:
    print("SQLite3 measurements: ", *sqlite_queries(), end='\n\n')

if DUCKDB:
    print("DuckDB measurements: ", *duckdb_queries(), end='\n\n')

if PANDAS:
    print("Pandas measurements: ", *pandas_queries(), end='\n\n')

if SQLALCHEMY:
    print("SQLalchemy measurements: ", *sqlalchemy_queries(), end='\n\n')
