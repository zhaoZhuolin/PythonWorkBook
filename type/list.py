# -*- coding: utf-8 -*-
# @Time    : 08/07/2021 12:00
# @Author  : ZZL

"""
列表的基础使用
"""
# 程序主入口
if __name__ == "__main__":
    #定义列表
    list_val = ['a','b','c']
    print(list_val)

    #len()输出列表长度
    print(len(list_val))

    # 按照索引访问
    print(list_val[0])

    #追加元素
    list_val.append("D")

    #插入元素到指定位置
    list_val.insert( 0,"ZZZ")
    print(list_val)

    #删除末尾的一个元素
    list_val.pop()
    print(list_val)

    #删除指定位置的一个元素
    list_val.pop(0)
    print(list_val)

    # 根据索引更新某个元素
    list_val[1] = "ZZL"
    print(list_val)