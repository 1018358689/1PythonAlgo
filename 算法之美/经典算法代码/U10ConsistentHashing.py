# -*- coding: utf-8 -*-
"""
  Created on Wed Feb 19 22:59:40 2020
  一致性哈希算法,用 sha1()哈希函数
  @author: 刘瑜
  源代码文件是：U10ConsistentHashing.py
"""
import hashlib                      #导入带sha1()哈希算法函数的库 
class CHash(object):                #定义一致性哈希算法类
    def __init__(self, nodes=None, v_num=2):#nodes列表存放节点地址，v_num一个节点对应的虚拟节点数默认为2
        self._v_num = v_num         #一个节点对应的虚拟节点数，默认2个
        self._vNode_IP={}          #用于将虚拟节点的hash值与node的对应关系
        self._vNodeAdd=[]          #用于存放所有的虚拟节点的hash值，这里需要保持排序
        for node in nodes:         #初始化虚拟节点环并顺序排序
            self.addNode(node)
        print('\n虚拟节点哈希值升序排序结果：\n',self._vNodeAdd) #对虚拟节点哈希地址进行从小到大排序
        
    def addNode(self, node):           #建立虚拟节点环（需要顺序排序）
        for i in range(self._v_num):    #根据虚拟节点数，为每个节点建立虚拟节点
            vNodeStr = "%s%s" % (node, i) #新的虚拟节点IP地址为：服务器节点IP+i
            key = self._gen_key(vNodeStr) #产生虚拟节点的哈希地址
            print('虚拟节点字符串',vNodeStr,'对应的哈希值:',key)
            self._vNode_IP[key] =node   #虚拟节点哈希地址为键，节点IP地址为值
            self._vNodeAdd.append(key)   #对虚拟节点哈希地址进行独立存储
        self._vNodeAdd.sort()
       
    def delNode(self, node):             #删除退出节点地址及对应的虚拟地址
        for i in range(self._v_num):
            vNodeStr= "%s%s" % (node, i) 
            key = self._gen_key(vNodeStr) #产生虚拟节点的哈希地址
            del self._vNode_IP[key]      #通过哈希地址删除字典里的虚拟节点信息
            self._vNodeAdd.remove(key)   #删除虚拟节点哈希地址
 
    def dataNode(self,data):              #返回数据存储对应的服务器地址
        if self._vNodeAdd:                #虚拟节点哈希地址列表不为空
            key = self._gen_key(data)     #产生业务数据对应的哈希地址
            print(data,' 哈希地址：',key)
            for node_key in self._vNodeAdd: #获取虚拟节点的哈希地址
                if key <= node_key:          #如果业务数据的哈希地址小于等于当前虚拟节点的哈希地址
                    return self._vNode_IP[node_key] #返回当前虚拟节点哈希地址对应的接点IP地址值
            return self._vNodeAdd[self._vNodeAdd[0]]#如果业务数据的哈希值超过所有节点的地址，则归入并返回第一个节点IP地址
        else:
            return None                    #没有节点
 
    @staticmethod
    def _gen_key(key_str):              #通过sha1()产生哈希值
        hashValue= hashlib.sha1(key_str.encode('utf8')).hexdigest()#获取sha1()函数计算后的哈希地址
        #print(hashValue)
        return hashValue
 
C_H=CHash(["192.168.1.1","192.168.1.2","192.168.1.3","192.168.1.4"])
data=["大熊猫","三酷猫","布偶猫"]
print('\n正常情况下，存储数据时，归入的节点地址:')
print(data[0]+' 存入的节点IP地址:',C_H.dataNode(data[0]))
print(data[1]+' 存入的节点IP地址:',C_H.dataNode(data[1]))
print(data[2]+' 存入的节点IP地址:',C_H.dataNode(data[2]))
#192.168.1.2脱离
print('\n192.168.1.2节点脱离分布式系统的情况:')
C_H.delNode("192.168.1.2")     #删除节点
print(data[0]+' 存入的节点IP地址:',C_H.dataNode(data[0]))
print(data[1]+' 存入的节点IP地址:',C_H.dataNode(data[1]))
print(data[2]+' 存入的节点IP地址:',C_H.dataNode(data[2]))

