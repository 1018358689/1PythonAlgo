# -*- coding: utf-8 -*-
"""
   Created on Wed Apr  8 20:58:26 2020
   K最临近算法KNN 
   @author:刘瑜
   源代码文件是：U11KNN.py
"""
import numpy as np
trainData=np.array([[23,8],[26,9],[21,7],[23,9],[19,11],[18,9],[20,10]])  #训练集数据（长，宽）
labels=['小鲫鱼','小鲫鱼','小鲫鱼','小鲫鱼','小蝌蚪','小蝌蚪','小蝌蚪']   #训练集数据对应的分类
K=3                                                                       #最临近值取3
testData=[20,11]                                                          #测试数据
def SolveStance(tData,Labels,testData):                                 #求所有训练集数据到测试数据的距离
    rData=[]                                                              #存放所求距离和分类值
    i=0
    for DotValue in tData:
        ed=np.sqrt((DotValue[0]-testData[0])**2+(DotValue[1]-testData[1])**2)#欧式公式求距离
        rData.append([ed,Labels[i]])                                      #所求距离和分类进行保存
        i+=1
    return rData                                                          #返回所求距离和分类
def SortSolve(rData):
    return sorted(rData)                                                  #从小到大排序
def GetKValues(sData,k):                                                  #得到K值和分类结果
    kData=sData[:k]                                                      #取前面K个最邻近值
    print(kData)
    ClassCount={}                                                        #分类统计存储
    for item in kData:
        ClassCount[item[1]]=ClassCount.get(item[1],0)+1                  #统计各自分类的次数
    rEnds=sorted(ClassCount.items())                                     
    return rEnds[-1:]                                                    #返回最后结果

StanceData=SolveStance(trainData,labels,testData)                         #获得距离列表
ss=SortSolve(StanceData)                                                   #对距离列表从小到大排序
sKind,rate=GetKValues(ss,K)[0]                                                     #求K值及最终判断值分类
print('输入测试值属于%s类,判断准确率百分之%d'%(sKind,100*(rate/K)))   #输出结果      
