from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


import json

with open('/demo/config.json') as config:
    data = json.load(config)
user = data["username"]
password = data["password"]
db = data["database"]
port = data['host']



#cnx = create_engine('mariadb+pymysql://root:semilshah1534@localhost:3306/alchemy')
#cnx = create_engine("mysql+pymysql://root:password123@localhost:3306/alchemy?charset=utf8mb4")
cnx = create_engine ("mysql+pymysql://"+user+":"+password+"@localhost:"+port+"/"+db+"?charset=utf8mb4")
#cnx = create_engine("mysql+mysqlconnector://root:semilshah1534@localhost:3306/alchemy")

Session = sessionmaker(bind=cnx)
session = Session()

Base = declarative_base()

class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key =True)
    name = Column(String(50))
Base.metadata.create_all(cnx)