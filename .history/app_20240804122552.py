# Ordering Data
import random 
from sqlalchemy.orm import sessionmaker

from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()

# We have created a random users in our database
# names = ['Andrew Pip', 'Iron Man', 'John Doe', 'Jane Doe']
# ages = [20, 21, 22, 23, 25, 27, 30, 35, 60]

# for x  in range (100):
#     user = User(name=random.choice(names), age=random.choice(ages))
#     session.add(user)



#query all users ordered by age(ascending)

# users = session.query(User).order_by(User.age.asc()).all()

# for user in users:
#     print(f"user age: {user.age},name:{user.name},id: {user.id}")
    
#query all users ordered by age(descending)
# users = session.query(User).order_by(User.age.desc()).all()

# for user in users:
#     print(f"user age: {user.age},name:{user.name},id: {user.id}")

#query all users ordered by age and name
users = session.query(User).order_by(User.age, User.name).all() # Take a note the first coulumn is age and the second column is name it will start the sort the starting age which is 20 and then in the group of 20 ages users   

for user in users:
    print(f"user age: {user.age},name:{user.name},id: {user.id}")
    
    
    
    
session.commit()
