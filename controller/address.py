from asyncio.log import logger
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from connect import engine
import logging
from sqlalchemy.ext.declarative import declarative_base


def address_user(Address_street, Address_city, Address_postalcode, Address_country):
    query = "INSERT INTO Address(street,city,postalcode,country) VALUES('{}','{}','{}','{}')".format(
        Address_street,
        Address_city,
        Address_postalcode,
        Address_country)
    logger.info(query)
    engine.execute(query)
    return id


address_user('NintyFeetRoad', 'Mumbai', '401103', 'India')


def updatemy_user(newstreet):
    query = "UPDATE Address SET Street = '{}' WHERE id = '2'".format(newstreet)
    logger.info(query)
    engine.execute(query)


updatemy_user('BangladeshGround')


def deletemy_user1(newstreet):
    query = "DELETE from Address WHERE Street = '{}'".format(newstreet)
    logger.info(query)
    engine.execute(query)



deletemy_user1('BangladeshGround')