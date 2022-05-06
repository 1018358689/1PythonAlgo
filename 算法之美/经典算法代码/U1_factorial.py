# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 23:19:22 2020
   求数的阶乘
@author: 刘瑜等
源代码文件：U1_factorial.py
"""
def factorial(x):
    m=1
    if x==0:
        return 1
    for i in range(1,x+1):
        m*=i
    return m
x=10
v=factorial(x)
print('%d的阶乘是%d'%(x,v))