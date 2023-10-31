# -*-coding:utf-8-*-
# @Time    :2023/10/118:40
# @Author  :wsy
# @Email   :2960388548@qq.com
# @File    :test2.py
# @Software:PyCharm
'''
4个概念
1.测试固件（test fixture）  可以理解为测试以前或测试之后需要做的一些操作
unittest常用的测试固件有：setUp、tearDown、setUpClass、tearDownClass
setUp、tearDown  是在每个测试用例执行之前或者执行之后执行
setUpClass、tearDownClass  是在 类执行之前或之后执行

setUpClass 和 tearDownClass 整个class只执行一次
setUp 和 tearDown 每条用例执行一次


2.测试用例（test case） 通过unittest 通过提供的assert（断言方法：一个判断） 方法来验证一组特定的操作
或者输入以后得到的具体响应，unittest 提供了一个Testcase 类，用来创建测试用例
unittest 中测试用例中必须以test开头

3.测试套件（test suite）:一组测试用例   执行测试套件相当于执行了这一组用例

4.测试执行器（test runner） 用来执行测试用例，并返回测试结果
可以用图表、文字等方式  比如：HTMLTestRunner

'''




'''



import unittest


class TestDaotiandi(unittest.TestCase):
    @classmethod   #装饰器   装饰setUpClass和tearDownClass
    def setUpClass(cls) -> None:
        print("setupclass")
    def setUp(self) -> None:
        print("setup")
    def test_first(self):
        print("first")
        self.assertEqual("稻田地","稻田地")
    def test_second(self):
        print("second")
        self.assertEqual("稻田","稻田")
    def tearDown(self) -> None:
        print("teardown")
    @classmethod
    def tearDownClass(cls) -> None:
        print("teardownclass")


if __name__ == 'main':
    unittest.main()





import unittest   #daoruunittest


class TestDemo(unittest.TestCase):   #新建一个测试类，必须继承TestCase
    def setUp(self):        #测试固件的初始化
        print("setup")
    def test_002(self):   #所有测试用例必须以test开头，使用数字指定顺序
        self.assertEqual("稻田地","稻田地")   #判断第一个稻田地是否等于第二个稻田地
    def test_001(self):
        print("first")
        self.assertEqual("稻田地","稻田地")
    def tearDown(self) -> None:     #
        print("teardown")


if __name__ == '__main__':
    unittest.main()   #程序运行的入口

'''

import unittest


class TestDaotiandi(unittest.TestCase):
    a=4
    def setUp(self) -> None:
        print("setup")

    # @unittest.skip("莫须有")   #skip: 无条件跳过
    def test_first(self):
        print("first")
        self.assertEqual("稻田地","稻田地")

    # @unittest.skipIf(a>3,"莫须有")   #skipIf: 有条件跳过
    @unittest.skipUnless(a==5,"info")   #skipUnless: 不满足跳过
    def test_second(self):
        print("second")
        self.assertEqual("稻田","稻田")

    def tearDown(self) -> None:
        print("teardown")


if __name__ == 'main':
    unittest.main()

