# -*- coding: utf-8 -*-
"""
  Created on Tue Feb 18 10:49:28 2020
  网页排名算法
  @author: 刘瑜等
  源代码文件是：U10PageRank.py
"""
# -*- coding: utf-8 -*-
import numpy as np
M= np.array([[0, 1, 1, 0],
             [1, 0, 0, 0],
             [0, 1, 0, 1],
             [1,0 , 0, 0]], dtype=float)  # dtype指定为float

def MoveMatrix(m):     #建立转移矩阵
    num=m.sum(axis=0)  #统计每列1的总数，也就是每个网页的出链数
    return m/num       #返回建立的移动矩阵

def V(c):  # pr值得初始化
    pr =np.ones((c.shape[0], 1), dtype=float)/len(c)  # 初始化pr值矩阵
    return pr

def PR(p, m, v):  # 迭代计算pageRank值
    i=0           #统计迭代次数
    while True:  
        v1 = p*np.dot(m, v) + (1 - p) * v  #Pr值计算公式
        if np.abs((v-v1).all())<0.001 :# 判断pr矩阵是否收敛,小于给定的e=0.001
            break         #收敛，则跳出循环
        else:
            v=v1          #不收敛，则继续迭代
        i+=1
        if i==20 : break  #控制迭代次数，可以减少重复计算次数
    print('求pr值迭代了%d次'%(i))
    return v

M0=MoveMatrix(M)
print('初始转移矩：\n',M0)
V0=V(M0) #求得初始pr值
a= 0.85  #阻尼系数，经验值，采用0.85
print('最后迭代格网页pr值结果：\n',PR(a,M0,V0))  # 计算pr值
