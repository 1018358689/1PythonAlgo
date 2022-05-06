# -*- coding: utf-8 -*-
"""
  Created on Fri Aug 23 17:18:49 2019
  插入排序
  @author: 刘瑜
  源代码文件是：L4InsertSort.py
"""
def InsertSort(arr):
    n=len(arr)
    if n==1:
        return 1
    for i in range(1,n):
        c1=arr[i]                   #获取当前未排序的值
        j=i
        while j>0 and c1>arr[j-1]:  #在前面排序里插入值
            arr[j]=arr[j-1]         #把小数往后移动1位
            j-=1
        arr[j]=c1
l2=[9,3,1,5,6]
print('排序前的列表值：',l2)
InsertSort(l2)
print('排序后的列表值：',l2)
