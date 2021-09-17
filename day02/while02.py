# -*- coding: utf-8 -*-
# @Time    : 09/15/2021 
# @Author  : ZZL

"""
猜数字
"""
import random
answer = random.randint(1, 100)
countNum = 0
while True:
    countNum+=1
    inputVal = input("请输入值:")
    if inputVal>answer:
        print("太大了")
    elif inputVal<answer:
        print("太小了")
    else:
        print("恭喜你猜对了")
        break;
print("您共猜了"+countNum+"次")
print("您的智商明显余额不足")


        