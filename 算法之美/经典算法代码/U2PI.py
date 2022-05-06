# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 14:49:17 2019
蒙特卡洛法求PI
@author: 刘瑜等
源代码文件：U2PI.py
"""
from random import random
n=100000
def xy_range(n):
    m=0
    for i in range(1,n+1):
        x=random()*2-1  #x的取值范围为[-1,1)
        y=random()*2-1  #y的取值范围为[-1,1)
        if x**2+y**2<1:
            m+=1
    return m
c1=xy_range(n)
print('总实验次数是%d,计算的圆周率是%f'%(n,4*c1/n))
            
    
    
