# -*- coding: utf-8 -*-
"""
  Created on Mon Feb 24 22:26:55 2020
  欧几里得公式算法
  @author: 刘瑜
  源代码文件是:L10gcd.py
"""
def gcd(a,b):    #用欧几里得递归求两个正整数的最大公约数，递归式
    if a%b==0:   #当余数为0时，找到最大公约数
        return b #返回最大公约数
    c=gcd(b,a%b)
    return c
        
print(gcd(50,20))
print(gcd(108,27))
print(gcd(100,13))

def GCD(a,b):          #非递归，循环式
    while True:
        if a==0:
            return b
        else:
            a,b=a%b,a
print(gcd(50,20))
print(gcd(20,50))