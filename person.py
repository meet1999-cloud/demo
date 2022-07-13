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


# def add_column(engine, table_name, column):
#     column_name = column.compile(dialect=engine.dialect)
#     column_type = column.type.compile(engine.dialect)
#     engine.execute('ALTER TABLE %s ADD COLUMN %s %s' % (table_name, column_name, column_type))
#
#
# column = Column('firstname', String(50), primary_key=True)
# column1 = Column('lastname', String(50))
# column2 = Column('PhoneNumber', Numeric(10))
# column3 = Column('Email', String(50))
# column4 = Column('DOB', (Date()))
#
# add_column(engine=engine, table_name='person', column=column1)
# add_column(engine=engine, table_name='person', column=column2)
# add_column(engine=engine, table_name='person', column=column3)
# add_column(engine=engine, table_name='person', column=column4)

class Student1(Base):
    __tablename__ = 'student1'
    id = Column(Integer, primary_key=True)
    RollNo = Column(Integer(), primary_key=True)
    Batch = Column(Integer())
    person_id = Column(Integer, ForeignKey("person.id"))


class Teacher(Base):
    __tablename__ = 'teacher'
    id = Column(Integer, primary_key=True)
    Salary = Column(Integer())
    Employeeid = Column(Integer(), primary_key=True)
    DOJ = Column(Integer())
    student1_id = Column(Integer, ForeignKey("student1.id"))


class Address(Base):
    __tablename__ = 'Address'
    id = Column(Integer, primary_key=True)
    Street = Column(String(50))
    City = Column(String(50))
    PostalCode = Column(Integer())
    Country = Column(String(50))
    person_id = Column(Integer, ForeignKey("person.id"))


Base.metadata.create_all(engine)
