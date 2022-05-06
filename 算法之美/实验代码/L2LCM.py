# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 20:36:26 2020
    求x,y的最小公倍数
@author: 刘瑜
源代码文件是：L2LCM.py
"""
def LCM(x,y):
    if x>y:
        small=y
    else:
        small=x
    i=1
    m=small
    while True:
       if m%y==0 and m%x==0:
           return m
       else:
           i+=1
           m=small*i
x,y=20,12
v=LCM(x,y)
print('%d和%d的最小公倍数是%d'%(x,y,v))