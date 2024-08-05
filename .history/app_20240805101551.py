# Ordering Data
import random 
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_
from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()

# Query all the users
# users_all = session.query(User).all()

# # Query all the users with age greater than or equal to 25
# users_filtered = session.query(User).filter(User.age >= 25).all()

# Query all the users with age greater than or equal to 25
# users_filtered = session.query(User).filter(User.age >= 25, User.name == 'Iron Man').all()

# Query all the users with age equal to 30
# users = session.query(User).filter(User.age >= 25).all()

# filter vs filter_by:
# filter: Used for more complex queries and supports a wide range of conditions using column attributes.
# filter_by: Simplified version used for equality checks (e.g., filter_by(name='Iron Man')). so when you want to check like "==","=" use filter_by. 
for user in users:
    print(f"User age: {user.age}")

# print("All users: ", len(users_all))
# print("Filtered users: ", len(users_filtered))








session.commit()
