from flask import Flask, render_template, request, redirect
from bll import student
from bll import lesson
app = Flask(__name__)


@app.route('/')
def index():
    return "hello, world"


@app.route("/student/list")
def student_list():
    students = student.query()
    return render_template("student_list.html", data=students)


if __name__ == '__main__':
    app.run()
