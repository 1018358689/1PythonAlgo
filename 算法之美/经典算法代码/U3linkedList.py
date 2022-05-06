# -*- coding: utf-8 -*-
"""
    Created on Mon Dec  2 19:53:25 2019
       构建链表，访问链表值，打印节点个数及节点值
    @author:刘瑜
    源代码文件是：U3linkedList.py
"""
class Node(): #定义节点类
    def __init__(self,data=None,next=None): #初始化类
        self._data=data
        self._next=next
    def setData(self,NewData):         #设置节点的数值
        self._data=NewData
    def setNext(self,NewNext):         #设置节点的下一个地址
        self._next=NewNext
    def getData(self):                 #得到节点的数值
        return self._data
    def getNext(self):                 #得到节点的下一个地址
        return self._next

class LinkedList():                      #建立链表类
    def __init__(self):                  #初始化类
        self._head=Node()                #链表头
        self._length=0                   #链表长度
    def tail_add(self,NewData):          #在链表尾部增加节点
        NewNode=Node(NewData,None)       #新增一个节点
        if self._length==0:              #空链表
            self._head=NewNode           #把新增节点对象赋值给head
            self._length=1               #链表长度变1
        else:
            current=self._head
            while current.getNext()!=None:#判断下一个地址是否None
                current=current.getNext() #根据地址next遍历链表
            current.setNext(NewNode)      #找到链尾，增加新节点
            self._length+=1               #链表数量加一
    def PrintLinkedList(self):           #遍历并打印节点数值
        curr=self._head
        while curr!=None:                #判断下一个地址是否None
            print('打印节点：%s'%(curr.getData()))
            curr=curr.getNext()
    def getLength(self):
        return self._length
#==================================调用链表类实例，并打印结果
foods=['apple','water','juice','tomato']
newLinked=LinkedList()             #建立链表实例
for s in foods:
    newLinked.tail_add(s)          #增加节点，并给每个节点赋值
print(newLinked.getLength())       #打印链表节点数
newLinked.PrintLinkedList()        #打印所有的节点的值
    