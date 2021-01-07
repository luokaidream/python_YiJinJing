# -*- coding:UTF-8 -*-
# Author: LuoKai
# date = 2021/1/6

"""
python 中也使用if else, While 等处理条件控制和循环控制
"""
"""
# if 条件控制
""""""
a = int(input("请输入数字："))
if a == 10:
    print("输入正确！！")
else:
    print("输入错误！！")

# 多条件控制 if elif else
age = int(input("请输入年龄: "))
if age < 18:
    print("我还是少年！")
elif 18 < age < 40:
    print("我还是青年！")
else:
    print("我是中年还是老年？")

# 多个if 条件，其实就是顺序执行代码, 执行到那个if条件为真时，将不在继续向下执行
language = input("请输入开发语言：")
if language == 'python':
    print("I am pythoner")
if language == 'java':  #
    print("I am javaer")

# if 语句中还可以有其他if 语句
age = int(input("年龄多大了？"))
sex = input("性别是：")
if age > 18:
    if sex == "male":
        print("原来是个少你那")
    else:
        print("啥啥啥")
"""
# while循环
"""
语句格式
while 条件:
    语句块

"""
n = 1
while n < 9:
    print(n)
    n = n + 1

# for循环
for i in 'HelloWorld':
    print(i)

for i in ['i', 'o', 'v', 'e']:
    print(i)

# break 跳出当前循环 , 下面例子就是当循环时，如果碰到元素等于指定元素'python',就跳出for循环，后续不再执行
l1 = ['java', 'python', 'php', 'c++']
for i in l1:
    if i == 'python':
        break
    print(i)
# 同样break 也可以使用在while循环中
a = 1
while a < 10:
    print(a)
    a = a + 1
    if a == 5:  # 当a = 5时将会跳出当前循环，不在执行后面内容
        break

# continue 用于跳过当前循环，执行下一次循环
for i in range(10):
    if i == 3:  # 判断如果i为3时，跳过当前循环
        continue
    print(i)

print("-----------------------分割线-----------------")
b = 1
while b < 10:
    if b == 4:
        b = b + 1
        continue
    else:
        print(b)
        b = b + 1
