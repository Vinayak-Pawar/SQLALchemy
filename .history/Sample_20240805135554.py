import pandas as pd
from sqlalchemy import create_engine

# Define your connection string
username = 'postgres'
password = '12345'
host = 'localhost'
port = '5432'
database = 'Real_Estate'

# Create the connection string
connection_string = f'postgresql://{username}:{password}@{host}:{port}/{database}'

# Create the database engine
engine = create_engine(connection_string)

# Define the path to your CSV file
csv_file_path = 'path/to/your/file.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Define the table name where you want to import the data
table_name = 'your_table_name'

# Import the data into PostgreSQL
df.to_sql(table_name, engine, if_exists='replace', index=False)

print("Data imported successfully!")
