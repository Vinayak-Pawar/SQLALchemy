from sqlalchemy import create_engine

# common database connection template to follow: "dialect+driver://username:password@host:port/database"
engine = create_engine('sqlite:///college.db', echo=True)