# -*-coding:utf-8-*-
# @Time    :2023/10/2017:01
# @Author  :wsy
# @Email   :2960388548@qq.com
# @File    :denglu2.py
# @Software:PyCharm


from selenium import webdriver
from selenium.webdriver.common.by import By

from denglu import *


class addEvent():
    addbtu=(By.XPATH,"/html/body/div/div[1]/div[2]/button")
    addname=(By.XPATH,'//*[@id="id_name"]')
    address=(By.XPATH,'//*[@id="id_address"]')
    numbers=(By.XPATH,'//*[@id="id_limit"]')
    datetm=(By.XPATH,'//*[@id="id_start_time"]')
    submitbtu=(By.XPATH,'/html/body/div[1]/div[2]/form/div[7]/div/button')

class addcaozuo(ChuShiHua):
    def tj(self,tianjia):
        ele=self.driver.find_element(*addEvent.addbtu)
        ele.click()


