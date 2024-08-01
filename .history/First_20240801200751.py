from sqlalchemy import create_engine

common 
engine = create_engine('sqlite:///college.db', echo=True)