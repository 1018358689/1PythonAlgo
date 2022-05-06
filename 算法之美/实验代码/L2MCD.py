# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 19:56:41 2020
      求最大公约数
@author: 刘瑜
源代码文件：L2MCD.py
"""
def MCD(x,y):
    if x>y:
        small=y
    else:
        small=x
    if x%small==0 and y%small==0:  #考虑x,y本身是倍数关系
        return small
    i=2
    small=small//2+1               #优化循环次数
    print('小数折半%d'%(small))
    maxCD=1
    while i<small:
        if x%i==0 and y%i==0:
            maxCD=i
        i+=1
    return maxCD
x=50
y=30
v=MCD(x,y)
print('%d和%d的最大公约数是%d'%(x,y,v))
