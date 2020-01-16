from flask import Flask
from bll import student

app = Flask(__name__)


@app.route('/abc')
def index():
    return "hello,world!"


if __name__ == '__main__':
    s={
        "id":"1",
        "name":"李一一",
        "mobile":"19982996666",
        "enroll_year":"2020",
        "class_name":"编程班"
    }
    student.update(s)

    app.run()
