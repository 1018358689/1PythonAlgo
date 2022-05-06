# -*- coding: utf-8 -*-
"""
  Created on Wed Dec 11 21:04:45 2019
  邻接表
  @author: 刘瑜等
  源代码文件是：U3AdjacencyTable.py
"""
class Node():    #建立一个链表节点类
    def __init__(self,NodeValue,Edgevalue):
        self.Edgevalue=Edgevalue
        self.NodeValue=NodeValue
        self.Next=None
class AdjacencyTable():
    def __init__(self,Lines):
        self.Lines=Lines         #字典对象
    def getTopNode(self):        #获取图节点
        for k in self.Lines:
            print("图节点:",k)
    def addNewEdgeNode(self,TopKey,NodeValue,EdgeValue): #增加链表节点
        if TopKey in self.Lines:       #判断键是否在字典中
            Address=self.Lines[TopKey]          #获取指向链表的地址 
            if Address is None:
                self.Lines[TopKey]=Node(NodeValue,EdgeValue) #增加链表第一个节点
            else:
                while Address :               #非空地址
                    if Address.Next :
                        Address=Address.Next
                    else:                    #如果是空地址
                        Address.Next=Node(NodeValue,EdgeValue) #增加新链表节点
                        break
        else:   #字典无该键
            print('无该图节点：',TopKey)
#===============================================图遍历
    def printAll(self):
        if self.Lines is None:
            print('图没有节点！')
        else:
            for k,v in self.Lines.items():
                print('图节点：',k)
                while v:
                    print('  其连接节点是%d,连接边是%d'%(v.NodeValue,v.Edgevalue))
                    v=v.Next
                
#===============================================实例化
TopNode={1:None,2:None,3:None,4:None,5:None,6:None,7:None}
CityLines=AdjacencyTable(TopNode)
CityLines.addNewEdgeNode(1,2,1)
CityLines.addNewEdgeNode(1,3,2)
CityLines.addNewEdgeNode(1,4,3)
CityLines.addNewEdgeNode(2,6,4)
CityLines.addNewEdgeNode(3,6,5)
CityLines.addNewEdgeNode(3,5,6)
CityLines.addNewEdgeNode(4,5,7)
CityLines.addNewEdgeNode(5,7,8)
CityLines.addNewEdgeNode(6,7,9)
CityLines.getTopNode()
print('图遍历：')
CityLines.printAll()  
        