#!/usr/bin/evn python
# -*- encoding:utf-8 -*-
from model import *
__author__ = "CM"


@db_session
def add(t):
    teacher = Teacher(**t)
    return teacher


@db_session
def delete(teacher_id):
    teacher = Teacher.get(id=teacher_id)
    if teacher:
        teacher.delete()
        commit()


@db_session
def update(teacher):
    t = Teacher.get(id=teacher["id"])
    if t:
        t.name = teacher["name"]
        t.photo = teacher["photo"]
        t.brief = teacher["brief"]
        commit()

@db_session
def info(teacher_id):
    t = Teacher.get(id=teacher_id)
    data ={
            "id":t.id,
            "name":t.name,
            "photo":t.photo,
            "brief":t.brief,
            "lessons":[lesson.to_dict() for lesson in t.lessons]        
        }

    return data

@db_session
def query(keyword: str = None) ->list:
    if keyword:
        teachers = select(t for t in Teacher if keyword in t.name or keyword in t.brief)
    else:
        teachers = select(t for t in Teacher)

    teacher_list = [t.to_dict() for t in teachers]


    data = [
        {
            "id":t.id,
            "name":t.name,
            "photo":t.photo,
            "brief":t.brief,
            "lessons":[lesson.to_dict() for lesson in t.lessons]        
        }
        for t in teachers
    ]

    return data


