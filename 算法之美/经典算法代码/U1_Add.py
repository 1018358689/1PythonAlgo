# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 16:25:12 2019
累加器算法
@author: 刘瑜等
源代码文件：U1_Add.py
"""
import time 
def Add_N(n1):                 #自定义累加算法函数
    total=0
    for a in range(1,n1+1):
        total=total+a
    return total
N=10000
t1=time.process_time() 
print('1到%d自然数累加结果为%d'%(N,Add_N(N)))
t2=time.process_time()
print('循环累加算法用时：%.8f秒'%(t2-t1)) 
#=========================================累加算法算法二
t3=time.process_time()
print('采用累加公式计算1到%d累加和为%d'%(N,N*(N+1)/2))  #直接采用自然数累加和公式，只有一行代码
t4=time.process_time()
print('循环累加算法用时：%.12f秒'%(t4-t3)) 