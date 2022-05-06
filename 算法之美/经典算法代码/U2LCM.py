# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 21:13:10 2019
求两整数的最小公倍数
@author: 刘瑜等
源代码文件：U2LCM.py
"""
def T1(x,y):
    increat=0
    if x>y :
       increat=x
    elif x<y:
        increat=y
    else :
        return x
    while increat :
        if increat%x==0 and increat%y==0 :
            return increat
        else:
            increat+=1
try:             
    n1=int(input('输入第一个整数：'))     #=
    n2=int(input('输入第二个整数：'))
    if n1<=0 or n2<=0 :                  #这里把整数限制在1开始的自然数
        print('输出整数应该大于等于0')
    else:
        print('%d和%d的最小公倍数是%d'%(n1,n2,T1(n1,n2))) #调用自定义函数求最小公倍数
except:
    print('输出数出错！')       
