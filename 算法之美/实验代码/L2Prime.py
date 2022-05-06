# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 20:15:19 2020
    质因数分解
@author: 刘瑜
源代码文件:L2Prime.py
"""
def Prime(x):
    solution=[]                 #记录求解结果
    i=2
    m=x//2+1                    #数字折半，加1
    while i<m:
        if x%i==0:              #能除尽的是质因数
            solution.append(i)  #记录质因数
            x=x//i              #x里去掉记录的质因数
            i=2
        else:
            i+=1
    return solution
m=40
v=Prime(m)
if len(v)<1:
    print('%d不能分解：'%(m))
else:
    print('%d质因数分解为：'%(m))
    print(v)
