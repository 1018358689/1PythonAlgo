# -*- coding: utf-8 -*-
"""
  Created on Wed Dec 11 16:51:52 2019
  用列表实现二维邻接矩阵
  @author: 刘瑜等
  源代码文件是：U3GraphList.py
"""
import numpy as np
class AdjacencyMatrix():            #邻接矩阵类
    def __init__(self,n=2):
        self.Matrix=np.zeros((n,n))
    def getMatrix(self):            #打印邻接矩阵
        for d in self.Matrix:
            print(d)
    def addEdge(self,x,y,value):
        self.Matrix[x,y]=value      #设置1代表节点之间存在关系，0代表没有关系
#================================
airport=AdjacencyMatrix(4)          #四个飞机场节点
airport.addEdge(0,1,1)              #A与B建立关系
airport.addEdge(0,2,1)              #A与C建立关系
airport.addEdge(0,3,1)              #A与D建立关系
airport.addEdge(2,3,1)              #C与D建立关系
airport.addEdge(3,0,1)              #D与A建立关系
airport.getMatrix()                 #打印邻接表
