from flask import Flask
from bll import student

app = Flask(__name__)


@app.route('/abc')
def index():
    return "hullo"


if __name__ == '__main__':
    s={
        "id":"1",
        "name":"王五",
        "mobile":"19982996666",
        "enroll_year":"2019",
        "class_name":"小猫编程"
    }
    student.update(s)

    app.run()
