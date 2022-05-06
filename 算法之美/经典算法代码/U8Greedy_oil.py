# -*- coding: utf-8 -*-
"""
  Created on Thu Mar  5 20:55:10 2020
  贪心算法求最少的加油次数
  @author: 刘瑜等
  源代码文件是：U8Greedy_oil.py
"""
def oil(n,distance):
    i=1                           #起始站加油算第一次
    count=0                       #当前站与下一站的距离
    for one in distance:
        count+=one                #试着继续累加公里数，尽量跑最长距离
        if n<count:               #加满油开始持续跑，超过当前加油距离累加公里数
            print('%d公里开始处加油'%(one))#累加距离等于或超过一次跑最长距离，要加油了
            count=one             #加满油，从新开始累计跑的距离
            i+=1                  #计加油次数
    return i
n=300
dis=[150,180,120,100,280,160]    #要求距离间隔都小于n，否则汽车中途要抛锚了
#dis=[150,60,50,180,120,100,280,160]
num=oil(n,dis)
print('该车最少要加油%d次'%(num))