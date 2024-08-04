# Ordering Data
import random 
from sqlalchemy.orm import sessionmaker

from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()

# Query all the users
users_all = session.query(User).all()

# Query all the users with age greater than or equal to 25
users_filtered = session.query(User).filter(User.age >= 25).all()

print("All users: ", len(users_all))
print("All users: ", len(users_all))

session.commit()
