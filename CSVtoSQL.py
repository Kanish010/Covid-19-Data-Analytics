import psycopg2
import pandas as pd
import numpy as np
from io import StringIO
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Database connection parameters from the .env file
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
          
# Establish connection to PostgreSQL
try:
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cursor = conn.cursor()
    print("Database connection established.")
except Exception as e:
    print(f"Error connecting to the database: {e}")
    exit(1)

# Function to upload data to a table using INSERT
def upload_to_db_insert(df, table_name):
    # Convert dataframe to a list of tuples
    tuples = [tuple(x) for x in df.to_numpy()]
    
    # Generate the column names and the placeholder symbols
    cols = ','.join(list(df.columns))
    values = ','.join(['%s'] * len(df.columns))
    
    # SQL query to insert data
    query = f"INSERT INTO {table_name}({cols}) VALUES ({values})"
    
    try:
        cursor.executemany(query, tuples)
        conn.commit()
        print(f"Data inserted into {table_name} successfully.")
    except Exception as e:
        print(f"Error inserting data into {table_name}: {e}")
        conn.rollback()

# Function to upload data to a table using COPY (more efficient for large datasets)
def upload_to_db_copy(df, table_name, columns):
    buffer = StringIO()
    df.to_csv(buffer, index=False, header=False)
    buffer.seek(0)
    
    try:
        cursor.copy_from(buffer, table_name, sep=',', columns=columns, null='')
        conn.commit()
        print(f"Data inserted into {table_name} successfully using COPY.")
    except Exception as e:
        print(f"Error inserting data into {table_name} using COPY: {e}")
        conn.rollback()

# Load and process CSV files
def load_and_process_csv(file_path, column_names, numeric_columns=None):
    try:
        df = pd.read_csv(file_path)
        print(f"Loaded CSV file: {file_path}")
    except Exception as e:
        print(f"Error loading CSV file {file_path}: {e}")
        return None
    
    # Rename columns to match the table schema
    df.columns = column_names
    print(f"Renamed columns for {file_path}.")
    
    # Replace infinite values with NaN
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    
    # Convert specified columns to numeric types
    if numeric_columns:
        for col in numeric_columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        print(f"Converted numeric columns for {file_path}.")
    
    return df

# Define CSV files and their corresponding table details
csv_tables = [
    {
        'file_path': 'Dataset/country_wise_latest.csv',
        'table_name': 'country_wise_latest',
        'column_names': [
            'country_region', 'confirmed', 'deaths', 'recovered', 'active', 
            'new_cases', 'new_deaths', 'new_recovered', 'deaths_per_100_cases', 
            'recovered_per_100_cases', 'deaths_per_100_recovered', 
            'confirmed_last_week', 'one_week_change', 'one_week_percent_increase', 
            'who_region'
        ],
        'numeric_columns': [
            'confirmed', 'deaths', 'recovered', 'active', 'new_cases', 
            'new_deaths', 'new_recovered', 'deaths_per_100_cases', 
            'recovered_per_100_cases', 'deaths_per_100_recovered', 
            'confirmed_last_week', 'one_week_change', 'one_week_percent_increase'
        ],
        'use_copy': True  # Using COPY for this table as it might be large
    },
    {
        'file_path': '/mnt/data/covid_19_clean_complete.csv',
        'table_name': 'covid_19_clean_complete',
        'column_names': [
            'province_state', 'country_region', 'lat', 'long', 'date', 
            'confirmed', 'deaths', 'recovered', 'active', 'who_region'
        ],
        'numeric_columns': [
            'lat', 'long', 'confirmed', 'deaths', 'recovered', 'active'
        ],
        'use_copy': True  # Using COPY for this large table
    },
    {
        'file_path': 'Dataset/day_wise.csv',
        'table_name': 'day_wise',
        'column_names': [
            'date', 'confirmed', 'deaths', 'recovered', 'active', 
            'new_cases', 'new_deaths', 'new_recovered', 'deaths_per_100_cases', 
            'recovered_per_100_cases', 'deaths_per_100_recovered', 'no_of_countries'
        ],
        'numeric_columns': [
            'confirmed', 'deaths', 'recovered', 'active', 'new_cases', 
            'new_deaths', 'new_recovered', 'deaths_per_100_cases', 
            'recovered_per_100_cases', 'deaths_per_100_recovered', 'no_of_countries'
        ],
        'use_copy': False  # Using INSERT for this table
    },
    {
        'file_path': 'Dataset/worldometer_data.csv',
        'table_name': 'worldometer_data',
        'column_names': [
            'country', 'continent', 'population', 'total_cases', 'new_cases', 
            'total_deaths', 'new_deaths', 'total_recovered', 'new_recovered', 
            'active_cases', 'serious_critical', 'total_cases_per_million', 
            'deaths_per_million', 'total_tests', 'tests_per_million', 
            'who_region'
        ],
        'numeric_columns': [
            'population', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 
            'total_recovered', 'new_recovered', 'active_cases', 'serious_critical', 
            'total_cases_per_million', 'deaths_per_million', 'total_tests', 
            'tests_per_million'
        ],
        'use_copy': False
    }
]

# Process and upload each CSV
for table in csv_tables:
    df = load_and_process_csv(
        file_path=table['file_path'],
        column_names=table['column_names'],
        numeric_columns=table.get('numeric_columns', None)
    )
    
    if df is not None:
        if table['use_copy']:
            # Use COPY method
            upload_to_db_copy(df, table['table_name'], table['column_names'])
        else:
            # Use INSERT method
            upload_to_db_insert(df, table['table_name'])
    else:
        print(f"Skipping upload for table {table['table_name']} due to loading issues.")

# Close the connection
cursor.close()
conn.close()
print("Database connection closed.")