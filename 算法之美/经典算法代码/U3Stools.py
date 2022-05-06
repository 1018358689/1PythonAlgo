# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 20:30:40 2019
    抢凳子游戏
@author: 刘瑜
源代码文件：U3Stools.py
"""
import random
flag=True
queue=[1,2,3,4,5,6,7]          #记录初始抢凳子的人的排队情况
while flag:
    if len(queue)==1:
        print('抢凳子游戏%d获胜！'%(queue[0]))
        break
    hit=random.randint(1,3)   #产生1到3的一个整数，代表击鼓次数
    while hit>=1:
       pop1=queue.pop()       #从列表右边弹出一个元素，并在列表右边删除该元素
       if hit==1:
           print('本次击鼓%d被淘汰！'%(pop1))
           break              #第一次击鼓结束
       queue.insert(0,pop1)   #把列表右边的元素插入列表最左边，转圈子
       hit-=1
        
