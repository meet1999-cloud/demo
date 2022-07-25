from sqlalchemy import create_engine, Column, String, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from connect import engine, Base
from person import Teacher
import json

class Course(Base):
    __tablename__ = 'course'
    course_id = Column(Integer, primary_key=True)
    title = Column(String(50))
    credits = Column(Integer)
    level = Column(Integer)
    total = Column(Integer)
    teacher_id = Column(Integer, ForeignKey(Teacher.id))


class Exam(Base):
    __tablename__ = 'exam'
    id = Column(Float, primary_key=True)
    examdate = Column(Date)
    supervisior = Column(String(50))
    totalmarks = Column(Integer)


Base.metadata.create_all(engine)
