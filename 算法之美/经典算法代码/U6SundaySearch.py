# -*- coding: utf-8 -*-
"""
  Created on Fri Sep 13 09:45:58 2019
  Sunday算法
  @author: 刘瑜等
  源代码文件是：U6SundaySearch.py
"""
def CheckKeys(keys,endi): #检查模式串尾+1对应的文本串字符，在模式串里的位置
    n=len(keys)
    j=n-1
    while j>=0:           
        if keys[j]==endi:
            print('%s的距末位置%d'%(endi,j))
            return n-j   #移动相对位置数n-j
        j-=1
    return n+1     #模式串中不存在，移动次数n+1
def SundaySearch(arr,keys):
    count=0              #找到子串数量
    i=0
    t_n=len(arr)-1
    k_m=len(keys)-1
    while i<=t_n:
        j=0
        m=0
        while j<=k_m:      #比较模式串字符与文本串对应的字符
            if arr[i+j]!=keys[j]:   
                if i+k_m+1>t_n:   #模式串与文本串最后比较时，i+k_m+1不能超过文本串的长度
                    m=-1
                    i+=k_m+1
                    break        #最后一次比较时，剩余文本串长度小于模式串，退出循环
                endi=arr[i+k_m+1]  #比较模式串末尾+1对应的文本串的字符C
                m=CheckKeys(keys,endi) 
                begin=arr[i]
                i+=m             #往右移动m位
                print('开始比对字符串%s，末尾+1处%s，移动下标到%d处,移动了%d'%(begin,endi,i,m))
                break  
            j+=1
        if  m==0:               
            count+=1             #记录匹配串的数量
            print('找到%s开始下标%d,'%(keys,i))
            i+=k_m+1             #右移动k_m+1 
    print('%s在文本串里找到%d次'%(keys,count))
keys='China'
#s1='dddchina'
s1='I am from China. I am a student.I live in Tianjin China.I love Python.Are you from China'
SundaySearch(s1,keys) 

           