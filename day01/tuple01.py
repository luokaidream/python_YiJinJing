# -*- coding:UTF-8 -*-
# Author: LuoKai
# date = 2020/12/31

"""
元组 tuple，python中的一种 ”不可修改有序“ 的数据类型，使用小括号表示数据，数据间使用丢号间隔
"""

# 创建元组几种方式， 1 直接创建 2 使用tuple()
t1 = (1, 2, 3)
print(type(t1))  # 输出  <class 'tuple'>
t2 = tuple([1, 2, 4])
print(type(t2))  # 输出  <class 'tuple'>
# 如果元组只有一个元素，记得元素后加逗号，否则不会认为是元组
t = (1,)
print(type(t))  # 输出  <class 'tuple'>
tt = (1)
print(type(tt))  # 输出  <class 'int'>

# 元组有序，所以也可进行索引
t3 = ('A', 'B', 'C', 1, 3, 5)
print(t3[1])
print(t3[2:5])
print(t3[-3:-1])
print(t3[::2])

# 元组的数据不能修改
# t3[2] = "2"  # 报错 TypeError: 'tuple' object does not support item assignment
print(t3)

# -----------------------------------------------------------------------------

# 元组的方法，因为元组是不可变数据类型，所以没有类似列表的append sort 等方法
print(dir(t3))

#  'count', 'index'
# count()方法统计元素中某系元素出现的次数
