from asyncio.log import logger
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from connect import engine
import logging
from sqlalchemy.ext.declarative import declarative_base

def insert_user2(teacher_id, teacher_salary, teacher_doj, teacher_employee_id, student1_id):
    query = "INSERT INTO teacher(id, Salary, DOJ, Employeeid, student1_id) VALUES('{}','{}','{}','{}','{}')".format(
        teacher_id,
        teacher_salary,
        teacher_doj,
        teacher_employee_id,
        student1_id)
    logger.info(query)
    engine.execute(query)


insert_user2('12', '25000', '13', '1237', '12')
