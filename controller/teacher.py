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


def insert_user2(teacher_id, teacher_Salary, teacher_DOJ, teacher_Employeeid, student1_id):
    query = "INSERT INTO teacher(id, Salary, DOJ, Employeeid, student1_id) VALUES('{}','{}','{}','{}','{}')".format(
        teacher_id,
        teacher_Salary,
        teacher_DOJ,
        teacher_Employeeid,
        student1_id)
    print(query)
    engine.execute(query)


insert_user2('12', '25000', '13', '1237', '12')
