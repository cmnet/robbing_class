from flask import Flask, render_template, request, redirect
# from bll import student
from bll import lesson
from model import *
app = Flask(__name__)


@app.route('/')
def index():
    lsn = {
        "name": "数学课",
        "teacher": 2,
        "student_number": "25",
        "start_time": "2020年3月24日",
        "address": "高升桥路9号918",
        "price": "¥258/2.5小时",
        "robbing_start_time": "2月29日00:00开抢",
        "robbing_end_time": "3月8日12:00截止",
        "brief": "课程难度:★★★★, 授课老师有13余年教学经验, 课堂高效, 趣味学习",
        "remark": "此课程较其他课程稍难, 建议有扎实基础的同学报名"
    }
    # lesson.add(lsn)
    return "Hello, world!"


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


if __name__ == '__main__':
    app.run(port=5001, debug=True)
