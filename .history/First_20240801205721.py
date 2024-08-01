from sqlalchemy import create_engine, Column, Integer, String
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

Base = declarative_base()

class user(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)
    
Base.metadata.create_all(engine)
