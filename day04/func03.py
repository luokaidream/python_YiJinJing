# -*- coding:UTF-8 -*-
# Author: LuoKai
# date = 2021/1/16

"""
了解闭包后，就引申出python强大的装饰器功能, 装饰器，就是对原有函数起到装饰功能的函数，装饰器函数一定是个闭包

为啥要做装饰器?
开发项目中，如果我们原本写好一个功能，但是突然需要加一些其他功能，如果我们修改原有功能成本就很好，可能所有调用函数的地方都需要修改，
装饰器就是很好解决这种问题
"""


# 举例，假如我们存在一个登录功能，但是登录前提示用户"安全事项"

# 定义装饰器，参数作为变量，前面讲过参数可以作为变量以及返回值
def check_login(func):
    def inner():
        print("请注意保护您的密码，确认周围是否有人...")
        func()

    return inner


# 登录功能
def login():
    print("登录成功")


# 怎样使用装饰器呢，python有语法糖 @ ，但是我们先使用普通的方式来看下这个过程

f = check_login(login)  # 调用check_login函数，并传入登录函数，此时返回值应该是inner内部函数 f = inner
# 函数名+（）括号，调用函数inner(),此时执行inner函数内容，先打印print 内容，再次执行func() ,func就是我们传入的login函数，此函数内部打印“登录成功”
f()


# 输出:
# 请注意保护您的密码，确认周围是否有人...
# 登录成功

# 但是上面的方式我们发现有个问题，就是其实我们没有调用原本的login，二是调用的check_login, 所以仍然达不到目的，方法就是使用语法糖@，仍然使用上面的例子
def check_login1(func):
    def inner():
        print("请注意保护您的密码，确认周围是否有人...")
        func()

    return inner


@check_login1  # 使用语法糖@ 当调用函数login1时，这里就相当于把login1传入check_login1
def login1():
    print("登录成功")


# 调用函数
login1()  # 与上面输出一致
