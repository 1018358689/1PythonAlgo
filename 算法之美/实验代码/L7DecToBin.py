# -*- coding: utf-8 -*-
"""
  Created on Fri Apr  3 21:51:23 2020
  十进制转二进制
  @author: 刘瑜
  源代码文件是：L7DecToBin.py

def DecToBin(n):
    if n==1:
        print(n,end='')
        return n
    else:
        DecToBin(n//2)
        print(n%2,end='')
n=12
print('%d转为二进制数是:'%(n))
DecToBin(n)
"""

def DecToBin(n,b):
    if n==1:
        #print(n,end='')
        return n
    else:
        DecToBin(n//2,b)
        b.append(n%2)
        #print(n%2,end='')
    return b
n=9
print('%d转为二进制数是:'%(n))
b=[1,]
B=DecToBin(n,b)
print(B)