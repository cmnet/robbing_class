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
