from asyncio.log import logger
import json
from sqlalchemy import create_engine
import logging 
from connect import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


def exam_user(exam_examdate, exam_supervisior, exam_totalmarks):
    query = "INSERT INTO exam(examdate,supervisior,totalmarks) VALUES('{}','{}','{}')".format(
        exam_examdate,
        exam_supervisior,
        exam_totalmarks
    )
    logger.info(query)
    engine.execute(query)
    return id


exam_user('1999-08-12', 'Meet', '95')


def update1_user(newsupervisior):
    query = "UPDATE exam SET Supervisior='{}' WHERE id = '2'".format(newsupervisior)
    logger.info(query)
    engine.execute(query)


update1_user('Misha')


def delete_user1(exam_supervisior):
    query = "DELETE from exam WHERE Supervisior='{}'".format(exam_supervisior)
    logger.info(query)
    engine.execute(query)


delete_user1("Misha")