# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 14:11:31 2019
   进栈出栈
@author: 刘瑜
源代码文件：U3Stack.py
"""
stack=[]
for s in range(1,7):
    stack.append(s)     #元素依次进栈
print('进栈后的堆栈情况：',stack)
i=1
while stack:
    print('元素%d第%d个出栈'%(stack.pop(),i))  #元素依次出栈
    i+=1