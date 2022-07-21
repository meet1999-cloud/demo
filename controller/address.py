import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

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


def address_user(Address_Street, Address_City, Address_PostalCode, Address_Country):
    query = "INSERT INTO Address(Street,City,PostalCode,Country) VALUES('{}','{}','{}','{}')".format(
        Address_Street,
        Address_City,
        Address_PostalCode,
        Address_Country)
    print(query)
    engine.execute(query)
    return id


address_user('NintyFeetRoad', 'Mumbai', '401103', 'India')


def updatemy_user(newStreet):
    query = "UPDATE Address SET Street = '{}' WHERE id = '2'".format(newStreet)
    print(query)
    engine.execute(query)


updatemy_user('BangladeshGround')


def deletemy_user1(newStreet):
    query = "DELETE from Address WHERE Street = '{}'".format(newStreet)
    print(query)
    engine.execute(query)



deletemy_user1('BangladeshGround')
