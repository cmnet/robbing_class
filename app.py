from flask import Flask,render_template,request,redirect
from bll import student
from bll import lesson
from bll import teacher

app = Flask(__name__)


@app.route('/')
def index():
    # lsn = {
    #     "name": "英语课",
    #     "teacher": "张老师",
    #     "student_number": "25",
    #     "start_time": "2020年3月24日",
    #     "address": "高升桥路9号918",
    #     "price": "¥258/2.5小时",
    #     "robbing_start_time": "2月29日00:00开抢",
    #     "robbing_end_time": "3月8日12:00截止",
    #     "brief": "课程难度:★★★★, 授课老师有13余年教学经验, 课堂高效, 趣味学习",
    #     "remark": "此课程较其他课程稍难, 建议有扎实基础的同学报名"
    # }
    # lesson.add(lsn)
    # t = {
    #     "name": "刘老师",
    #     "photo": "ㄟ( ▔ —— ▔ )ㄏ",
    #     "brief": "世界上最牛逼的老师"
    # }
    # teacher.add(t)
    # print("ok")
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




@app.route("/teacher/save",methods=["POST"])
def save_teacher():
    name = request.form["name"]
    brief = request.form["brief"]

    _teacher = {"name":name,"brief":brief}

    teacher.add(_teacher)


    return redirect("/teacher/list")
    # photo = requst.files[0]
    


@app.route("/teacher/update",methods=["POST"])
def update_teacher():
    id = request.form["id"]
    name = request.form["name"]
    brief = request.form["brief"]

    _teacher = {"name":name,"brief":brief, "id": int(id), "photo": ""}

    teacher.update(_teacher)


    return redirect("/teacher/list")

@app.route("/teacher/delete")
def delete_teacher():
    teacher_id = request.args["id"]
    teacher.delete(int(teacher_id))
    return redirect("/teacher/list")

# if __name__ == '__main__':
#     s={
#         "id":"1",
#         "name":"王五",
#         "mobile":"19982996666",
#         "enroll_year":"2019",
#         "class_name":"小猫编程"
#     }
#     student.update(s)

#     app.run()


if __name__ == '__main__':

    app.run(debug=True)


