# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 23:31:17 2020

@author: 111
"""

#coding:utf-8
# 极大似然估计  朴素贝叶斯算法
import pandas as pd
import numpy as np

class NaiveBayes(object):
    def getTrainSet(self):
      
        dataSetNP = np.array([['A地区',24,'女','医生',1],
                ['A地区',24,'男','工人',0],
                ['A地区',65,'男','农民',0],
                ['A地区',65,'女','工人',0],
                ['A地区',24,'女','教师',1],
                ['B地区',24,'女','企业员工',1],
                ['B地区',25,'男','政府职员',1],
                ['B地区',15,'女','学生',0],
                ['B地区',16,'男','学生',0],
                ['C地区',34,'女','教师',0],
                ['C地区',35,'男','工人',0],
                ['C地区',45,'男','农民',0]])
        trainData = dataSetNP[:,0:dataSetNP.shape[1]-1]   #训练数据x1,x2
        labels = dataSetNP[:,dataSetNP.shape[1]-1]        #训练数据所对应的所属类型Y
        return trainData, labels

    def classify(self, trainData, labels, features):
        #求labels中每个label的先验概率
        labels = list(labels)    #转换为list类型
        labelset = set(labels)
        P_y = {}       #存入label的概率
        for label in labelset:
            P_y[label] = labels.count(label)/float(len(labels))   # p = count(y) / count(Y)
            print(label,P_y[label])

        #求label与feature同时发生的概率
        P_xy = {}
        for y in P_y.keys():
            y_index = [i for i, label in enumerate(labels) if label == y]  # labels中出现y值的所有数值的下标索引
            for j in range(len(features)):      # features[0] 在trainData[:,0]中出现的值的所有下标索引
                x_index = [i for i, feature in enumerate(trainData[:,j]) if feature == features[j]]
                xy_count = len(set(x_index) & set(y_index))   # set(x_index)&set(y_index)列出两个表相同的元素
                pkey = str(features[j]) + '*' + str(y)
                P_xy[pkey] = xy_count / float(len(labels))
                print(pkey,P_xy[pkey])

        #求条件概率
        P = {}
        for y in P_y.keys():
            for x in features:
                pkey = str(x) + '|' + str(y)
                P[pkey] = P_xy[str(x)+'*'+str(y)] / float(P_y[y])    #P[X1/Y] = P[X1Y]/P[Y]
                print(pkey,P[pkey])

        #求[2,'S']所属类别
        F = {}   #[2,'S']属于各个类别的概率
        for y in P_y:
            F[y] = P_y[y]
            for x in features:
                F[y] = F[y]*P[str(x)+'|'+str(y)]     #P[y/X] = P[X/y]*P[y]/P[X]，分母相等，比较分子即可，所以有F=P[X/y]*P[y]=P[x1/Y]*P[x2/Y]*P[y]
                print(str(x),str(y),F[y])

        features_label = max(F, key=F.get)  #概率最大值对应的类别
        return features_label


if __name__ == '__main__':
    nb = NaiveBayes()
    # 训练数据
    trainData, labels = nb.getTrainSet()
    # x1,x2
    #features = ['A地区',24,'女','教师']
    features =['B地区',65,'男','工人']
    # 该特征应属于哪一类
    result = nb.classify(trainData, labels, features)
    print(features,'属于',result)