# -*- coding: utf-8 -*-
"""
  Created on Sat Feb 29 19:11:50 2020
  kruskal算法求最小生成树
  @author: 刘瑜等
  源代码文件是：U8MST_kruskal.py
"""               
def kruskal_Tree(nodes,edges):
    Mst=[]      #记录最小生成树节点
    n=len(nodes) #节点数
    i=0
    sort_Glist=sorted(edges,key=lambda one: one[2]) #对带权数边进行从小到大排序
    print('从小到大按照边的权重数进行排序：\n',sort_Glist)
    for one in sort_Glist:  #找出独立的最小树
        if not((one[0]in Mst and one[1] in Mst) or (one[1]in Mst and one[0] in Mst)):
            Mst.append(one) #合成记录最小生成树
            i+=1            #记录权重最小数个数
        if i==n-1:
            break
    return Mst #返回最小生成树
nodes=['A','B','C','D','E','F']
nodes_list=[('A','B',1),('A','C',6),('A','D',6),
            ('B','D',3),('B','F',4), ('B','E',5), ('B','C',4),
            ('C','E',3),
            ('D','F',2), 
            ('E','F',3)] 
Tree=kruskal_Tree(nodes,nodes_list)     
print('求得最小生成树：\n',Tree)
