# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 07:51:12 2019
分块查找
@author: 刘瑜等
源代码文件是：BlockSearch.py
"""
from U5LinearFind import LinearFind  
def BlockSearch(arr,key,index,n):  #arr为待查找的列表，key为要查找关键值，index为块内最大值索引数列，n为块长度
    #先通过块最大值找出块范围
    B_max=-1
    j=0        #最大值索引下标
    for i in index:
        j+=1
        if key<=i:
            B_max=i
            break
    if B_max==-1:
        return -1                 #在块范围内没有该关键字值，结束查找
    #确定所在块
    print('块内最大值为%d'%(B_max))
    r=LinearFind(arr[(j-1)*n:(j*n-1)],key)
    print('线性查找结果%d'%(r))
    if r==-1:
        return -1
    else:
        return (j-1)*n+r        #找到关键字值在列表里得下标
   
s1=[1,4,2,8,3,10,89,20,19,50,200,128,121,120,110]
index=[8,89,200]
key=2
r=BlockSearch(s1,key,index,5)
if r==-1:
    print('%d在列表里不存在'%(key))
else :
    print('%d在列表里的下标为%d'%(key,r))
