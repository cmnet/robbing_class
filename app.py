
from flask import Flask, render_template, request, redirect
from bll import student, lesson, teacher
from model import *

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, world!"


@app.route('/teacher/list')
def teacher_list():
    teachers = teacher.query()
    return render_template('teacher.html',data=teachers)


@app.route("/teacher/add")
def add_teacher():
    return render_template("add_teacher.html")


@app.route("/teacher/edit")
def edit_teacher():
    teacher_id = request.args["id"]
    data = teacher.info(int(teacher_id))
    return render_template("edit_teacher.html",teacher=data)


@app.route("/teacher/save", methods=["POST"])
def save_teacher():
    name = request.form["name"]
    brief = request.form["brief"]

    _teacher = {"name":name,"brief":brief}

    teacher.add(_teacher)
    return redirect("/teacher/list")
    # photo = requst.files[0]
    

@app.route("/teacher/update", methods=["POST"])
def update_teacher():
    id = request.form["id"]
    name = request.form["name"]
    brief = request.form["brief"]

    _teacher = {"name": name, "brief": brief, "id": int(id), "photo": ""}

    teacher.update(_teacher)

    return redirect("/teacher/list")


@app.route("/teacher/delete")
def delete_teacher():
    teacher_id = request.args["id"]
    teacher.delete(int(teacher_id))
    return redirect("/teacher/list")


@app.route('/lesson/list')
def lesson_list():
    res = lesson.query()
    return render_template('lesson.html', data=res, length=len(res))


@app.route("/lesson/add")
def add_lesson():
    return render_template('add_lesson.html')


@app.route("/lesson/edit")
def edit_lesson():
    lesson_id = request.args["id"]
    data = lesson.info(int(lesson_id))
    return render_template('edit_lesson.html', lesson=data)


@app.route("/lesson/save", methods=["POST"])
@db_session
def save_lesson():
    name = request.form["name"]
    teacher = Teacher.get(id=int(request.form["teacher"]))
    student_number = request.form["student_number"]
    start_time_year = request.form["start_time_year"]
    start_time_month = request.form["start_time_month"]
    start_time_day = request.form["start_time_day"]
    start_time_hour = request.form["start_time_hour"]
    address_province = request.form["address_province"]
    address_city = request.form["address_city"]
    address_area = request.form["address_area"]
    address = request.form["address"]
    price = request.form["price"]
    robbing_start_time_month = request.form["robbing_start_time_month"]
    robbing_start_time_day = request.form["robbing_start_time_day"]
    robbing_start_time_hour = request.form["robbing_start_time_hour"]
    robbing_end_time_month = request.form["robbing_start_time_month"]
    robbing_end_time_day = request.form["robbing_start_time_day"]
    robbing_end_time_hour = request.form["robbing_start_time_hour"]
    brief = request.form["brief"]
    remark = request.form["remark"]

    res = {
        "name": name,
        "teacher": teacher,
        "student_number": student_number,
        "start_time": "{}年{}月{}日{}时".format(start_time_year, start_time_month, start_time_day, start_time_hour),
        "address": "{}省{}市{}区{}".format(address_province, address_city, address_area, address),
        "price": price,
        "robbing_start_time": "{}月{}日{}时".format(robbing_start_time_month, robbing_start_time_day,
                                                 robbing_start_time_hour),
        "robbing_end_time": "{}月{}日{}时".format(robbing_end_time_month, robbing_end_time_day, robbing_end_time_hour),
        "brief": brief,
        "remark": remark
    }
    lesson.add(res)
    return redirect('/lesson/list')


@app.route("/lesson/update", methods=["POST"])
@db_session
def update_lesson():
    id = request.form["id"]
    name = request.form["name"]
    teacher = Teacher.get(id=int(request.form["teacher"]))
    student_number = request.form["student_number"]
    start_time_year = request.form["start_time_year"]
    start_time_month = request.form["start_time_month"]
    start_time_day = request.form["start_time_day"]
    start_time_hour = request.form["start_time_hour"]
    address_province = request.form["address_province"]
    address_city = request.form["address_city"]
    address_area = request.form["address_area"]
    address = request.form["address"]
    price = request.form["price"]
    robbing_start_time_month = request.form["robbing_start_time_month"]
    robbing_start_time_day = request.form["robbing_start_time_day"]
    robbing_start_time_hour = request.form["robbing_start_time_hour"]
    robbing_end_time_month = request.form["robbing_start_time_month"]
    robbing_end_time_day = request.form["robbing_start_time_day"]
    robbing_end_time_hour = request.form["robbing_start_time_hour"]
    brief = request.form["brief"]
    remark = request.form["remark"]

    res = {
        "id": int(id),
        "name": name,
        "teacher": teacher,
        "student_number": student_number,
        "start_time": "{}年{}月{}日{}时".format(start_time_year, start_time_month, start_time_day, start_time_hour),
        "address": "{}省{}市{}区{}".format(address_province, address_city, address_area, address),
        "price": price,
        "robbing_start_time": "{}月{}日{}时".format(robbing_start_time_month, robbing_start_time_day,
                                                 robbing_start_time_hour),
        "robbing_end_time": "{}月{}日{}时".format(robbing_end_time_month, robbing_end_time_day, robbing_end_time_hour),
        "brief": brief,
        "remark": remark
    }
    lesson.update(res)
    return redirect('/lesson/list')


@app.route("/lesson/delete")
def delete_lesson():
    lesson_id = request.args["id"]
    lesson.delete(int(lesson_id))
    return redirect("/lesson/list")


@app.route("/student/list")
def student_list():
    keyword=request.args.get("keyword")
    students = student.query(keyword)
    return render_template("student_list.html", data=students)

@app.route("/student/add")
def add_student():
    return render_template("add_student.html")

@app.route("/student/edit")
def edit_student():
    student_id = request.args.get("id")
    data = student.info(int(student_id))
    return render_template("edit_student.html", student=data)


@app.route("/student/save", methods=["POST"])
def save_student():   
    name = request.form["name"]
    class_name = request.form["class_name"]
    enroll_year = request.form["enroll_year"]
    mobile = request.form["mobile"]
    _student = {
        "name": name,
        "class_name":class_name,
        "enroll_year":enroll_year,
        "mobile":mobile
    }
    student.add(_student)
    return redirect("/student/list")

@app.route("/student/update", methods=["POST"])
def update_student():   
    id = request.form["id"]
    name = request.form["name"]
    class_name = request.form["class_name"]
    enroll_year = request.form["enroll_year"]
    mobile = request.form["mobile"]
    _student = {
        "id": int(id),
        "name": name,
        "class_name":class_name,
        "enroll_year":enroll_year,
        "mobile":mobile
    }
    student.update(_student)
    return redirect("/student/list")


if __name__ == '__main__':
    app.run(port=5000, debug=True, use_reloader=True)
