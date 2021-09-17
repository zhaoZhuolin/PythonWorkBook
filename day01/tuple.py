# -*- coding: utf-8 -*-
# @Time    : 08/07/2021 12:00
# @Author  : ZZL

"""
元组的基础使用
"""
# 程序主入口
if __name__ == "__main__":

    #声明
    tup1 = ('Google', 'Runoob', 1997, 2000)
    tup2 = (1, 2, 3, 4, 5 )
    tup3 = "a", "b", "c", "d"   #  不需要括号也可以
    print(type(tup3))  # tuple
    
    # 遵循列表的len，按索引查找,修改
    for item  in tup1:
        print(item)

    fruits_list = ['apple', 'banana', 'orange']
    fruits_tuple = tuple(fruits_list)
    # print(fruits_tuple)
    # print(fruits_tuple[1])

