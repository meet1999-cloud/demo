from sqlalchemy import create_engine, Column, String, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import json

with open('/home/deuex-solutions/Desktop/code/demo/config.json') as config:
    data = json.load(config)
user = data["username"]
password = data["password"]
db = data["database"]
port = data['host']

engine = create_engine(
    "mysql+pymysql://" + user + ":" + password + "@localhost:" + port + "/" + db + "?charset=utf8mb4")

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Course(Base):
    __tablename__ = 'course'
    CourseId = Column(Integer, primary_key=True)
    Title = Column(String(50))
    Credits = Column(Float, primary_key=True)
    Level = Column(Integer)
    Total = Column(Integer)
    exam_id = Column(Integer, ForeignKey("exam.id")) ### Created a ForeignKey for a relationship between two Tables

class Exam(Base):
    __tablename__ = 'exam'
    id = Column(Integer, primary_key=True)
    ExamDate = Column(Date)
    Supervisior = Column(String(50))
    TotalMarks = Column(Integer)


Base.metadata.create_all(engine)
