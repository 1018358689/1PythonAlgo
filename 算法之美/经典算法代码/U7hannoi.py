# -*- coding: utf-8 -*-
"""
  Created on Fri Jan  3 15:31:48 2020
  递归求汉诺塔问题
  @author: 刘瑜等
  源代码文件是：U7hannoi.py
"""
def hanoi(n,x,y,z):
    if n==1:
        print(x,"-->",z)
    else:
        hanoi(n-1,x,z,y)   #将前n-1个盘子从x移动到y上
        print(x,'-->',z)  #将最底下的最后一个盘子从x移动到z上
        hanoi(n-1,y,x,z)   #将y上n-1个盘子移动到z上
n=3
print('%d个盘片时的移动过程：'%(n))
hanoi(n,'x','y','z')  #初始时n个盘片都在x针上，x,y,z代表三根针