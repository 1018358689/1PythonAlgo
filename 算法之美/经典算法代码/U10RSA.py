# -*- coding: utf-8 -*-
"""
  Created on Thu Feb 27 18:19:50 2020
  RSA算法加密，解密
  @author: 刘瑜等
  源代码文件是：U10RSA.py
"""
from U10gcd1 import *       #调用自定义gcd1模块，要求跟本代码文件在一个路径下
from U10Montgomery1 import Montgomery #调用自定义Montgomery1模块

def Keys(p,q,e):         #计算n、e、d
    if gcd(p,q)==1:      #是互质的
        n=p*q
    else:
        print('p=%d,q=%d不是互质的，算法停止。'%(p,q))
        return 0,0,0
    fn=(p-1)*(q-1)       #通过欧拉公式求得n在1到n范围内得互质数量
    x,y,q=e_gcd(e,fn)    #欧几里得扩展算法求d=x
    if x<0:              #由于d要求是正整数
        x=(x+fn)%fn      #x=(x+fn)%fn    
    d=x
    return n,e,d
def encode(m,e,n):       #对明文m进行加密    
    c=Montgomery(m,e,n)  #调用蒙哥马利幂模运算
    return c             #返回密文c
def decode(c,d,n):           #对密文解密
    m=Montgomery(c,d,n)  #调用蒙哥马利幂模运算
    return m
if __name__ == "__main__":
    p,q,e=2333,150,3111
    n,e,d=Keys(p,q,e)     #求得公钥(n,e),私钥(d,e)   Keys(21,15,31)出错   
    print('n=%d,e=%d,d=%d'%(n,e,d))
    m=151                  #要发送的信息
    if n!=0 and e!=0 :
        c=encode(m,e,n)      #获取密文
        print('明文%d的密文是：\n%d'%(m,c))
        m1=decode(c,d,n)
        print('密文解密结果是：',m1)
