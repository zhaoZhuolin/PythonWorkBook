# -*- coding: utf-8 -*-
# @Time    : 08/07/2021 12:00
# @Author  : ZZL


"""
字典的基本使用
"""
# 程序主入口
if __name__ == "__main__":
    dict_val = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

    #修改
    dict_val['Name'] = "ZZL"
    # print(dict_val)

    #删除
    # del dict_val['Name'] # 删除键 'Name'
    # dict_val.clear()     # 清空字典
    # del dict_val         # 删除字典

    # 获取
    for key, value in dict_val.items():
        print(key, value)