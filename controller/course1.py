import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from connect import engine
from sqlalchemy.ext.declarative import declarative_base

def course_user(course_course_id, course_title, course_level, course_credits, course_total, courseteacher_id):
    query = "INSERT INTO course(course_id,title,level,credits,total,teacher_id) VALUES('{}','{}','{}','{}','{}','{}')".format(
        course_course_id,
        course_title,
        course_level,
        course_credits,
        course_total,
        courseteacher_id)

    print(query)
    engine.execute(query)


course_user('7', 'Devops Engineer', '15', '7', '82', '2')
