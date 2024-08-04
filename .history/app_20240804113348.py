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

# if you want to list all the users you can use for loop like this
# for user in users:
#     print(f"User id:{user.id}, name:{user.name}, age:{user.age}")

# if you want to filter the users you can use filter method
users = session.query(User).filter_by(age = 25).all() # you can also use one_or_none() method to access the single user if you know that there is only single user in the database(Table). and if you have many this will give you an error message

print(users)