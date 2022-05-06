# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 15:24:59 2019
九九乘法表算法
@author: 刘瑜等
源代码文件：U1_nines.py
"""
for y in range(1,10):
    for x in range(1,y+1):
        print('%dX%d=%d'%(x,y,x*y),end=' ')  #end=' '公式之间为空格，不换行
    print('')                                #一行结束，默认print()换行
