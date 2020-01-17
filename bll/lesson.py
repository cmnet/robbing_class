#!/usr/bin/evn python
# -*- encoding:utf-8 -*-
from model import *
__author__ = "Jelly"

# ============================================

@db_session
def add(lsn):
    lesson = Lesson(**lsn)
    return lesson


@db_session
def delete(lesson_id):
    lesson = Lesson.get(id=lesson_id)
    if lesson:
        lesson.delete()
        commit()

# =============================================


@db_session
def update(lsn):
    lesson = Lesson.get(id=lsn["id"])
# ----------------------------------------------
    if lesson:
        lesson.name = lsn["name"]
        lesson.teacher = lsn["teacher"]
        lesson.student_number = lsn["student_number"]
        lesson.start_time = lsn["start_time"]
        lesson.address = lsn["address"]
        lesson.price = lsn["price"]
        lesson.robbing_start_time = lsn["robbing_start_time"]
        lesson.robbing_end_time = lsn["robbing_end_time"]
        lesson.brief = lsn["brief"]
        lesson.remark = lsn["remark"]
        commit()

# ============================================


@db_session
def query(name):
    lessons = select(l for l in Lesson if name in l.name)      # find lesson
    lesson_list = [lesson.to_dict() for lesson in lessons]
    return lesson_list
