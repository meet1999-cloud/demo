from asyncio.log import logger
from sqlalchemy import create_engine, Column, Date, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from connect import engine, Base
import logging 
from course import Course
from person import Student1
import json

class Enrolled(Base):
    __tablename__ = 'enrolled'
    enrolled_id = Column(Integer, primary_key=True)
    date = Column(Date)
    course_Id = Column(Integer, ForeignKey(Course.CourseId))
    student1_id = Column(Integer, ForeignKey(Student1.id))


def enrolled_user(enrolleed_Date, enrolledcourse_Id, enrolledstudent1_id):
    query = "INSERT INTO enrolled(Date, course_Id, student1_id) VALUES('{}','{}','{}')".format(
        enrolleed_Date,
        enrolledcourse_Id,
        enrolledstudent1_id
    )
    logger.info(query)
    engine.execute(query)


enrolled_user('2004-1-06', '6', '5')
Base.metadata.create_all(engine)
