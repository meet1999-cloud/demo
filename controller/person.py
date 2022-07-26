from asyncio.log import logger
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging
from connect import engine
from sqlalchemy.ext.declarative import declarative_base

def insert_user1(person_firstname, person_lastname, person_phonenumber, person_email, person_dob):
    query = "INSERT INTO person(firstname,lastname,phonenumber,email,dob) VALUES( '{}', '{}', '{}', '{}', '{}')".format(
        person_firstname,
        person_lastname,
        person_phonenumber,
        person_email,
        person_dob)

    logger.info(query)
    engine.execute(query)
    query = "SELECT id  FROM person WHERE Email='{}';".format(person_email)
    b = engine.execute(query)
    for row in b:
        logger.info("email", row[0])
    return id


insert_user1('Rohan', 'Sanghvi', '7039614709', 'parita.s16@gmail.com', '1973-04-16')


def update_user(newname):
    query = "UPDATE person SET firstname='{}' WHERE id = '1';".format(newname)
    logger.info(query)
    engine.execute(query)


update_user('Rohan')


def delete_user(person_id):
    query = "DELETE from person WHERE id = '{}'".format(person_id)
    logger.info(query)
    engine.execute(query)


delete_user("43")
