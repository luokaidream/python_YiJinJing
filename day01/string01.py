# -*- coding:UTF-8 -*-
# Author: LuoKai
# date = 2020/12/26

# 字符串的表示方式，以及用法

# 单引号方式
str1 = 'I am a string type'

# 双引号方式, 注意双引号里可以有单引号，双引号中的单引号并当成正常的字符串
str2 = "Today is a good day, I 'm LiLei"

# 三引号方式，三引号多用于文字较多的字符串
"""
i am line 1
i am line 2
i am line 3
"""

# 字符串，是不可变数据类型，拥有切片功能，且有很多方法

# 切片

s1 = 'Hello, World!'
# 切片获取元素，字符串的1到3的元素，记得切片是左闭右开区间获取
a = s1[1:3]
print(a)  # 输出:  e1

# 如果不指定开始位置，默认从0开始
print(s1[:5])  # 输出 Hello

# 切换还可负数索引，当字符串较长时，只想截取后面部分，如下
print(s1[-3:])  # 输出ld! ,从后面切片从-1开始，而不是0了

# 切片还可以使用调整步长，比如跳过一个的方式
s2 = "1234567890"  # 取出 13579，就可以使用步长为2的方式
print(s2[::2])  # 输出13579

# 字符串可以正常相加相乘
print(s1 + s2)  # 输出  Hello, World!1234567890
print(s1 * 3)  # 输出  Hello, World!Hello, World!Hello, World!

# 字符串属于不可变类型，所以不能给某个元素赋值
# s1[3] = 'tttt'
# TypeError: 'str' object does not support item assignment


# ------------------------------------------------------------------------
# 字符串存在很多内置方法可以使用，下面写几个常用的方法
s3 = "How are you ?"

# index() 方法用于查询字符串中某元素的位置(可以指定起始位置),并返回此位置
print(s3.index('How'))
# print(s3.index("www"))  # 如果不在字符串中，将报错 ValueError: substring not found

# find()方法也可以用于查询元素，查找到返回最左端的索引，查找不到返回-1，这就是与index的区别
print(s3.find('are'))  # 返回 位置4
print(s3.find('love'))  # 返回 -1

# join  split  strip isupper  islowwer  replace  startwith endw

# join()方法用于将序列中的元素连接起来
print('/'.join(['usr', 'bin', 'sh']))  # 输出 usr/bin/sh

# split()方法与join对应，将字符串分割成序列
print("usr/bin/sh".split('/'))  # 输出  ['usr', 'bin', 'sh']
