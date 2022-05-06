# -*- coding: utf-8 -*-
"""
  Created on Thu Aug 22 14:43:57 2019
  Knuth_DurstenfeldShuffle洗牌算法
  @author: 刘瑜
  源代码文件：U12Knuth_DurstenfeldShuffle.py
"""
import random
cards=[i for i in range(1,10)] #产生1到9顺序数
print(cards)
n=len(cards)                #取列表的长度
i=n-1                       #i指向列表最后一个元素
while i>=0:                 #从列表最大范围,缩小到0
    p=random.randint(0,i)   #在实际长列表里随机产生一个顺序号p
    cards.append(cards[p])  #把该顺序号指向的元素抽取,放到列表尾部
    del cards[p]            #删除该位置的元素
    i-=1                    #缩小抽取范围
print(cards)                #打印随机取值的结果
