# Grouping and Chaining Data
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import
from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()

# group users by age
users = session.query(User.age).group_by(User.age).all()

print(users)






session.commit()