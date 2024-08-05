# Grouping and Chaining Data
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()


session.