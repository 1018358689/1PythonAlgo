# -*- coding: utf-8 -*-
"""
  Created on Sat Apr 11 20:21:33 2020
  Inside-Out Shuffle洗牌算法
  @author: 刘瑜
  源代码文件是：U12Inside_Out.py
"""
import random
cards=[i for i in range(1,10)] #产生1到9顺序数
print(cards)
i=0
n=len(cards)            #取被取值列表的长度  
while i<n:
    p=random.randint(0,i)
    cards[i],cards[p]=cards[p],cards[i]#对换牌号
    i+=1
print(cards)
