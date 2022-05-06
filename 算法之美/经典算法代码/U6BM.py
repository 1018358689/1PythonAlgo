# -*- coding: utf-8 -*-
"""
  Created on Thu Sep 12 19:26:26 2019
  BM字符串搜索算法
  @author: 刘瑜等
  源代码文件是：U6BM.py
"""
def GoodIndex(keys):       
    n=len(keys)
    m=n
    p=n                #好后缀在模式串里出现的最左边位置
    last=keys[n-1]     #最后一个字符,看作好后缀
    while n>1:         #检查模式串里左边有否一样的好后缀
        if keys[n-2]==last:
            p=n-2
        n-=1
    return m-p         

def CountBadIndex(keys,bad):
    n=len(keys)
    j=n
    while j>0:
        if keys[j-1]==bad:
            return n-j 
        j-=1
    return n        #坏字符在模式串中不存在

def CompareAndSearch(arr,keys):
    last_count=GoodIndex(keys)    #获取好后缀在模式串里从最右到最左的长度*
    print('最后一个字符在前面的重复次数%d'%(last_count))
    FindNum=0       #记录查找到的模式串的个数
    text_n=len(arr)
    k_n=len(keys)
    move=0      #模式串移动的下个开始位置   
    while move<=text_n-k_n:
        j=k_n-1
        print('移动位置%d'%(move))
        while j>=0:
            if arr[move+j]!=keys[j]:
                bad=arr[move+j]
                break            #存在坏字符
            j-=1
        if j==-1:                #找到字符串
            FindNum+=1
            move+=k_n
        else:
            if j==k_n-1:         #最后一个就不一致
                print('坏字符为%s'%(bad))
                d=CountBadIndex(keys,bad)
                print('增加的坏字符长度为%d'%(d))
                move+=d
            else:               #存在好后缀，检查最后一个字母在模式串前面出现的次数
                move+=k_n-last_count    #*
    print('模式串%s在文本串里找到到次数%d'%(keys,FindNum))

keys='China'
s1='I am from China. I am a student.I live in Tianjin China.I love Python.Are you from China'
CompareAndSearch(s1,keys)                
                
                    
    

