# -*- coding: utf-8 -*-
"""
  Created on Thu Aug 29 20:05:22 2019
  快速排序
  @author: 刘瑜等
  源代码文件是：U4QuickSort.py
"""
def MovePivot(arr,low,high):
    Pivot=arr[high]               #取最右边一个值
    imove=(low-1)                 #从最左边减1开始
    for i in range(low,high):
        if arr[i]<=Pivot:        
            imove+=1             #记录最近一个交换值下标
            arr[imove],arr[i]=arr[i],arr[imove]   #大的放后面，小的放imove处
    arr[imove+1],arr[high]=arr[high],arr[imove+1] #最后一次，把Pivot值放到imove+1处（分界处）
    return imove+1
def QuickSort(arr,low,high):
    if low<high:
        pivot=MovePivot(arr,low,high)
        QuickSort(arr,low,pivot-1)
        QuickSort(arr,pivot+1,high)
#s1=[10,3,28,4,12,20]
s1=[10,3,28,4,50,12,20]
print('排序前列表',s1)
h=len(s1)
QuickSort(s1,0,h-1)
print('快速排序结果',s1)
