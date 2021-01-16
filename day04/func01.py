# -*- coding:UTF-8 -*-
# Author: LuoKai
# date = 2021/1/14

from functools import reduce

"""
此篇介绍python的一些高阶函数，另外python函数也可以作为类似变量一样传递，所谓的函数式编程

"""


# 函数可以作为参数传递使用
def func01(a, b, c):  # 定义个返回三个数之和的函数
    return a + b + c


# 定义一个函数，其中一个参数为函数
def ext01(func, x, y, z):
    return func(x, y, z)


# 调用函数，并传入参数名，记住此处函数名不加(),如果加括号，就是调用函数了
print(ext01(func01, 2, 4, 6))  # 输出 三个数之和12

"""
下面记录下python内置的一些告诫函数，map()  filter()  reduce()
"""


# map(函数, 可迭代对象) map接收两个参数，第一个函数，第二个可迭代类型， 主要作用是将迭代得每个数据，传入参数得到得最终一个新的迭代数据

def f01(x):
    return x * 2


print(map(f01, [1, 2, 3, 4, 5, 6]))  # 输出 map对象 <map object at 0x0000016061BA9288>
print(list(map(f01, [1, 2, 3, 4, 5, 6])))  # 打印实际数据，许使用list()  [2, 4, 6, 8, 10, 12]


# reduce() 函数，再python3中被移除了，放在了functools模块中，如需使用先引入 from functools import reduce
# 此函数叶是两个参数，第一个参数是个函数，第二个是个序列，但是参数接收两个序列中的参数，计算出结果，在和序列后面的参数进行计算
# 如 reduce(f, [x1,x2,x3,x4])  ==  f(f(f(x1,x2),x3),x4), 利用这方方式我们可以计算两个数之和

def f02(x, y):
    return x + y


print(reduce(f02, range(10)))  # 输出 45 ，直接返回


# filter() 内建函数也是应用再序列，同时与map一样，接收一个函数，一个序列，用于把每个序列的元素应用于函数，如果返回Ture保留数据，False删除数据
# 在一个list中，删掉偶数，只保留奇数
def f03(x):
    return x % 2 == 1


print(filter(f03, [1, 2, 3, 4, 5, 6, 7]))  # 输出 <filter object at 0x00000270F8FD06C8>
print(list(filter(f03, [1, 2, 3, 4, 5, 6, 7])))  # 输出  [1, 3, 5, 7]

# sorted() 此内建函数用于排序，同时可以指定函数以某种方式进行排序
print([-1, 5, -10, 4, 1])  # 输出  [-1, 5, -10, 4, 1]
print(sorted([-1, 5, -10, 4, 1], key=abs))  # 指定一个key对应一个函数，是按照这个函数进行处理后排序，本例为绝对值
print(sorted([-1, 5, -10, 4, 1], key=abs, reverse=True))  # 执行reverse参数可以进行倒序
