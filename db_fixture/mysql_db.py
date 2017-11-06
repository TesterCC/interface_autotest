#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/6 11:42'

from pymysql import connect, cursors
from pymysql.err import OperationalError
import os
import configparser as cparser


# 读取db_config.ini文件设置
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + "/db_config.ini"

cf = cparser.ConfigParser()
cf.read(file_path)

host = cf.get("mysqlconf", "host")    # db_config.ini [mysqlconf]
port = cf.get("mysqlconf", "port")
db = cf.get("mysqlconf", "db_name")
user = cf.get("mysqlconf", "user")
password = cf.get("mysqlconf", "password")


# 封装MySQL基本操作
class DB(object):
    def __init__(self):
        try:
            # 连接数据库
            self.conn = connect(host=host,
                                user=user,
                                password=password,
                                db=db,
                                charset='utf8mb4',
                                cursorclass=cursors.DictCursor)
        except OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    # 清楚表数据
    def clear(self, table_name):
        # real_sql = "truncate table " + table_name + ";"
        real_sql = "delete from " + table_name + ";"
        with self.conn.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.conn.commit()     # 提交SQL语句

    # 插入表数据
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        # print(real_sql)   # for Debug

        with self.conn.cursor() as cursor:
            cursor.execute(real_sql)
        self.conn.commit()

    # 关闭数据库连接
    def close(self):
        self.conn.close()

    # init data   初始化test data
    def init_data(self, datas):
        for table, data in datas.items():
            self.clear(table)     # 清理表
            for d in data:
                self.insert(table, d)
        self.close()


if __name__ == '__main__':
    db = DB()
    table_name = "sign_event"
    data = {'id': 11,
            'name': '接口测试初级指导',
            '`limit`': 30,          # limit不做特别处理插入mysql会报错
            'status': 1,
            'address': '会议室4',
            'start_time': '2017-12-10 10:25:00',
            'create_time': '2017-11-06 10:25:00'}     # create_time没有default值，所以要添加

    table_name2 = "sign_guest"
    data2 = {'realname': 'jack',
             'phone': 13800110011,
             'email': 'jack@mail.com',
             'sign': 0,
             'event_id': 11,
             'create_time': '2017-11-06 10:25:00'}

    db.clear(table_name)
    db.insert(table_name, data)
    db.clear(table_name2)
    db.insert(table_name2, data2)

    db.close()


