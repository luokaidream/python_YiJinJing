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

# 列表元素可以修改
list3[1] = "Test"
print(list3)  # 输出  ['a', 'Test', 'i', 'o', 'u']

# 列表也有很多内置方法，如下
# append() 追加元素到列表
list4 = ['i', '1', 'am', '2', 'good']
list4.append('no')  # pycharm会有波浪线提示这样得做法不好，不如直接定义，这里只为表示append得用法， append没有返回值，直接使用即可
print(list4)  # 输出 ['i', '1', 'am', '2', 'good', 'no']

# remove() 删除列表中指定的元素
list4.remove('am')
print(list4)  # 输出 ['i', '1', '2', 'good', 'no']

# pop() 删除列表中最后的元素
list4.pop()
print(list4)  # 输出 ['i', '1', '2', 'good']

# insert() 在列表中插入元素
l3 = ['1', '3', '5', '9']
l3.insert(1, '2')  # 在位置1插入元素’2‘
print(l3)

# count() 统计列表中某个元素的数量
print(l3.count('3'))  # 输出 1， 元素'3'只出现一次

# reserve() 用于反转列表
l3.reverse()
print(l3)  # 输出 ['9', '5', '3', '2', '1']

# sort() 对列表进行排序
l5 = ['A', 'c', 'D', '4', 'E', '5']
l5.sort()  # 元素类型要一致
print(l5)  # 输出 ['4', '5', 'A', 'D', 'E', 'c']
l5.sort(reverse=True)  # 可以用reverse 指定是正序倒序
print(l5)  # 输出 ['c', 'E', 'D', 'A', '5', '4']
