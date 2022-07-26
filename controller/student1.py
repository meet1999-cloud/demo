from asyncio.log import logger
import json
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import logging
from connect import engine

def insert_user(student1_id, student1_rollno, student1_batch, student1_level6, person_id):
    query = "INSERT INTO student1 (id,rollno,batch,level6,person_id) VALUES ('{}','{}','{}','{}','{}')".format(
        student1_id,
        student1_rollno,
        student1_batch,
        student1_level6,
        person_id)
    logger.info(query)
    engine.execute(query)


insert_user('13', '109', '2005', '10', '12')


def update_user2(newrollno):
    query = "UPDATE student1 SET RollNo='{}' WHERE id ='2';".format(newrollno)
    logger.info(query)
    engine.execute(query)


update_user2('105')


def delete_user3(student1_id):
    query = "DELETE from student1 WHERE id = '{}'".format(student1_id)
    logger.info(query)
    engine.execute(query)


delete_user3('1')
