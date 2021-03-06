# -*- coding: utf-8 -*-
"""
   Created on Wed Dec  4 07:44:54 2019
   构建数组
   @author: 刘瑜
   源代码文件是：U3BuildArray.py
"""
import numpy as np
A1=np.array([100,99,100])  #构建一维数组
print('A1所有的元素和为%d'%(A1.sum()))  #用sum()方法求所有元素的和
A2=np.array([[100,100,100],[60,60,60],[88,88,88]])  #构建二维数组
print('二维数组A2:')
print(A2)
print('A2在第二维（列）方向方向上，求所有元素的和为:',np.sum(A2,axis=0))  #在第二维方向上，用sum()方法求元素的和
print('A2在第一维（行）方向方向上，求所有元素的和为:',np.sum(A2,axis=1))  #在第一维方向上，用sum()方法求元素的和
A3=np.array([[[100,100,100],[60,60,60],[88,88,88]],[[50,50,50],[40,40,40],[30,30,30]]])  #构建三维数组
print('三维数组A3:')
print(A3)
print('A3在第三维方向上，求所有元素的和为:',np.sum(A3,axis=0))  #在第三维方向上（最外面），用sum()方法求元素的和
print('A3在第二维方向上，求所有元素的和为:',np.sum(A3,axis=1))  #在第二维向上（中间），用sum()方法求元素的和
print('A3在第一维方向上，求所有元素的和为:',np.sum(A3,axis=2))  #在第一维方向上（最里面），用sum()方法求元素的和