# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 08:21:59 2020

@author: 111
"""

# -*- coding:utf-8 -*-
# _author_ = xu_qn
# 全排列 分为两种：递归与非递归
 
 
# 递归方法
def recursion_permutation(list, first, last):
    if first >= last:  # 递归结束情况
        print(list)
    for i in range(first, last):  # first包含，last不包含
        list[i], list[first] = list[first], list[i]
        recursion_permutation(list, first+1, last)
        list[i], list[first] = list[first], list[i]  # 交换回来，还原成原来的序列放置重复交换
 
 
# 非递归：字典序法
def is_not_reverse(list):  # 判断是否为倒叙list
    for i in range(len(list)-1):
        if list[i] < list[i+1]:
            return True
    return False
 
def find_first_min(list):  # 从右到左是递增的 只需要找到最右大于pi的数
    for i in range(len(list)-1, 0, -1):
        if list[i] > list[0]:
            min_index = i
            break
    return min_index
def reverse_list(list,first,last):
    while first < last:
        if list[first] > list[last]:
            list[first], list[last] = list[last], list[first]
        first += 1
        last -= 1
 
def dictionary_permutation(list):
    while is_not_reverse(list):
        for i in range(len(list) - 2, -1, -1):
            if list[i] < list[i + 1]:  # 从左到右找到第一个左边小于右边的数pi 坐标i
                j = find_first_min(list[i:])  # 找到pi右边数字中比pi大的最小数下标
                list[i], list[j+i] = list[j+i], list[i]  # 交换pi,pj，pj在原list的坐标i+j
                reverse_list(list, i+1, len(list)-1)  # 将pi后的list倒转，变为升序
                print(list)
 
 
 
 
if __name__ == "__main__":
    list = [1, 2, 3, 4, 5]
    #recursion_permutation(list, 0, len(list))
    dictionary_permutation(list)
