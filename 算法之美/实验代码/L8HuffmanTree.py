# -*- coding: utf-8 -*-
"""
   Created on Sun Mar  1 21:30:46 2020
   哈夫曼树算法，求带权路径长度、求每个叶子节点的压缩二进制码
   @author: 刘瑜等
   源代码文件是：L8HuffmanTree.py
"""
def node_sort(R):   #对记录表，按照频率的大小反复排序，一直到所有的节点都加入二叉树
    return sorted(R,key=lambda one: one[1]) 
#哈夫曼树算法
def HuffmanTree(Records):
    newHT=[]   #记录生成的哈夫曼树
    sort_nodes=node_sort(Records)     #小到大排序
    print('第一次从小到大排序\n        ',sort_nodes)
    length=len(sort_nodes)
    if length==1:
        print('只有一个节点的哈夫曼树：',sort_nodes)
        return sort_nodes
    newHT.append(sort_nodes[0])      #第一次取最小频率的第1个节点
    newHT.append(sort_nodes[1])      #第一次取最小频率的第2节点
    new_parentNode=(sort_nodes[0][0]+sort_nodes[1][0],sort_nodes[0][1]+sort_nodes[1][1],1)
    newHT.append(new_parentNode)      #生成第一个父节点
    if length==2:                    #只有两个节点的哈夫曼树
        return newHT
    while True :
        sort_nodes=sort_nodes[2:]         #删除最小频率的两个节点
        sort_nodes.append(new_parentNode) #新生成的父节点同时存入记录表
        sort_nodes=node_sort(sort_nodes)  #重新从小到大排序
        print('    生成树newHT：\n        ',newHT)
        print('下次一次排序：\n        ',sort_nodes)
        length=len(sort_nodes)
        if length==2:                     #最后一次构建父节点
            new_parentNode=(sort_nodes[0][0]+sort_nodes[1][0],sort_nodes[0][1]+sort_nodes[1][1],sort_nodes[1][2]+1)
            newHT.append(new_parentNode)
            return newHT
        else:
            flag=True
            if (len(sort_nodes[0][0])==1 and len(sort_nodes[1][0])==1) and flag : #最小两个节点都是叶子节点
                if new_parentNode[1]>sort_nodes[1][1]:                 #2叶子节点都在父节点的左边
                    level=new_parentNode[2]
                    pos=newHT.index(new_parentNode)
                    new_parentNode=(sort_nodes[0][0]+sort_nodes[1][0],sort_nodes[0][1]+\
                                    sort_nodes[1][1],level+1)
                    newHT.insert(pos,(sort_nodes[0][0],sort_nodes[0][1],level))
                    newHT.insert(pos+1,(sort_nodes[1][0],sort_nodes[1][1],level))
                else:
                   level=new_parentNode[2]-1                       
                   if new_parentNode[1]<=sort_nodes[0][1]:#节点都等于大于比较的父节点
                       level+=1                         #2叶子节点在父节点的右边，否则在下一层的右边
                   new_parentNode=(sort_nodes[0][0]+sort_nodes[1][0],sort_nodes[0][1]+sort_nodes[1][1],level+1)
                   newHT.append((sort_nodes[0][0],sort_nodes[0][1],level))  #第1个节点插入
                   newHT.append((sort_nodes[1][0],sort_nodes[1][1],level))  #第2个节点插入
                newHT.append(new_parentNode)                         #1、2节点的父节点插入
                flag=False
            if flag:
                try:
                    index=newHT.index(sort_nodes[0])                 #哈夫曼树里获取的1节点是当前层的父节点之一
                    newHT.insert(index+1,(sort_nodes[1][0],sort_nodes[1][1],sort_nodes[0][2]))          #第2个节点记入树当前父节点的右边
                    new_parentNode=(sort_nodes[0][0]+sort_nodes[1][0],sort_nodes[0][1]+sort_nodes[1][1],sort_nodes[0][2]+1)
                    newHT.append(new_parentNode) #1、2节点的父节点插入
                except Exception:
                    try:
                        index=newHT.index(sort_nodes[1])                 #哈夫曼树里获取的2节点是当前层的父节点之一
                        if sort_nodes[0][1]>=sort_nodes[1][1]:            #叶子权重大于等于左边父节点权重，放右边
                            index+=1
                        newHT.insert(index,(sort_nodes[0][0],sort_nodes[0][1],sort_nodes[1][2])) #第2个节点记入树当前父节点的左边
                        new_parentNode=(sort_nodes[1][0]+sort_nodes[0][0],sort_nodes[1][1]+sort_nodes[0][1],sort_nodes[1][2]+1)
                        newHT.append(new_parentNode) #1、2节点的父节点插入
                    except Exception:
                        pass
           
Records=[('A',2,0),('B',3,0),('C',3,0),('D',4,0),('E',7,0),('F',6,0)]           #数据格式（字母，字出现的频率，记录层级，初始叶子都为第0层）
#Records=[('A',19,0),('B',21,0),('C',2,0),('D',3,0),('E',6,0),('F',7,0),('G',10,0),('H',32,0)] 
#Records=[('A',9,0),('B',12,0),('C',6,0),('D',3,0),('E',5,0),('F',15,0)] 
h_tree=HuffmanTree(Records)
print('最后哈夫曼树生成结果：\n',h_tree)

def SolutionPath(h):   #求哈夫曼树带权路径长度
    length=0
    for one in h:
        length+=one[1]*(3-one[2])
    return length
p=SolutionPath(h_tree)
print('该哈夫曼树带权路径长度为',p)

def SolutionBin(H,R): #求哈夫曼树每个叶子节点的二进制压缩编码
    B={}              #记录每个叶子节点的二进制码       
    for one in R: 
        B[one[0]]=''    
    for s in R:       #依次求每个叶子节点的二进制编码
        first=' '      #用于上下父节点之间比较
        for one in H: #该哈夫曼树
            if len(one[0])>1: #对父节点进行判断 
                if s[0] in one[0]: #子节点在父节点里
                    if s[0]==one[0][0]:  #字节点在左边
                        B[s[0]]='0'+B[s[0]]
                    else:
                        if first[0]==one[0][0]: #父节点在左边
                            B[s[0]]='0'+B[s[0]]
                        else:
                            B[s[0]]='1'+B[s[0]]
                    first=one[0]         #记录前一个父节点
    return B
B=SolutionBin(h_tree,Records)
print(B)
                