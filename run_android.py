# -*-coding:utf-8-*-
# @Time    :2023/10/2311:04
# @Author  :wsy
# @Email   :2960388548@qq.com
# @File    :run_android.py
# @Software:PyCharm

from test2 import *
import unittest
from unittestreport import TestRunner

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestDaotiandi('test_second'))
    runner = TestRunner(suite)
    runner.run()
    runner.send_email(host="smtp.qq.com",
                      port=465,
                      user="2960388548@qq.com",
                      password="nkqdiaashqtkdece",
                      to_addrs="15326564721@163.com")
