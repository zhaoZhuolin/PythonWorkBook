# -*- coding: utf-8 -*-
# @Time    : 08/07/2021 12:00
# @Author  : ZZL


"""
数据类型和变量的基本使用
整型(int)、浮点(float)、字符串(str)，布尔值(bollean)，列表(list)、元组(tuple)、字典(dictionary)、集合(set)
"""
# 程序主入口
if __name__ == "__main__":

    #整型
    int_value = 666
    print(int_value)

    #浮点
    float_value = 666.66
    print(float_value)

    #字符串
    str_value = "hello young lady"
    print(str_value)

    #布尔值
    bool_value_true = True
    print(bool_value_true)
    bool_value_false = False
    print(bool_value_false)

    #空值
    none_value = None
    print(none_value)

    #列表
    list_value = ['2021', '0701', '100周年', '党的生日']
    print(list_value)

    #元组
    tup_value = ("Mac","Windows","1999")
    print(tup_value)

    #字典
    dic_value = {
        "name": "小明",
        "likes":"吃苹果"
    }
    print(dic_value)

    #集合
    basket_value = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print(basket_value)