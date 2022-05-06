# -*- coding: utf-8 -*-
"""
  Created on Wed Sep  4 20:08:50 2019
  斐波那契查找
  @author: 刘瑜等
  源代码文件是：U5FibonacciSearch.py
"""
def FibonacciSearch(arr, key):
  # 求斐波那契列表
  n=len(arr)
  i=1
  F=[1,1,]        #存放生成的斐波那数
  while F[i]<=n:
      F.append(F[i-1]+F[i])
      i+=1
  print('生成的斐波那契数',F)
  left = 0
  right =n - 1
  # 为了满足斐波那契前后相邻数比，当右边数不够时，用最右边数补充缺的个数
  f =F[i]               #最右边的斐波那契数    
  print('生成的最右边的斐波那契数%d'%(f))
  i=0
  while i<f-n:          #补充数列右边不足的个数
    arr.append(arr[right])
    i += 1
  print(arr)
  k=len(F)              #斐波那契数列元素个数
  t= 0                  #查找计数器
  while left <= right:
    t += 1              #统计查找次数
    if k < 2:
      mid = left
    else:
      mid = left + F[k-1]-1
    print("left=%s, mid=%s, right=%s" % (left, mid, right))
    if key < arr[mid]:
      right = mid - 1
      k -= 1
    elif key > arr[mid]:
      left = mid + 1
      k -= 2
    else:
      print("查找次数: %s" % t)  
      if mid <= right:
          return mid
      else:
          return right
  print("查找次数: %s" % t)
  return False
#key=70
key=90
s1= [0,3,5,7,10,30,50,70,80,100]
r=FibonacciSearch(s1,key)
if r==False:
    print('数%d在列表里没有找到！')
else:
    print('查找数%d在列表里的下标为%d'%(key,r))

