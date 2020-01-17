from flask import Flask
from bll import lesson
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
    return "Hello, world!"


if __name__ == '__main__':
    app.run()
