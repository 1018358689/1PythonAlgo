# -*- coding: utf-8 -*-
"""
  Created on Tue Sep  3 19:57:55 2019
  插值查找
  @author: 刘瑜等
  源代码文件是：U5ValueSearch.py
"""
def ValueSearch(arr,key):
    i=0
    left=0
    right=len(arr)-1
    while left<right:
        i+=1
        print('查找次数%d'%(i))
        mid=left+int((right-left)*(key-arr[left])/(arr[right]-arr[left]))
        if key<arr[mid]:
            right=mid-1
        elif key>arr[mid]:
            left=mid+1
        else:
            return mid     #返回查到元素的下标值
    return -1              #若没有找到，则返回-1
s1=[0,3,5,7,9,20,30,40,50]
key=50
print('查询列表为',s1)
print('查询值为',key)
r=ValueSearch(s1,key)
if r==-1:
    print('%d没有找到'%(key))
else:
    print('查找值%d在列表里的下标值为%d'%(key,r))
