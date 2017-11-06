import sys
sys.path.append('../db_fixture')
try:
    from mysql_db import DB
except ImportError:
    from .mysql_db import DB

# create data
datas = {
    # 培训会表数据
    'sign_event': [
        {'id': 1, 'name': '接口测试初级指导1', '`limit`': 30, 'status': 1, 'address': '会议室1', 'start_time': '2017-12-11 10:25:00', 'create_time': '2017-11-06 10:25:00'},
        {'id': 2, 'name': '接口测试初级指导2', '`limit`': 30, 'status': 1, 'address': '会议室2', 'start_time': '2017-12-12 10:25:00', 'create_time': '2017-11-06 10:25:00'},
        {'id': 3, 'name': '接口测试初级指导3', '`limit`': 30, 'status': 1, 'address': '会议室3', 'start_time': '2017-12-13 10:25:00', 'create_time': '2017-11-06 10:25:00'},
        {'id': 4, 'name': '接口测试初级指导4', '`limit`': 30, 'status': 1, 'address': '会议室4', 'start_time': '2017-12-14 10:25:00', 'create_time': '2017-11-06 10:25:00'},

    ],
    # 参与者表数据
    'sign_guest': [
        {'id': 1, 'realname': 'Lily1', 'phone': 13331833331, 'email': 'lily1@qq.com', 'sign': 0, 'event_id': 1, 'create_time': '2017-11-06 10:25:00'},
        {'id': 2, 'realname': 'Lily2', 'phone': 13331833332, 'email': 'lily2@qq.com', 'sign': 1, 'event_id': 2, 'create_time': '2017-11-06 10:25:00'},
        {'id': 3, 'realname': 'Lily3', 'phone': 13331833333, 'email': 'lily3@qq.com', 'sign': 1, 'event_id': 3, 'create_time': '2017-11-06 10:25:00'},
        {'id': 4, 'realname': 'Lily4', 'phone': 13331833334, 'email': 'lily4@qq.com', 'sign': 0, 'event_id': 4, 'create_time': '2017-11-06 10:25:00'},
        {'id': 5, 'realname': 'Lily5', 'phone': 13331833335, 'email': 'lily4@qq.com', 'sign': 0, 'event_id': 2, 'create_time': '2017-11-06 10:25:00'},
    ],
}


# Inster table datas   将测试数据插入测试表
def init_data():
    DB().init_data(datas)

if __name__ == '__main__':
    init_data()
