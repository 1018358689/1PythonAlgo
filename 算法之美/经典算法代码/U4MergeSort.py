# -*- coding: utf-8 -*-
"""
  Created on Fri Aug 30 14:57:11 2019
  @author: 刘瑜等
  源代码文件是：U4MergeSort.py
"""
def MergeSort(arr):   
    if len(arr) <= 1:              #当长度为1时，并归结束
        return arr
    mid=len(arr)//2                #对半方式并归
    left = MergeSort(arr[:mid])    #递归方法并归左边列表
    right = MergeSort(arr[mid:])   #递归方法并归右边列表
    return Merge(left, right)      #并归并返回结果
def Merge(left,right):             #对两部分数组进行并归
    r, l=0, 0
    temp=[]                        #临时列表记录归并过程
    lmax=len(left)
    rmax=len(right)
    while l<lmax and r<rmax:
        if left[l] <= right[r]:    #小于等于的
            temp.append(left[l])   #放左边
            l += 1
        else:
            temp.append(right[r])  #大于的放右边
            r += 1
    temp += list(left[l:])
    temp += list(right[r:])
    #print(temp)                   #输出并归结果
    return temp
s1=[1, 9, 10, 4, 50, 6, 7, 90, 21, 23, 45]
print('排序前列表',s1)
print('并归排序后列表',MergeSort(s1))