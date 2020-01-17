#!/usr/bin/evn python
# -*- encoding:utf-8 -*-
from model import *
__author__ = "CM"

@db_session
def add(s):
    student = Student(**s)
    return student

@db_session
def delete(student_id):
    student = student.get(id=student_id)
    student.delete()
    commit()

@db_session
def update(student):
    s= Student.get(id=student["id"])
    s.name = student["name"]
    s.mobile = student["mobile"]
    s.enroll_year = student["enroll_year"]
    s.class_name = student["class_name"]
    commit()

    
