# -*- coding: utf-8 -*-
# @Time    : 09/16/2021 
# @Author  : ZZL

"""
函数使用
"""

from random import randint

def roll(n):
    total=0
    for _ in range(n):
        total+=randint(1,6)
    return total    

def add(a=0,b=0,c=1):
    return a+b+c

# 摇筛子
# print(roll(3))
# #使用默认参数执行
# print(add())
# #传递参数执行
# print(add(1,2,3))


# 在参数名前面的*表示args是一个可变参数
def add(*args):
    total = 0
    for val in args:
        total +=val
    return total
print(add(12,12))
