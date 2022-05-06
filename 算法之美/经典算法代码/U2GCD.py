# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 18:15:11 2019
求两个整数的最大公约数
@author: 刘瑜等
源代码文件：U2GCD.py
"""
def Divisor(x,y):                        #自定义求两个整数的最大公约数
    reduce=0
    if x<y :                             #确定小数
        reduce=x
    elif x>y :
        reduce=y
    else:                                #相等时直接返回其中一个数
        return x
    while reduce>=1 :                    #从小数开始作为除数，减一进行整除运算
        if x%reduce==0 and y%reduce==0 : #对x,y整除都没有余数，意味着都能整除
            return reduce                #返回数就是最大公倍数
        else:                            #x,y只要其中一个不能被整除，reduce就减一
            reduce-=1
try:             
    n1=int(input('输入第一个整数：'))     #=
    n2=int(input('输入第二个整数：'))
    if n1<=0 or n2<=0 :                  #这里把整数限制在1开始的自然数
        print('输出整数应该大于等于0')
    else:
        print('%d和%d的公约数是%d'%(n1,n2,Divisor(n1,n2))) #调用自定义函数求最大公约数
except:
    print('输出数出错！')                #输入出错时，报错