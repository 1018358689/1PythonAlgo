# -*- coding: utf-8 -*-
"""
  Created on Thu Aug 22 17:18:13 2019
  冒泡排序
  @author: 刘瑜等
  源代码文件是：U4bubbleSort.py
"""
def bubbleSort(s1):
    n=len(s1)
    for i in range(n):
        for j in range(n-i-1):
            if s1[j]>s1[j+1]:
                c1=s1[j]
                s1[j]=s1[j+1]
                s1[j+1]=c1
l1=[9,0,6,5,3,10,36,2,1]
print('排序前的数列：',l1)
bubbleSort(l1)
print('排序后的数列：',l1)
                
