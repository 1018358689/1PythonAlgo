# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 22:39:34 2020
       K均值聚类算法
@author: 刘瑜
"""
import numpy as np
import matplotlib.pyplot as plt
SampleData=np.array([[4,18],[6,10],
                    [27,23],[30,41],[24,42]])
Centroids=np.array([[10,30],[20,20]]) #随意给定两个初始质心位置
#plt.scatter(SampleData[:,0],SampleData[:,1])
#plt.scatter(Centroids[:,0],Centroids[:,1],color='red',marker='p',linestyle='--',linewidth=5)

def Eu_Distance(one,one_C):  #欧几里得距离公式
    #k个测试质心与当前样本点位进行求距离，确定最小距离，该样本点就归某一个质心
    return np.sqrt(np.sum(np.power(one - one_C, 2))) #欧几里得距离公式求距离
def Kmean(data,Centroid,k):      #求K个聚类质心过程
    step=0 
    Go=True
    SData_len=len(data)          #获取样本个数
    record_dist=np.zeros([SData_len,2]) #记录每个样本属于哪个质心,并记录距离
    while Go or step<2:         #聚类迭代次数超过20次或最小质心不变时停止
        i=0
        while i<SData_len:       #每个样本数与k个质心求距离，并按照最近原则分类
            j=0                  #从第一个质心开始
            c_i=-1               #最小距离的位置 
            MinDist=np.inf       #inf为无穷大
            while j<k:          #一个质心一个质心地与每个样本进行距离比较
                One_dist=Eu_Distance(data[i],Centroid[j])
                if MinDist>One_dist:   #判断当前样本点距离哪个质心距离更短
                    MinDist=One_dist   
                    c_i=j              #记录距离更短的质心顺序号，该案例j=0,1
                j+=1
            record_dist[i]=c_i,MinDist #当前样本属于哪个质心，距离
            i+=1
        for m in range(k):       #比较完一次样本的距离更新一次质心坐标
            newDist=np.mean(data[record_dist[:,0]==m],axis = 0) #求m质点分类距离的均值
            Centroid[m]=newDist
            ss = np.abs(Centroid[m]-newDist) #前一步质心与当前步质心差的绝对值
            if np.sum(ss, axis=0) > 1e-4:    #当两个质心距离差小于0.0001时，认为质心相对稳定
                Centroid[m] = newDist
                Go = False                   #准备退出质心迭代过程
        step+=1                              #循环迭代次数控制在20次以内
    print('质心点迭代了%d次'%(step))
    return Centroid,record_dist              #返回最后质点和最后样本分类结果
length=len(SampleData)
End_C,End_dist=Kmean(SampleData,Centroids,len(Centroids))   #返回最后质点和样本分类
n=0
while n<length:
    if End_dist[n,0]==0:
        flag='o'
    else:
        flag='s'
    plt.scatter(SampleData[n,0],SampleData[n,1],marker=flag,linestyle='--',color='blue')
    n+=1
plt.scatter(End_C[:,0],End_C[:,1],color='green',marker='v',linestyle='--',linewidth=5)
plt.show()
print('                     (3)')
#print(End_dist)