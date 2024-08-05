# Grouping and Chaining Data
from sqlalchemy.orm import sessionmaker# we can also import and_ for doing and operations
from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()