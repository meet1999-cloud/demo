from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from demo.model.person import *

my_conn = create_engine(
    "mysql+pymysql://" + user + ":" + password + "@localhost:" + port + "/" + db + "?charset=utf8mb4")
Session = sessionmaker(bind=my_conn)
session = Session()
Base = declarative_base()


def insert_user(student1_id, student1_RollNo, student1_Batch, student1_level6, person_id):
    query = "INSERT INTO student1 (id,RollNo,Batch,level6,person_id) VALUES ('{}','{}','{}','{}','{}')".format(
        student1_id,
        student1_RollNo,
        student1_Batch,
        student1_level6,
        person_id)
    print(query)
    engine.execute(query)


insert_user('13', '109', '2005', '10', '12')


def update_user2(newRollNo):
    query = "UPDATE student1 SET RollNo='{}' WHERE id ='2';".format(newRollNo)
    print(query)
    engine.execute(query)


update_user2('105')


def delete_user3(student1_id):
    query = "DELETE from student1 WHERE id = '{}'".format(student1_id)
    print(query)
    engine.execute(query)


delete_user3('1')
