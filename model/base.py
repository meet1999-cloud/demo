from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from connect import engine
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()