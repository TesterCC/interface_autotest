#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/5 22:17'

import time
import sys
from HTMLTestRunner import HTMLTestRunner
import unittest
from db_fixture import test_data

sys.path.append('./interface')
sys.path.append('./db_fixture')

# 指定测试用例为当前文件夹下的 interface 目录
test_dir = './interface'
# discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')   # 批量匹配执行用例
discover = unittest.defaultTestLoader.discover(test_dir, pattern='add_event_test.py')


if __name__ == "__main__":
    test_data.init_data()    # 初始化接口测试数据

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='Training Manage System Interface Test Report',
                            description='Implementation Example with: ')
    runner.run(discover)
    fp.close()