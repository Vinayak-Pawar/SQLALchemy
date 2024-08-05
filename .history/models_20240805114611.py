# models.py
from sqlalchemy import (create_engine, Column, Integer, String, ForeignKey)
from sqlalchemy.orm import declarative_base, relationship,sessionmaker

# common database connection template to follow: "dialect+driver://username:password@host:port/database"

username = 'postgres'
password = '12345'  # Replace with your actual password
host = 'localhost'
port = '5432'
database = 'postgres'

connection_string = f'postgresql://{username}:{password}@{host}:{port}/{database}'

# Create an engine
engine = create_engine(connection_string)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class User(Base):  # Class name should be 'User' to match the import
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    
Base.metadata.create_all(engine)


# There are different ways Mapped and Un