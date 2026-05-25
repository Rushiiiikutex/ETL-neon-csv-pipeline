# ETL Pipeline: Neon PostgreSQL → CSV

This project implements an ETL (Extract, Transform, Load) pipeline using Python.

## Features

- Extracts ERP data from a Neon PostgreSQL database
- Executes SQL queries using psycopg2
- Loads query results into pandas DataFrames
- Performs data transformations and column filtering
- Exports processed datasets to CSV files
- Uses environment variables (.env) for secure database credentials

## Tech Stack

- Python
- PostgreSQL (Neon)
- SQL
- pandas
- psycopg2
- python-dotenv

## Pipeline Flow

Neon PostgreSQL
↓
SQL Query
↓
psycopg2 Connection
↓
pandas DataFrame
↓
Transformations
↓
CSV Export
