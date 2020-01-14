from pony.orm import *

db = Database()
db_config = {
    "provider": "mysql",
    "host": "47.100.21.40",
    "user": "root",
    "passwd": "123456",
    "db": "robbing_class"
}

db.bind(**db_config)
# set_sql_debug(True)


class Teacher(db.Entity):
    """用户表"""
    _table_ = 'users'
    id = PrimaryKey(int, column='user_id', auto=True)  # id
    name = Required(str, 20, nullable=True)
    photo = Optional(str, 128)             # 用户头像
    brief = Optional(str, 256)                  # 简介

    # @property
    # def get_classes_nums(self):  # 获取班级数
    #     return count(c.id for c in self.classes if c.status > 1)

    def __str__(self):
        return "Users(id='%s')" % self.id

    def check_password(self, hash_pwd):
        if hash_pwd == self.password:
            return True
        return False


# False指数据库表存在的情况，True指表不存在的情况下会自动创建表结构
db.generate_mapping(create_tables=True)
