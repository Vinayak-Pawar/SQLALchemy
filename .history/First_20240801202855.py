from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

# common database connection template to follow: "dialect+driver://username:password@host:port/database"

username = 'postgres'
password = '12345'  # Replace with your actual password
host = 'localhost'
port = '5432'
database = 'postgres'

connection_string = f'postgresql://{username}:{password}@{host}:{port}/{database}'

# Create an engine
engine = create_engine(connection_string)