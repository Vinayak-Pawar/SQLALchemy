# Ordering Data
import random 
from sqlalchemy.orm import sessionmaker

from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()

# Query all the users


session.commit()
