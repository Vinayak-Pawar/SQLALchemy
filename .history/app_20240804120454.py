# Ordering Data
import random 
from sqlalchemy import sessionmaker

from models import User, engine

Session = sessionmaker(bind=engine)
session = Sesssion()

names = ['Andrew Pip', 'Iron Man', 'John Doe', 'Jane Doe']
ages = [20, 21, 22, 23, 25, 27, 30, 35, 60]

for x  in range (100)