# -*- coding: utf-8 -*-
"""
  Created on Sat Sep  7 14:49:32 2019
  哈希查找
  @author: 刘瑜等
  源代码文件是：U5HashSearch.py
"""
maxsize=20   #哈希表最大存放20个哈希值
HashTable={i:None for i in range(maxsize)}
print('哈希表大小为%d'%len(HashTable))

def Hash(value):   #哈希函数，采用留余数法求Address
    address=value%maxsize       #散列除留余数法求address
    if HashTable[address]==None:
        return address      #确定哈希地址
    else:                       #考虑键值冲突,试探下一个空值哈希表位置
        while address<maxsize:
            address+=1
            if HashTable[address]==None:
                return address
    return -1   #哈希表地址不够
    
    
def BuildHashTable(Values):     #根据哈希地址，存储哈希值
    for value in Values:
        address=Hash(value)
        print('建立的键值对(%d %d)'%(address,value))
        if address!=-1:
            HashTable[address]=value
        else:                       #考虑键值冲突,试探下一个空值哈希表位置
            print('数值%d存放的哈希表地址不够！'%(value))                
    return HashTable
def FindValue(HashT,value):
    address=value%maxsize
    if HashT[address]==value:
        return True
    else:
        address+=1 
        while address<maxsize:
            if HashT[address]==value:
                return True
            address+=1
    return False
   
s1=[20,30,1,2,5,8,23,44,48]
value=44
if FindValue(BuildHashTable(s1),value):
    print('在哈希表里找到%d'%(value))
else:
    print('在哈希表里找不到%d'%(value))


'''
class HashTable:
  def __init__(self, size):
    self.elem = [None for i in range(size)] # 使用list数据结构作为哈希表元素保存方法
    self.count = size # 最大表长
 
  def hash(self, key):
    return key % self.count # 散列函数采用除留余数法
 
  def insert_hash(self, key):
    """插入关键字到哈希表内"""
    address = self.hash(key) # 求散列地址
    while self.elem[address]: # 当前位置已经有数据了，发生冲突。
      address = (address+1) % self.count # 线性探测下一地址是否可用
    self.elem[address] = key # 没有冲突则直接保存。
 
  def search_hash(self, key):
    """查找关键字，返回布尔值"""
    star = address = self.hash(key)
    while self.elem[address] != key:
      address = (address + 1) % self.count
      if not self.elem[address] or address == star: # 说明没找到或者循环到了开始的位置
        return False
    return True
 
 
if __name__ == '__main__':
  list_a = [12, 67, 56, 16, 25, 37, 22, 29, 15, 47, 48, 34]
  hash_table = HashTable(12)
  for i in list_a:
    hash_table.insert_hash(i)
 
  for i in hash_table.elem:
    if i:
      print((i, hash_table.elem.index(i)), end=" ")
  print("\n")
 
  print(hash_table.search_hash(15))
  print(hash_table.search_hash(33))
'''
