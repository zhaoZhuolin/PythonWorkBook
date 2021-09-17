# -*- coding: utf-8 -*-
# @Time    : 09/15/2021 
# @Author  : ZZL

"""
for输出图案
"""
num = int(input("请输入行数："))
for x in range(num):
    for _ in range(x+1):
        print("*",end="")
    print()
        
    