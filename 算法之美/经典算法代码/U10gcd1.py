# -*- coding: utf-8 -*-
"""
  Created on Mon Feb 24 22:26:55 2020
  欧几里得公式算法
  @author: 刘瑜等
  源代码文件是:U10gcd1.py
"""
def gcd(a,b):    #用欧几里得递归求两个正整数的最大公约数
    if a%b==0:   #当余数为0时，找到最大公约数
        return b #返回最大公约数
    c=gcd(b,a%b)
    return c
        
print(gcd(50,20))
print(gcd(108,27))
print(gcd(100,13))
def e_gcd(a, b):     
    if b == 0:             #余数为0，返回
        return 1, 0, a     #x=1,y=0,a为最后一次非零余数
    else:         
        x, y, q = e_gcd(b, a % b) #q为gcd(b, a%b)余数         
        x, y = y, (x-(a//b)*y) #
        return x, y, q
if __name__ == "__main__":
    x,y,q=e_gcd(50, 20)
    print('求解x=%d，y=%d,余数为=%d'%(x,y,q)) #满足贝祖等式ax+by=gcd(a,b)