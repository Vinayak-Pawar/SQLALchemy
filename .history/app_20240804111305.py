# app.py
from models import User, engine
from sqlalchemy.orm import sessionmaker

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

# Example: Add a new user
user = User(name="John Doe", age=30)
user_2 = User(name="Andrew Pip", age=25)
user_3 = User(name="Iron Man", age=57)
user_4 = User(name="Richard Rodriguez", age=25)
session.add(user)
session.commit()