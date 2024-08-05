# Grouping and Chaining Data
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()


# Different Functionalities in func function with sample code
count: Count the number of rows.
python
Copy code
from sqlalchemy import func, select

count_query = select(func.count())
result = conn.execute(count_query)
print(result.scalar())










# group users by age
users = session.query(User.age, func.count(User.id)).group_by(User.age).all()

print(users)






session.commit()