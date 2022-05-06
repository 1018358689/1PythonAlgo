# -*- coding: utf-8 -*-
"""
  Created on Fri Apr  3 20:31:39 2020
  @author: 刘瑜
  源代码文件是：L7Fibonacci.py
"""
def Fibonacci(n):
    F=[0,1]
    i=0
    while i<n-1:
        F.append(F[i]+F[i+1])  #前两个数和求得当前数
        i+=1
    return F[1:]
n=10
print('求%d的斐波那契数列',n)
print(Fibonacci(n))