# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 14:43:57 2019
    求空间任意三点连接而成的面积
@author: 刘瑜
源代码文件：U2Area.py
"""
import numpy as np
A=np.array([1,1,1])
B=np.array([3,1.5,1.5])
C=np.array([4,2,2])
Dab=np.sqrt(np.sum((A-B)**2))             
Dac=np.sqrt(np.sum((A-C)**2))              
Dbc=np.sqrt(np.sum((B-C)**2))              
print('AB的长度为',Dab)
print('AC的长度为',Dac)
print('BC的长度为',Dbc)
s=(Dab+Dac+Dbc)/2
area =np.sqrt(s*(s-Dab)*(s-Dac)*(s-Dbc))
print('该任意三角形的面积为%.2f平方米'%(area))
