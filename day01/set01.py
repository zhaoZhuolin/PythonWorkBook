# -*- coding: utf-8 -*-
# @Time    : 09/15/2021 
# @Author  : ZZL

"""
集合基本使用
"""
def main():
    set1 = {1,2,3,4,5}
    print(set1)
    print(len(set1))

    set2 = set(range(1,10))
    print(set2)

    #remove元素不存在会引发错误
    if 8 in set2:
        set2.remove(8)
    print(set2)

    # 遍历
    for item in set2:
        print(item)


    set3 = set((1, 2, 3, 3, 2, 1))
    print(set3.pop())
    print(set3)
if __name__ == "__main__":
    main()