# -*- coding: utf-8 -*-
"""
  Created on Sat Feb 29 11:26:40 2020
  最大体积策略贪心算法求背包问题
  @author: 刘瑜等
  源代码文件是:U8Greedy01.py
"""
def FreeSpace(free,goods):     #比较物品还能不能放入背包
    return free-goods
  
def Greedy():
    goods_values=[20,10,15,25]  #蛋糕价值
    goods_volumes=[3,1,2,4]     #蛋糕体积
    bag_volume=5                #背包最大体积
    print('背包最大体积为:',bag_volume)
    Enter_records=[]            #记录装入物体对应的价值
    sort_volumes=goods_volumes.copy()#为从小到大排序使用
    sort_volumes.sort()         #从小到大排序
    while sort_volumes :
        maxVolume=sort_volumes.pop(-1) #获取最大值体积
        Free=FreeSpace(bag_volume,maxVolume)
        if Free>=0:
            bag_volume=Free     #背包实际空余空间
            print('装入物体体积',maxVolume)
            Enter_records.append(goods_values[goods_volumes.index(maxVolume)])
    if Enter_records!=None:
        print('最大体积策略贪心算法求背包装入物体价值为%d元'%(sum(Enter_records)))
Greedy()        
