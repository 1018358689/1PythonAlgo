# -*- coding: utf-8 -*-
"""
   Created on Tue Feb 18 21:27:05 2020
   归一化算法
   @author: 刘瑜等
   源代码文件是：U10Normalization.py
"""
import numpy as np
import matplotlib.pyplot as plt
Data=np.array([[0.2,0.9,29],
               [0.9,0.1,100],
               [0.5,0.5,30]])
#====================================Min-Max
def Min_Max(data):
    min=0
    max=1
    C=data[:,2]
    min=np.min(C)
    max=np.max(C)
    for one in data:
        one[2]=(one[2]-min)/(max-min)
    print('转化后的矩阵：\n',data)
    return data
#=====================================Z-Score
def ZScore(data):
    x_mean=np.mean(data[:,2])      #求C特征属性列均值
    length=len(data[:,2])
    vari=np.sqrt((np.sum((data[:,2]-x_mean)**2))/length)
    print('方差：\n',vari)
    data[:,2]=(data[:,2]-x_mean)/vari #返回Z-Score公式计算结果
    print('Z-Score标准化后的矩阵：\n',data)
    return data
#====================================Decimal Scaling
def DecimalS(data):
    C=np.abs(data[:,2])
    max=int(np.sort(C)[-1])     #获取绝对值最大的数
    k=len(str(max))             #k为绝对值最大数的位数
    print('绝对值最大的位数：\n',k)
    data[:,2]=data[:,2]/(10**k)  #小数标定公式求值
    print('小数标定标准化后的矩阵：\n',data)
    return data    

def ShowData(Data,ShowD1):
    length=len(Data)
    X=np.ones(Data.shape[0])
    plt.figure(1)
    plt.subplot(121)
    for i in range(length):             #绘制归一化前的散点图
        plt.scatter(X*(i+1),Data[:,i])
    plt.subplot(122)
    for i in range(length):             #绘制归一化后的散点图
        plt.scatter(X*(i+1),ShowD1[:,i])
    plt.show()
ShowData(Data,Min_Max(Data.copy()))          
ShowData(Data,ZScore(Data.copy())) 
ShowData(Data,DecimalS(Data.copy()))