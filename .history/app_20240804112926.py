# app.py
from models import User, engine
from sqlalchemy.orm import sessionmaker

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

# # Example: Add a new user
# user = User(name="John Doe", age=30)
# user_2 = User(name="Andrew Pip", age=25)
# user_3 = User(name="Iron Man", age=57)
# user_4 = User(name="Richard Rodriguez", age=25)
# session.add(user)
# session.add_all([user_2, user_3, user_4])  # Add multiple users at once
# session.commit()

users = session.query(User).all()
# To access a specific user, use the index

# user = users[0]
# print(user)

# print(user.id)
# print(user.name)
# print(user.age)

# 
# for user in users:
#     print(f"User id:{user.id}, name:{user.name}, age:{user.age}")
