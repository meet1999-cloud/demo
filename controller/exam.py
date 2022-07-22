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


def exam_user(exam_ExamDate, exam_Supervisior, exam_TotalMarks):
    query = "INSERT INTO exam(ExamDate,Supervisior,TotalMarks) VALUES('{}','{}','{}')".format(
        exam_ExamDate,
        exam_Supervisior,
        exam_TotalMarks
    )
    print(query)
    engine.execute(query)
    return id


exam_user('1999-08-12', 'Meet', '95')


def update1_user(newSupervisior):
    query = "UPDATE exam SET Supervisior='{}' WHERE id = '2'".format(newSupervisior)
    print(query)
    engine.execute(query)


update1_user('Misha')


def delete_user1(exam_Supervisior):
    query = "DELETE from exam WHERE Supervisior='{}'".format(exam_Supervisior)
    print(query)
    engine.execute(query)


delete_user1("Misha")
