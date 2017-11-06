#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/6 14:52'


import unittest
import requests
import os
import sys

from db_fixture import test_data

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


# add_event_test finished
# 待调试 add_guest_test， get_event_list_test， get_guest_list_test ，user_sign_test
class AddEventTest(unittest.TestCase):
    """
    添加培训会
    """

    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/add_event/"

    def tearDown(self):
        print(self.result)

    def test_add_event_all_null(self):
        """
        所有参数为空
        """
        payload = {'eid': '', '': '', 'limit': '', 'address': "", 'start_time': '', 'create_time': ''}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], 'parameter error')

    def test_add_event_eid_exist(self):
        """
        id已经存在   eid 1
        """
        payload = {'eid': 1, 'name': '一加4发布会', 'limit': 2000, 'address': "深圳宝体", 'start_time': '2017', 'create_time': '2017-11-06 10:25:00'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'event id already exists')

    def test_add_event_name_exist(self):
        """
        名称已经存在
        """
        payload = {'eid': 12, 'name': '接口测试初级指导1', 'limit': 2000, 'address': "会议室3", 'start_time': '2017', 'create_time': '2017-11-06 10:25:00'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10023)
        self.assertEqual(self.result['message'], 'event name already exists')

    def test_add_event_data_type_error(self):
        """
        日期格式错误
        """
        payload = {'eid': 11, 'name': 'Requests常用API讲解', 'limit': 200, 'address': "会议室2", 'start_time': '2017'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10024)
        self.assertIn('start_time format error.', self.result['message'])

    def test_add_event_success(self):
        """
        添加成功
        """
        payload = {'eid': 11, 'name': 'Requests常用API讲解', 'limit': 200, 'address': "会议室2", 'start_time': '2017-11-10 12:00:00'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'add event success')


if __name__ == '__main__':
    test_data.init_data()   # 初始化接口测试数据（test_data中的datas）
    unittest.main()


