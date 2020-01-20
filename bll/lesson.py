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
def query(name=None):
    if name:
        lessons = select(l for l in Lesson if name in l.name)      # find lesson
    else:
        lessons = select(l for l in Lesson)

    data = [
        {
            "id": lesson.id,
            "name": lesson.name,
            "teacher": lesson.teacher.name if lesson.teacher else '',
            "student_number": lesson.student_number,
            "start_time": lesson.start_time,
            "address": lesson.address,
            "price": lesson.price,
            "robbing_start_time": lesson.robbing_start_time,
            "robbing_end_time": lesson.robbing_end_time,
            "brief": lesson.brief,
            "remark": lesson.remark
        }
        for lesson in lessons
            ]
    return data

# ============================================


@db_session
def info(lesson_id):
    lesson = Lesson.get(id=lesson_id)
    data = {
            "id": lesson.id,
            "name": lesson.name,
            "teacher": lesson.teacher.name if lesson.teacher else "",
            "student_number": lesson.student_number,
            "start_time_year": lesson.start_time.split("年")[0],
            "start_time_month": lesson.start_time.split("月")[0],
            "start_time_day": lesson.start_time.split("日")[0],
            "start_time_hour": lesson.start_time.split("时")[0],
            "address_provence": lesson.address.split("省")[0],
            "address_city": lesson.address.split("市")[0],
            "address_area": lesson.address.split("区")[0],
            "address": lesson.address.split("区")[1],
            "price": lesson.price,
            "robbing_start_time": lesson.robbing_start_time,
            "robbing_end_time": lesson.robbing_end_time,
            "brief": lesson.brief,
            "remark": lesson.remark
        }
    return data
