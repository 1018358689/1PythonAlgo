# -*- coding: utf-8 -*-
"""
  Created on Sat Aug 31 15:04:43 2019
  线性检索
  @author:刘瑜等
  源代码文件是：U5LinearFind.py
"""
def LinearFind(arr,key):
    n=len(arr)
    i=0     #从左边开始依次找
    while i<n:
        if arr[i]==key:
            return i    #返回找到元素的下标
        i+=1
    return -1            #没有找到元素
if __name__ == '__main__':
    s1=[100,22,44,0,2,492,3,20,38]
    key=5
    r=LinearFind(s1,key)
    print('待查找的元素列表',s1)
    if r!=-1 :
        print('元素%d找到，其下标为%d'%(key,r))
    else:
        print('元素%d没有找到'%(key))

