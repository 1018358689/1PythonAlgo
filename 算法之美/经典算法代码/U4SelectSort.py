# -*- coding: utf-8 -*-
"""
  Created on Fri Aug 23 16:01:31 2019
  选择排序
  @author: 刘瑜等
  源代码文件是：U4SelectSort.py
"""
def SelectSort(arr):
    n=len(arr)
    if n==1:
        return 1
    for i in range(n):
        mid=i                           #获得每次循环第一个比较值得下标
        for j in range(i,n-1):           #每次循环里寻找最小值
            if arr[mid]>arr[j+1]:       #循环过程判断最小值
                mid=j+1                 #获取更小值得下标
        arr[i],arr[mid]=arr[mid],arr[i]  #把最小的放到最前
s1=[3,18,0,32,2,1]
print('排序前的列表值：',s1)
SelectSort(s1)
print('排序后的列表值：',s1)