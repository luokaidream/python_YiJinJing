# -*- coding:UTF-8 -*-
# Author: LuoKai
# date = 2021/1/7

"""
python 使用def 定义函数， 函数可以有返回值，可以没有返回值，函数可以传递参数, 函数调用使用 函数名 + ()
格式:
def 函数名():  # 函数名使用小写字母
    语句块
    return xxx
调用函数   函数名()
"""


# 定义函数，不带return返回值
def myfun():
    print("I am a Python function, name is " + myfun.__name__)


# 调用函数
myfun()  # 输出 I am a Python function, name is myfun
print(myfun())  # 输出 None


# 定义带返回值函数
def myfun01():
    return "HelloWorld!"


# 调用函数并接收返回值
a = myfun01()
print(a)  # 输出 HelloWorld!


# 定义带参数的函数,函数名后面括号输入参数名称
def sum01(x, y):
    return x + y


# 调用带参数函数时，需传递参数
print(sum01(10, 20))  # 输出 30
