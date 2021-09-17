# -*- coding: utf-8 -*-
# @Time    : 09/15/2021 
# @Author  : ZZL

"""
ifelse的操作
"""

username = input('请输入账号')
password = input('请输入密码')

if username=="admin" and password =="123456":
    print("验证成功")
else:
    print("验证失败")