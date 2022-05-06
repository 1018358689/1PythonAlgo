# -*- coding: utf-8 -*-
"""
  Created on Sun Feb  9 20:19:39 2020
  朴素贝叶斯算法
  @author: 刘瑜
  源代码文件是：L11NBC.py
"""
import numpy as np
#Datas为训练集数据，含特征属性数据和分类数据
Datas=np.array([[1,1000,300,1,1],
                [2,800,3,4,0],
                [3,960,30,3,0],
                [4,1000,280,1,1],
                [5,1000,90,2,1],
                [6,1000,400,3,1],
                [7,1200,60,4,0],
                [8,1000,210,3,1],
                [9,800,200,4,0],
                [10,1000,70,4,0]])
Test=np.array([11,1000,1,500])  #测试数据

def NBC(trainData,labels,testData): #trainData传递特征属性值数据，labels分类数据，testData测试数据
    #求P(Ci)概率
    C={}    #存放不同分类的统计数量
    for label in labels:
        if C.get(label)!=None: 
            C[label]+=1
        else:
            C[label]=1
    print('分类情况：',C)
    Clen=len(labels)   #求出所有分类总数
    #求不同分类下的测试数据在训练集各自属性的发生概率
    Ptc={}    #存放不同分类下测试条件概率
    for k,c in C.items(): #获取分类名k和各自的统计数量c
        c=int(c)
        Atcount={}#存放测试数据在训练集的不同分类的属性里的出现数量
        for records in trainData: #一次返回一行训练记录
            if records[-1]==k:    #在同一分类值情况下
                i=0
                length=len(testData)
                while i<length:                  #比较每个属性值
                    if testData[i]==records[i]: #训练集属性值与测试集值比较
                        if Atcount.get(testData[i])!=None:
                            Atcount[testData[i]]+=1
                        else:
                            Atcount[testData[i]]=1
                    i+=1
        Pt=np.array(list(Atcount.values()))/c #求得分类ci下的各属性出现概率
        print('在分类',k,'情况下，各属性出现次数',Atcount)
        v=1
        for p in Pt:
            if p!=0:
                v*=p
        Ptc[k]=(c/Clen)*v               #存储每一种分类下的条件概率
        print(Ptc)
    return max(Ptc, key=Ptc.get)        #返回概率最大的类别
market=NBC(Datas,Datas[:,-1],Test)         
print('测试数据',Test,'的分类是',market)
'''
Test1=np.array(['B地区',65,'男','工人'])
market1=NBC(Datas,Datas[:,-1],Test1)         
print(Test1)
print('的分类是'+market1)                  
'''