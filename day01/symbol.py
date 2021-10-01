# -*- coding: utf-8 -*-
# @Time    : 09/15/2021 
# @Author  : ZZL

"""
运算符
算术运算符：+ - * / // % **
赋值运算符：+= -= *= /=  %= //%
比较运算符：> < <= >= == != is is not
逻辑运算符：and or not 
三目云算符
"""

a=7
b=2
# print(a/b)
# print(a//b)
# print(a%b)

# #is和==的区别 
# import time
# time1 = time.gmtime()
# time2 = time.gmtime()
# print(time1)
# print(time2)
# print(time1 == time2)# 判断值是否相等
# print(time1 is time2) #is是去判断变量的内存空间地址

# age = int(input("请输入年龄:"))
# height = int(input("请输入身高:"))

# if 18< age < 30 and 175<= height <=190:
#     print("符号条件")
# else:
#     print("回家吃饭吧")

# print(False and True) #False
# print(False or True)#True

# if a>b:
#     max = a
# else:
#     max = b
# print(max)

# max = exp1 if contion else exp2
#三目表达式
print(a if a>b else b)