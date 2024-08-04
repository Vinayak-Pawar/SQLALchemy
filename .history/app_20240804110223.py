from sqlalchemy.orm import sessionmaker
from models import User, engine

Session = sessionmaker(bind=engine)

