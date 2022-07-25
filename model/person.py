from sqlalchemy import create_engine, Column, String, Date, Numeric, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from connect import engine, Base
import json

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    phonenumber = Column(Numeric(10))
    email = Column(String(50))
    dob = Column(Date())


class Student1(Base):
    __tablename__ = 'student1'
    id = Column(Integer, primary_key=True)
    rollno = Column(Integer(), primary_key=True)
    batch = Column(Integer())
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
    salary = Column(Integer())
    employee_id = Column(Integer(), primary_key=True)
    doj = Column(Integer)
    student1_id = Column(Integer, ForeignKey("student1.id"))


class Address(Base):
    __tablename__ = 'Address'
    id = Column(Integer, primary_key=True)
    street = Column(String(50))
    city = Column(String(50))
    postalcode = Column(Integer())
    country = Column(String(50))

Base.metadata.create_all(engine)
