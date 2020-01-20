#!/usr/bin/evn python
# -*- encoding:utf-8 -*-
from model import *
__author__ = "CM"


@db_session
def add(s: dict) -> Student:
    student = Student(**s)
    return student


@db_session
def delete(student_id: int):
    """
    student_id: 学生ID
    """
    student = Student.get(id=student_id)
    if student:
        student.delete()
        commit()


@db_session
def update(student: dict):
    """

    """
    s = Student.get(id=student["id"])
    if s:
        s.name = student["name"]
        s.mobile = student["mobile"]
        s.enroll_year = student["enroll_year"]
        s.class_name = student["class_name"]
        commit()


@db_session
def info(student_id: int) -> dict:
    """
    student_id: 学生id
    """
    s = Student.get(id=student_id)
    data = {
        "id": s.id,
        "name": s.name,
        "enroll_year": s.enroll_year,
        "lessons": [lesson.to_dict() for lesson in s.lessons]
    }
    return data


@db_session
def query(name: str = None) -> list:
    """
    @param name:
    @return:
    """
    if name:
        students = select(s for s in Student if name in s.name)
    else:
        students = select(s for s in Student)

    data = [
        {
            "id": s.id,
            "name": s.name,
            "enroll_year": s.enroll_year,
            "lessons": [lesson.to_dict() for lesson in s.lessons]
        }
        for s in students
    ]

    return data
