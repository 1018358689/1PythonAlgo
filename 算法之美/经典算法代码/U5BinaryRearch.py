# -*- coding: utf-8 -*-
"""
  Created on Tue Sep  3 10:40:22 2019
  二分法查找
  @author:刘瑜
  源代码文件是：U5BinaryRearch.py
"""
def BinaryRearch(arr,key):
    left=0           #左边界
    right=len(arr)   #有边界
    while left<=right:
        mid=(right-left)//2   #二分法中间位置
        if arr[left+mid]<key:      #key在右半范围
            left=left+mid+1
        elif arr[left+mid]>key:   #Key在左半范围
            right=left+mid-1
        else:
            return left+mid       #找到元素的下标值
    return -1                    #没有找到
if __name__ == '__main__':
    s1=[0,2,3,5,8,9,12,30,40,50,55]
    print('查找列表',s1)
    key=55
    r=BinaryRearch(s1,key)
    if r==-1:
        print('列表里没有%d元素'%(key))
    else:
        print('在列表里找到元素%d，其下标为%d'%(key,r))
