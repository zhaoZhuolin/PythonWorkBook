# -*- coding: utf-8 -*-
# @Time    : 08/07/2021 12:00
# @Author  : ZZL


"""
字典的基本使用
- 获取
- 修改
- 删除
"""
# 程序主入口
def main():
    dict_val = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
    # 获取
    # for key, value in dict_val.items():
    #     print(key, value)
    # print(dict_val.keys())
    # print(dict_val.values())

    #修改
    # dict_val['Name'] = "ZZL"
    # dict_val.update(Name="zzl")
    # print(dict_val)
    
    
    #删除
    # del dict_val['Name'] # 删除键 'Name'
    # dict_val.clear()     # 清空字典
    # del dict_val         # 删除字典
    # print(dict_val)
if __name__ == "__main__":
   main()