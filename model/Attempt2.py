from sqlalchemy import create_engine, Column, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from person import Student1
from course import Exam
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


class Attempt2(Base):
    __tablename__ = 'Attempt2'
    Attempt2_id = Column(Integer, primary_key=True)
    Attempt2_Marks = Column(Integer)
    student1_id = Column(Integer, ForeignKey(Student1.id))
    exam_id = Column(Integer, ForeignKey(Exam.id))


def Attempt2_user(Attempt2_id, Attempt2_Marks, student1_id, exam_id):
    query = "INSERT INTO Attempt2 (Attempt2_id, Attempt2_Marks, student1_id, exam_id) VALUES('{}','{}','{}','{}')".format(
        Attempt2_id,
        Attempt2_Marks,
        student1_id,
        exam_id)
    print(query)
    engine.execute(query)


Attempt2_user('9', '40', '5', '6')


def user4():
    query = "SELECT * FROM Attempt2;"
    # print(query)
    result = engine.execute(query)
    print(result)
    passed = 0
    failed = 0
    avg = 0
    count = 1
    for r in result:
        print(r.Attempt2_Marks)
        if r.Attempt2_Marks >= 50:
            passed += 1
        elif r.Attempt2_Marks < 50:
            failed += 1
        avg += r.Attempt2_Marks
        count += 1

    avg /= count

    print(passed, failed, avg)



user4()
