# -*- coding:UTF-8 -*-
# Author: LuoKai
# date = 2020/12/31


"""
字典 python中一种以键值对存储的数据 key:value形式，字典使用大括号{}表示，定义字典的key时不可使用可变数据类型
"""

# 定义字典，直接使用大括号，不同键值对使用逗号间隔
d1 = {'a': 1, 'b': 2}  # 注意key的值一定是不可变数据类型， 准确的说是列表、字典这种不可哈希（unhashable）的类型不可当做键值，可哈希的类型才可当作键
print(type(d1))  # 输出 <class 'dict'>
d2 = dict(a=1, b=2, c=3)
print(d2)  # 输出 {'a': 1, 'b': 2, 'c': 3}
print(type(d2))  # 输出 <class 'dict'>

l1 = [('a', 1), ('b', 2)]
print(dict(l1))  # 输出 {'a': 1, 'b': 2}

# 获取字典数据,可以直接用索引键名称得方式
d3 = {'name': 'lk', 'age': 18, 'city': 'ShenZhen'}
print(d3['name'])  # 输出 lk
# 修改字典的value,可以索引后直接修改
d3['age'] = 20
print(d3)  # 输出 {'name': 'lk', 'age': 20, 'city': 'ShenZhen'}

# -------------------------------------------------------------
# 字典同样存在很多内置方法
# 更新字典，使用update()方法
d4 = {'sex': 'male', 'height': '170CM'}
print(d3.update(d4))  # 输出 update方法无返回值，所以这个输出 None
print(d3)  # 输出 {'name': 'lk', 'age': 20, 'city': 'ShenZhen', 'sex': 'male', 'height': '170CM'}

# pop() 方法，使用key删除字典中指定的键值对
d4.pop('sex')
print(d4)  # 输出 {'height': '170CM'}

# clear()方法，清空字典所有键值对
d5 = {'name': 'lk', 'age': 20, 'city': 'ShenZhen', 'sex': 'male', 'height': '170CM'}
d5.clear()
print(d5)  # 输出 {}  空字典

# 获取字典的所有key，可以用keys方法
d6 = {'a': [1, 2, 3], 'b': ['a', 'b', 'c'], 'c': 'Time'}
print(d6.keys())  # 输出 dict_keys(['a', 'b', 'c'])

# 使用for循环获取每个key
for i in d6.keys():
    print(i)
# 输出
# a
# b
# c

# 既然上面可以获取key，那就可以获取value, 使用values()方法，将字典的值组成元组放入列表
print(d6.values())  # 输出 dict_values([[1, 2, 3], ['a', 'b', 'c'], 'Time'])
for v in d6.values():
    print(v)
# 分别以下输出
# [1, 2, 3]
# ['a', 'b', 'c']
# Time

# 上面分别输出key 和value，使用items() 可以分别输出key 和 value组成元组放入列表中
print(d6.items())  # 输出  dict_items([('a', [1, 2, 3]), ('b', ['a', 'b', 'c']), ('c', 'Time')])
for i, v in d6.items():
    print(i, "--->", v)
# 分别输出以下内容
# a ---> [1, 2, 3]
# b ---> ['a', 'b', 'c']
# c ---> Time

# fromkeys() 方法是以序列中的元素作为键值，生成新的字典
d7 = {}
d7 = d7.fromkeys(('a', 'b', 'c'))
print(d7)  # 输出 {'a': None, 'b': None, 'c': None}  记得给新生成的字典赋值
