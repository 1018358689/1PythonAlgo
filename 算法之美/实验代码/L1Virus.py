# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 18:44:30 2020
    求病毒扩散人数
@author: 刘瑜
代码文件U1Virus.py
"""
def Virus(d):
    n=0
    i=0
    for day in range(0,d,5): #间隔5天
        n+=3**i              #指数公式
        i+=1
    print(n)
Virus(31)
Virus(61)
