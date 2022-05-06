# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 08:43:13 2019

@author: 111
"""
def show1(i):
    return i**2
for i in range(10):
    r=show1(i)
    print('%d平方是%d'%(i,r))
    #print(i)
print('OK')