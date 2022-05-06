# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 21:41:04 2020

@author: 111
"""
dataSet = np.mat([[ 0.90796996 ,5.05836784]
                    ,[-2.88425582 , 0.01687006]
                    ,[-3.3447423 , -1.01730512]
                    ,[-0.32810867 , 0.48063528]
                    ,[ 1.90508653 , 3.530091  ]
                    ,[-3.00984169 , 2.66771831]
                    ,[-3.38237045 ,-2.9473363 ]
                    ,[ 2.22463036 ,-1.37361589]
                    ,[ 2.54391447 , 3.21299611]
                    ,[-2.46154315 , 2.78737555]
                    ,[-3.38237045 ,-2.9473363 ]
                    ,[ 2.8692781  ,-2.54779119]
                    ,[ 2.6265299  , 3.10868015]
                    ,[-2.46154315 , 2.78737555]
                    ,[-3.38237045 ,-2.9473363 ]
                    ,[ 2.80293085 ,-2.7315146 ]])
import numpy as np

def distEclud(vecA, vecB):  #定义一个欧式距离的函数  
    return np.sqrt(np.sum(np.power(vecA - vecB, 2)))

def randCent(dataSet, k):  #第一个中心点初始化
    n = np.shape(dataSet)[1]
    centroids = np.mat(np.zeros([k, n]))  #创建 k 行 n列的全为0 的矩阵
    for j in range(n):
        minj = np.min(dataSet[:,j]) #获得第j 列的最小值
        rangej = float(np.max(dataSet[:,j]) - minj)     #得到最大值与最小值之间的范围
        #获得输出为 K 行 1 列的数据，并且使其在数据集范围内
        centroids[:,j] = np.mat(minj + rangej * np.random.rand(k, 1))   
    return centroids

#参数： dataSet 样本点， K 簇的个数
#disMeans 距离， 默认使用欧式距离， createCent 初始中心点的选取
def KMeans(dataSet, k, distMeans= distEclud, createCent= randCent):
    m = np.shape(dataSet)[0]    #得到行数，即为样本数
    clusterAssement = np.mat(np.zeros([m,2]))   #创建 m 行 2 列的矩阵
    centroids = createCent(dataSet, k)      #初始化 k 个中心点
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = np.inf   #初始设置值为无穷大
            minIndex = -1
            for j in range(k):
                #  j循环，先计算 k个中心点到1 个样本的距离，在进行i循环，计算得到k个中心点到全部样本点的距离
                distJ = distMeans(centroids[j,:], dataSet[i,:])
                if distJ <  minDist:
                    minDist = distJ #更新 最小的距离
                    minIndex = j 
            if clusterAssement[i,0] != minIndex:    #如果中心点不变化的时候， 则终止循环
                clusterChanged = True 
            clusterAssement[i,:] = minIndex, minDist**2 #将 index，k值中心点 和  最小距离存入到数组中
        print(centroids)
        #更换中心点的位置
        for cent in range(k):
            ptsInClust = dataSet[np.nonzero(clusterAssement[:,0].A == cent)[0]] #分别找到属于k类的数据
            centroids[cent,:] = np.mean(ptsInClust, axis = 0)   #得到更新后的中心点
    return centroids, clusterAssement 

center, cluster = KMeans(dataSet, 2)
print('最后质心----')
print(center)