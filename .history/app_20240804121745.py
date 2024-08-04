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

users = session.query(User).order_by('age').all()

for user in users:
    print(f"user age: ",)


    
    
    
    
session.commit()
