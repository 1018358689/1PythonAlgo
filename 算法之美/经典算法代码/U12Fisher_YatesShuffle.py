# -*- coding: utf-8 -*-
"""
  Created on Sat Apr 11 14:50:34 2020
  Fisher_YatesShuffle洗牌算法
  @author: 刘瑜
  源代码文件是：U12Fisher_YatesShuffle.py
"""

import random
cards=[i for i in range(9)] #产生0到8顺序数
print(cards)
i=0
news=[]                     #接受产生的随机数
while cards:                #列表里有数值,就循环
    n=len(cards)            #取被取值列表的长度
    if n==1:                #当最后一个数值时
       news.append(cards[0])#可以直接放到新列表尾部
       break                #跳出循环
    i=random.randint(0,n-1) #在实际长列表里随机产生一个顺序号i
    news.append(cards[i])   #把取得的数放入接受取值列表里
    cards[i]=cards[-1]      #把原先列表的尾部数放到i处
    del cards[-1]           #删除尾部一个值
print(news)                 #打印随机取值的结果
