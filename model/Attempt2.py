from asyncio.log import logger
from sqlalchemy import create_engine, Column, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from connect import engine, Base
import logging
from person import Student1
from course import Exam
import json

class Attempt2(Base):
    __tablename__ = 'Attempt2'
    Attempt2_id = Column(Integer, primary_key=True)
    Attempt2_marks = Column(Integer)
    student1_id = Column(Integer, ForeignKey(Student1.id))
    exam_id = Column(Integer, ForeignKey(Exam.id))


def Attempt2_user(Attempt2_id, Attempt2_marks, student1_id, exam_id):
    query = "INSERT INTO Attempt2 (Attempt2_id, Attempt2_marks, student1_id, exam_id) VALUES('{}','{}','{}','{}')".format(
        Attempt2_id,
        Attempt2_marks,
        student1_id,
        exam_id)
    logger.info(query)
    engine.execute(query)


Attempt2_user('9', '40', '5', '6')


def user4():
    query = "SELECT * FROM Attempt2;"
    result = engine.execute(query)
    logger.info(result)
    passed = 0
    failed = 0
    avg = 0
    count = 1
    for r in result:
        logger.info(r.Attempt2_marks)
        if r.Attempt2_marks >= 50:
            passed += 1
        elif r.Attempt2_marks < 50:
            failed += 1
        avg += r.Attempt2_marks
        count += 1

    avg /= count

    logger.info(passed, failed, avg)



user4()
