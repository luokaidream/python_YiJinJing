# -*- coding:UTF-8 -*-
# Author: LuoKai
# date = 2020/12/30

"""python中的列表 是一种有序的可变数据类型，它也可以进行切片,索引获取元素，加,乘， 也有多种方法"""

# 列表的创建有以下几种方式，列表中的元素可以是任何数据类型
# 直接用方括号表示
l1 = ['A', 1, 'B', '2']

# 使用list方法生成列表
l2 = list('hello')
print(l2)  # 输出 ['h', 'e', 'l', 'l', 'o']

# 列表的加 乘
list1 = ['A', 'C']
list2 = ['B', 'D', 'E']

print(list1 + list2)  # 输出新列表 ['A', 'C', 'B', 'D', 'E']
print(list1 * 2)  # 输出新列表 ['A', 'C', 'A', 'C']

# 列表索引,切片， 左闭右开区间， 可以进行负索引，可以加步长
list3 = ['a', 'e', 'i', 'o', 'u']
print(list3[1])  # 输出 e
print(list3[1:3])  # 输出列表 ['e', 'i']
print(list3[3:])  # 输出列表 ['o', 'u']
print(list3[-3:])  # 输出列表 ['i', 'o', 'u']
print(list3[-5::2])  # 输出列表 ['a', 'i', 'u']
