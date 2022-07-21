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


def course_user(course_CourseId, course_Title, course_Level, course_Credits, course_Total, courseteacher_id):
    query = "INSERT INTO course(CourseId,Title,Level,Credits,Total,teacher_id) VALUES('{}','{}','{}','{}','{}','{}')".format(
        course_CourseId,
        course_Title,
        course_Level,
        course_Credits,
        course_Total,
        courseteacher_id)

    print(query)
    engine.execute(query)


course_user('7', 'Devops Engineer', '15', '7', '82', '2')
