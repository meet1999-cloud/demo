from sqlalchemy import create_engine, Column, Date, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from course import Course
from person import Student1

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


class Enrolled(Base):
    __tablename__ = 'enrolled'
    enrolled_id = Column(Integer, primary_key=True)
    Date = Column(Date)
    course_Id = Column(Integer, ForeignKey(Course.CourseId))
    student1_id = Column(Integer, ForeignKey(Student1.id))


Base.metadata.create_all(engine)


def enrolled_user(enrolleed_Date, enrolledcourse_Id, enrolledstudent1_id):
    query = "INSERT INTO enrolled(Date, course_Id, student1_id) VALUES('{}','{}','{}')".format(
        enrolleed_Date,
        enrolledcourse_Id,
        enrolledstudent1_id
    )
    print(query)
    engine.execute(query)


enrolled_user('2004-1-06', '6', '5')

