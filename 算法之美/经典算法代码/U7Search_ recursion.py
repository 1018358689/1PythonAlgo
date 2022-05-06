# -*- coding: utf-8 -*-
"""
  Created on Sun Dec 15 14:34:46 2019
  递归方式二分法查找值
  @author: 刘瑜
  源代码文件是：U7Search_ recursion.py
"""
def bin_search(value,line,start=0,end=0):
    mid =(end-start)//2 + start
    if start > end:     #开始下标大于结束下标，没有找到值
        return None     #返回空
    elif line[mid] > value : #中间值大于查找值，搜索左边的列表区间
        return bin_search(value,line,start,mid-1)
    elif line[mid] < value:  #中间值小于查找值，搜索右边的列表区间
        return bin_search(value,line,mid+1,end)
    elif line[mid] == value: #找到值，返回对应的下标值
        return mid
L=[0,2,3,5,6,8,9,10,21,52,82,100]  #必须有序
max1=len(L)
result=bin_search(10,L,0,max1-1)
print('查找结果为：',result)