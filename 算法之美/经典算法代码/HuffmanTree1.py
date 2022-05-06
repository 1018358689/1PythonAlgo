# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 21:30:46 2020
   存在问题的哈夫曼算法
@author: 111
"""

def node_sort(R):   #对记录表，按照频率的大小反复排序，一直到所有的节点都加入二叉树
    return sorted(R,key=lambda one: one[1])
 
#哈夫曼算法
def HuffmanTree(Records):
    newHT=[]   #记录生成的哈夫曼树
    sort_nodes=node_sort(Records)     #小到大排序
    print('第一次从小到大排序\n',sort_nodes)
    length=len(sort_nodes)
    if length==1:
        print('只有一个节点的哈夫曼树：',sort_nodes)
        return sort_nodes
    newHT.append(sort_nodes[0])      #第一次取最小频率的第1个节点
    newHT.append(sort_nodes[1])      #第一次取最小频率的第2节点
    new_parentNode=(sort_nodes[0][0]+sort_nodes[1][0],sort_nodes[0][1]+sort_nodes[1][1],1)
    newHT.append(new_parentNode)      #生成第一个父节点
    if length==2:
        return newHT
    while True :
        sort_nodes=sort_nodes[2:]         #删除最小频率的两个节点
        sort_nodes.append(new_parentNode) #新生成的父节点同时存入记录表
        sort_nodes=node_sort(sort_nodes)  #重新从小到大排序
        print('生成树：\n',newHT)
        print('下次一次排序：\n',sort_nodes)
       
        length=len(sort_nodes)
        if length==1:
            print(sort_nodes)
            return newHT
        if length==2:                     #最后一次构建父节点
            new_parentNode=(sort_nodes[0][0]+sort_nodes[1][0],sort_nodes[0][1]+sort_nodes[1][1],sort_nodes[1][2]+1)
            newHT.append(new_parentNode)
            return newHT
        else:
            if new_parentNode[0] in sort_nodes[0]:  #记录表里1节点是当前父节点
                newHT.append(sort_nodes[1])          #第2个节点记入树当前父节点的右边
            elif new_parentNode[0] in sort_nodes[1]:  #记录表里获取的2节点是当前父节点
                newHT.insert(len(newHT)-1,(sort_nodes[0],sort_nodes[1],new_parentNode[2])) #第2个节点记入树当前父节点的左边    
            elif not(new_parentNode[0] in sort_nodes[0] and new_parentNode[0] in sort_nodes[1]): #记录表里1，2节点都不是当前父节点   
                new_parentNode=(sort_nodes[0][0]+sort_nodes[1][0],sort_nodes[0][1]+sort_nodes[1][1],new_parentNode[2])
                newHT.append((sort_nodes[0][0],sort_nodes[0][1],new_parentNode[2]-1))  #第1个节点插入
                newHT.append((sort_nodes[1][0],sort_nodes[1][1],new_parentNode[2]-1))  #第2个节点插入
                newHT.append(new_parentNode)                         #1、2节点的父节点插入
           
Records=[('A',2,0),('B',3,0),('C',3,0),('D',4,0),('E',7,0),('F',6,0)]           #数据格式（字母，字出现的频率，记录层级，初始叶子都为第0层）
h_tree=HuffmanTree(Records)
print(h_tree)
