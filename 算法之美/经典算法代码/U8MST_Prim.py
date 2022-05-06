# -*- coding: utf-8 -*-
"""
  Created on Sun Mar  1 16:15:29 2020
  @author: 刘瑜等
  源代码文件是：U8MST_Prim.py
"""

def FindMinEdge(Nodes,row,edge,mst):
    n=len(edge)
    j=0   
    s_edge=sorted(edge)          #权重从小到大排序
    e_min=s_edge[0]              #获取权重最小值 
    while j<n:
        if edge[j]==e_min :      #找到最小值的对应下标
            a,b=Nodes[row],Nodes[j]
            if not([a,b,e_min] in mst or [b,a,e_min] in mst):#考虑节点的边已经存在
                return j         #返回找到的合适的最小权重边对应的列索引下标
            else:
                if s_edge[0]==s_edge[1]: #前后边权重一样,要避免原始下标位置一直在前面的问题
                    j+=1
                    continue
                j=-1             #j准备从-1,0重新开始查找比较新的最小值
                del(s_edge[0])   #删除重复节点，生成新的s_edge列表
                e_min=s_edge[0]  #获取下一个权重最小值
        j+=1    
    return -1               
def prim(nodes,edges):          #每个节点选取最小边的原则进行
    Mst=[]                      #记录最小生成树节点
    i=0                         #从第1行开始
    n=len(nodes)                #节点数
    for one in edges:
       index=FindMinEdge(nodes,i,one,Mst) #每个节点选一个最小权重的边，已经选入的需要去掉
       a,b,w=nodes[i],nodes[index],edges[i][index]#每次找到的边的两个节点和权重
       Mst.append([a,b,w])                #加入最小生成树
       i+=1
       if i==n-1:                         #最小生成树的边数是n-1
           break
    return Mst
    
f=float('inf')   
nodes=['A','B','C','D','E','F']
edges_list=[[f,1,6,6,f,f],
            [1,f,4,3,5,4],
            [6,4,f,f,3,f],
            [6,3,f,f,f,2],
            [f,5,3,f,f,3],
            [f,4,f,2,3,f]]

r=prim(nodes,edges_list)
print('城市群最小生成树为：',r)