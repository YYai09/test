# -*-coding:utf-8-*-
# @Time    :2023/10/2016:23
# @Author  :wsy
# @Email   :2960388548@qq.com
# @File    :hanshu_csv.py
# @Software:PyCharm


import csv


def hanshu_csv(file):
    mylist=[]
    with open(file,"r",encoding="utf-8") as f:
        data=csv.reader(f)
        for i in data:
            mylist.append(i)
        del mylist[0]
        return mylist
if __name__ == '__main__':
    data = hanshu_csv(r"C:\Users\lenovo\Desktop\datas.csv")
    print(data)
