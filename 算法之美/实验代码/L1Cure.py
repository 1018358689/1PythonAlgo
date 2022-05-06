# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 20:36:50 2020
    求治愈人数
@author: 刘瑜
"""
def Cure(d):
    m=1                     #第15第一个出院
    i=0
    for _ in range(20,d,5): #10天一循环
        i+=1
        dayOut=3**i
        if dayOut<1000:
            m=dayOut
        else:
            m+=1000*5   #改为每天出院人数
    print('%d天共出院人数%d'%(d,m))
Cure(31)
Cure(61)