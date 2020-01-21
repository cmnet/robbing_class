from model import *


def robbing(student_id: int, lesson_id: int) -> bool:
    lesson = Lesson.get(id=lesson_id)
    if lesson:
        lesson_student_number = lesson.student_number

        students = select(s for s in StudentLesson if s.lesson == lesson)
        had_robbing_student_number = len(students)
        if had_robbing_student_number < lesson_student_number:
            # 可以抢课
            student = Student.get(id=student_id)
            student_lesson = {
                "student": student,
                "lesson": lesson
            }
            StudentLesson(**student_lesson)
            return True
        else:
            # 名额已满，不可抢课
            return False
