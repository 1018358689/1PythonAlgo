# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 19:37:08 2019
    FIFO
@author: 刘瑜等
源代码文件是：U31FIFO.py
"""
import queue          #导入queue模块
s1='我是一只三酷猫!'
FIFO=queue.Queue()
i=len(s1)-1 
while i>=0 :
    FIFO.put(s1[i])
    i-=1
while not FIFO.empty():
    print(FIFO.get())
