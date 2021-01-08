# -*- coding:UTF-8 -*-
# Author: LuoKai
# date = 2021/1/7

"""
python函数的参数主要分为几类
    必选参数
    默认参数
    可变参数
    关键字参数
"""


# 必选参数, 即调用方法时必须输入同样数量的参数
def add(x, y):
    print(x + y)


add(2, 7)  # 输出 9


# add(2)  # 只传一个报错 TypeError: add() missing 1 required positional argument: 'y'
# add(2, 4, 5) # 传多一个报错 TypeError: add() takes 2 positional arguments but 3 were given
# add()  # 一个也不传报错 TypeError: add() missing 2 required positional arguments: 'x' and 'y'


# 默认参数，指定义函数时某些参数设定一些默认值，如果传入此参数值使用传入值，不传入使用默认值
def plus2(x, y=2):  # 定义函数，默认返回x的2倍
    print(x * y)


plus2(5)  # 输出 10
# 如果想变成3倍呢，那就传入y的值
plus2(5, 3)  # 输出 15


# 可变参数，使用一个*表示，用于需要传入多个参数，但是挨个定义比较繁琐,传入的参数为元组形式
def func(*numbers):  # 定义可变参数 *numbers
    print(numbers)  # 传入的numbers为元组形式 （1，2，3，4，5）


# 调用函数，传入多个数据
func(1, 2, 3, 4, 5)  # 输出 (1, 2, 3, 4, 5)
func(['a', 'b', 'c'])  # 输出 (['a', 'b', 'c'],)  只有一个元素为列表的元组


# 关键字参数，使用二个**表示，用于传入不定长的键值对给函数
def func01(**kwargs):  # **kwargs 定义关键字参数，传入键值对
    print(kwargs)  # kwargs得到的是一个字典


func01(name='lk', age=18)  # 输出 {'name': 'lk', 'age': 18}


# 上面我们发现当传入可变参数和关键字参数时需要一个一个传递，如果较多会很麻烦，所以我们调用函数传入参数也可以使用*或者**
# 可变参数
def func03(*args):
    print(args)


list2 = ['HA', 'Hei', 'HAI', 'NO']
# 对比一下两个结果
func03(list2)  # 输出(['HA', 'Hei', 'HAI', 'NO'],) 列表中的元素仍然被当成一个元素传递，组织一个元素的元组
func03(*list2)  # 输出('HA', 'Hei', 'HAI', 'NO')  列表中的元素分别传递，形成一个4个元素的元组


# 关键字参数
def func04(**kwargs):
    print(kwargs)


func04(name='AAA', age=18, city='DaZhouCheng')  # 这样传入很麻烦，如果参数很多将写很多
dict1 = {'name': 'AAA', 'age': 18, 'city': 'DaZhouCheng'}  # 先定义个字典，之后使用**传入就很简单
func04(**dict1)  # 输出 {'name': 'AAA', 'age': 18, 'city': 'DaZhouCheng'}

"""
    前面记录了4中参数的定义和传入方式，如果有组合呢，如有必选参数，有默认参数，可变参数，关键字参数呢？？
    注意一下内容:
    1： 定义函数的参数前后顺序  必选>>默认>>可变>>关键字 
    2: 调用函数也是这个顺序
"""


def func05(name, age, city='DaZhouCheng', *args, **kwargs):
    print('my name is %s, and my age is %d, i live in %s' % (name, age, city))
    print("可变参数:", args)
    print("关键字参数", kwargs)


func05('ZhouYuan', 18, 'HunDunTian', '**args', i='love')
# 输出，根据参数位置一一对应
# my name is ZhouYuan, and my age is 18, i live in HunDunTian
# 可变参数: ('**args',)
# 关键字参数 {'i': 'love'}
