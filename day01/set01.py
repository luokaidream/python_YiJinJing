# -*- coding:UTF-8 -*-
# Author: LuoKai
# date = 2021/1/5

"""
集合 set， python的集合与字典类似，也是用大括号{}表示，但是只能存储键值，不能存储value, 所以集合中的元素不能重复

"""

s1 = {'a', 1, 2}
print(type(s1))  # 输出 <class 'set'>
s2 = {'a', 'a', 'b', 'b', 'c'}
print(set(s2))  # 输出 {'b', 'a', 'c'} 去除重复元素

str1 = 'HelloWorld'
print(set(str1))  # 输出 {'o', 'l', 'W', 'r', 'd', 'H', 'e'} 此值为无序组合，输出结果可能不是这个

li1 = [1, 2, 3, 4]
print(set(li1))  # 输出{1, 2, 3, 4}

# 使用集合无重复元素的特点，我们合并列表，并去除重复元素只保留一个
l1 = ['H', 'om', 'c']
l2 = ['H', 'o', 'c', 'd']
print(list(set(l1 + l2)))  # 输出 ['d', 'o', 'H', 'om', 'c'] 重复的H只保留一个，set方法将列表变成集合，list方法再次转换为列表

# 集合也存在一些内置方法，如update pop等
# update方法更新集合
set1 = {'my', 'name', 'is'}
set1.update(['Groot'])  # 用列表是代表为一个元素，如果直接使用Groot将会被分成 g  r  o t
print(set1)  # 输出 {'is', 'name', 'my', 'Groot'}

# pop()方法随机删除集合中的一个元素
set2 = {'python', 'java', 'C++', 'PHP'}
set2.pop()  # 随机删除一个元素

# add()方法给集合添加元素
set2.add('Javascript')
print(set2)  # 输出 {'PHP', 'java', 'python', 'Javascript'}

# remove()删除结合中的指定元素
# set2.remove('python')
print(set2)  # 输出 {'Javascript', 'C++', 'java'}
# set2.remove('Ha') # 删除不存在元素 报错 KeyError: 'Ha' ， 提示KeyError 是不是类似字典了呢

# 集合也可以像其他数据类型一样， 使用for循环获取每个元素
for i in set2:
    print(i)

# 集合可以使用 | & - 做交集并集差集

s11 = {1, 2, 3, 4, 5, 6}
s12 = {5, 6, 7, 9}
s13 = {1, 2, 3}
print(s11 | s12)  # 输出 并集 {1, 2, 3, 4, 5, 6, 7, 9}
print(s11 & s12)  # 输出 交集 {5, 6}
print(s11 - s13)  # 输出 {4, 5, 6}
