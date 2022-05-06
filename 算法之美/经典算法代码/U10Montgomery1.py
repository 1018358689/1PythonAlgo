# -*- coding: utf-8 -*-
"""
  Created on Wed Feb 26 19:44:46 2020
  蒙哥马利幂模运算递归算法
   @author: 刘瑜等
  源代码文件是：U10Montgomery1.py
"""
def Montgomery(a,b,c):         #a为幂数的底,b为指数,c为求模的右边数
    if b==1:                   #指数b=1时，返回递归值
        #print('余数%d，底数%d,指数%d'%(a%c,a,b))
        return a%c             #指数为1时，返回2%10=2
    r=Montgomery(a,b>>1,c)%c   #保持原状态，在存储空间，然后再计算b>>1递归调用
    if b%2==0:
        #print('余数%d，底数%d,指数%d'%((r*r)%c,a,b))
        return (r*r)%c
    else:
        #print('余数%d，底数%d,指数%d'%((a*(r*r))%c,a,b))
        return (a*(r*r))%c
if __name__ == "__main__":
    a=2                            #底数
    b=9                            #指数
    c=10                           #模右边数
    v=Montgomery(a,b,c)            #调用递归函数
    v=Montgomery(177699,3111,349950)            #调用递归函数
    print('最后求得的幂模数为%d'%(v))
