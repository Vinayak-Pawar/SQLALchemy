# Ordering Data
i
from sqlalchemy import sessionmaker

from models import User, engine

Session = sessionmaker(bind=engine)
session = Sesssion()
