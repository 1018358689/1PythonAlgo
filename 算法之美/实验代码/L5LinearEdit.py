# -*- coding: utf-8 -*-
"""
  Created on Sat Aug 31 15:04:43 2019
  线性修改、删除、插入
  @author:刘瑜
  源代码文件是：L5LinearEdit.py
"""
def LinearEdit(arr,key,New):
    n=len(arr)
    i=0     #从左边开始依次找
    while i<n:
        if arr[i]==key:
            arr[i]=New   #修改找到的元素
            return i     #返回找到元素的下标
        i+=1
    return -1            #没有找到元素
def LinearInsert(arr,one):
    arr=sorted(arr)
    i=0
    n=len(arr)
    while i<n:
        if arr[i]>one:
            arr.insert(i,one)
            return arr
        i+=1
    arr.append(one)
    return arr

def LinearDel(arr,key):
    n=len(arr)
    i=0     #从左边开始依次找
    while i<n:
        if arr[i]==key:
            del(arr[i])  #删除找到的元素
            return -2     #返回找到元素的下标
        i+=1
    return -1            #没有找到元素
if __name__ == '__main__':
    D1=[9,10,3,2,0,8,7,11,15]
    key=8
    new=18
    print('待查找的元素列表',D1)
    r=LinearEdit(D1,key,new)
    one=5
    arr=LinearInsert(D1,one)
    D1=arr
    old=9
    r=LinearDel(D1,old)
    print('修改、排序、插入、删除后的元素列表',D1)


