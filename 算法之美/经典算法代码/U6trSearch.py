# -*- coding: utf-8 -*-
"""
  Created on Sun Sep  8 10:42:36 2019
  字符串暴力搜索算法
  @author: 刘瑜等
  源代码文件是：U6trSearch.py
"""
def StrSearch(arr,keys):
    i=0  
    m=len(keys)
    n=len(arr)
    count=0
    while i+m<=n :
        j=0
        while j<m: 
            if arr[i+j]!=keys[j]: 
                break
            j+=1
        if  j==m :
            count+=1
        i+=1
    return count  
s1='I am from China. I am a student.I live in Tianjin China.I love Python.Are you from China'
print(len(s1))
keys='China'
r=StrSearch(s1,keys)
print('在字符串里有%s %d个'%(keys,r))