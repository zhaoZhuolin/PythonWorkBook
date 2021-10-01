# -*- coding: utf-8 -*-
# @Time    : 08/07/2021 12:00
# @Author  : ZZL

"""
字符串的基础使用
"""

# 程序主入口
if __name__ == "__main__":
    #定义字符串
    str_val = "你的名字"
    print(str_val)

    # 访问字符串
    print(str_val[2:])  #名字
    
    # 字符串utf-8编码
    # str_encode = str_val.encode('utf-8')
    # print(str_encode)

    # 字符串utf-8解码
    # str_decode = str_val.decode('utf-8')
    # print(str_decode)

    #字符串长度
    print(len(str_val))

    #格式化字符串format
    print("{0}正在看{1}".format('我',str_val))
    
    str = "hello,world!"
    print("字符串首字母大写",str.title())
    print("字符串大写",str.upper())
    print("字符串是不是大写",str.isupper())
    print("字符串是以hello开头",str.startswith('hello'))
    print("字符串是以hello结尾",str.endswith('hello'))





    