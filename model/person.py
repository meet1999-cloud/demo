from sqlalchemy import create_engine, Column, String, Date, Numeric, Integer, ForeignKey
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


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    PhoneNumber = Column(Numeric(10))
    Email = Column(String(50))
    DOB = Column(Date())


class Student1(Base):
    __tablename__ = 'student1'
    id = Column(Integer, primary_key=True)
    RollNo = Column(Integer(), primary_key=True)
    Batch = Column(Integer())
    level5 = Column(Integer())
    person_id = Column(Integer, ForeignKey("person.id"))
    enrolled_id = Column(Integer, ForeignKey("enrolled.id"))


def my_var(engine, table_name, column):
    column_name = column.compile(dialect=engine.dialect)
    column_type = column.type.compile(engine.dialect)
    engine.execute('ALTER TABLE %s ADD COLUMN %s %s' % (table_name, column_name, column_type))


column = Column('level6', Integer, primary_key=True)


class Teacher(Base):
    __tablename__ = 'teacher'
    id = Column(Integer, primary_key=True)
    Salary = Column(Integer())
    Employeeid = Column(Integer(), primary_key=True)
    DOJ = Column(Integer)
    student1_id = Column(Integer, ForeignKey("student1.id"))


class Address(Base):
    __tablename__ = 'Address'
    id = Column(Integer, primary_key=True)
    Street = Column(String(50))
    City = Column(String(50))
    PostalCode = Column(Integer())
    Country = Column(String(50))
    # person_id = Column(Float, ForeignKey("person.id"))


Base.metadata.create_all(engine)
