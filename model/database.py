from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker
from connect import engine
from sqlalchemy.ext.declarative import declarative_base


import json

with open('/demo/config.json') as config:
    data = json.load(config)
user = data["username"]
password = data["password"]
db = data["database"]
port = data['host']

engine = create_engine ("mysql+pymysql://"+user+":"+password+"@localhost:"+port+"/"+db+"?charset=utf8mb4")

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key =True)
    name = Column(String(50))
Base.metadata.create_all(engine)