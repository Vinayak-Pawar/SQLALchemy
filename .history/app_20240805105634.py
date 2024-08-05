# Grouping and Chaining Data
from sqlalchemy.orm import sessionmaker
from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()

# group users by age
users = session.query(User.age).group_by(User.age).all()








session.commit()