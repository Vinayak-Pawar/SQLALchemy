# Ordering Data
import random 
from sqlalchemy.orm import sessionmaker

from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()

# Query all the users
users_all = session.query(User).all()

# Query all the users


session.commit()
