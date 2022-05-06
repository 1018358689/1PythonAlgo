# -*- coding: utf-8 -*-
"""
  Created on Mon Aug 26 18:35:13 2019

  希尔排序
  @author: 刘瑜等
  源代码文件是：U4SellSort.py
"""
def SellSort(arr):
    n=len(arr)
    endi=0                    #最后修改下标
    if n==1 :
        return 1
    space=n//3                     #从列表中三分之一位置作为增量
    while space> 0: 
        for i in range(space):   #控制一个间隔循环几次
            key= arr[i] 
            j=0                  #每个元素控制比较次数
            while i+(j+1)*space<n :
                print('交换开始下标数%d，交换结束%d'%(j,i+(j+1)*space))
                if space>1 :
                     if arr[i+(j+1)*space]<key: 
                         arr[i+j*space] = arr[i+(j+1)*space]
                         endi=i+(j+1)*space
                     
                else:              #当增量为1时，相邻元素比较，调整
                   if arr[j]>arr[j+1]:
                       arr[j],arr[j+1]=arr[j+1],arr[j]
                j+=1       
                    
            if arr[i]!=key:         #必须考虑无需交换情况
                arr[endi]=key
            print('第%d'%(i))
            print(arr)
        space-=1
              

#s1=[18,3,0,5,2,10,7]
s1=[18,3,0,5,2,10,7,15,38,100]
print('排序前的列表值：',s1)
SellSort(s1)
print('排序后的列表值：',s1)
                 
            
