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


def user(course_id):
    query = "select count(enrolled_id) AS id FROM enrolled WHERE course_id='{}'".format(course_id)
    result = engine.execute(query)
    for row in result:
        print("course_id", row)
    return result


user('2')


def user1(teacher_id):
    query = "select count(CourseId) AS id FROM course WHERE teacher_id='{}'".format(teacher_id)
    result1 = engine.execute(query)
    for row1 in result1:
        print("teacher_id", row1)
    return result1


user1(2)




