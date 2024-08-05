# Ordering Data
import random 
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # we can also import and_ for doing and operations
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
# for user in users:
#     print(f"User age: {user.age}")

# print("All users: ", len(users_all))
# print("Filtered users: ", len(users_filtered))

users = session.query(User).filter(and_(User.age >= 30, User.name == 'Iron Man', User.id > 4)).all()

# In this "or_" function we can pass as many parameters as we want.
# We can also use Bitwise operators like " | " but remember to wrap your conditions like this "(User.age >= 30) | (User.name == 'Iron Man') | (User.id > 4)"
for user in users:
    print(f"{user.age}-{user.name} {user.id}")





session.commit()
