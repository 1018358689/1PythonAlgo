# -*- coding: utf-8 -*-
"""
   Created on Mon Mar  9 20:59:57 2020
   约瑟夫生者死者小游戏
   @author: 刘瑜
   源代码文件是：U12Joseph_game.py
"""
people=[i for i in range(1,31)]
print('船上的人排队如下：',people)
pos=0                         #检查位置
goout=[]                      #记录投海的人的序号
number=len(people)            #人数
index=8
while number>15:              #大于15人，继续选择投海的人
    if index<number:          #9或9倍数的位置，且不能超过队伍人数
        goout.append(people[index]) #记录投海的人的序号
        del people[index]     #出队
        index=index+8         #寻找下第9个人
        number=len(people)    #重新获取人数
    else:                     #超过队伍人序号，从头开始继续数到9
        index=index-number    #从队伍头开始数数，要考虑队伍尾没有数的人数
print('下海的人序号：',goout)  #打印出队人序号
print('留下的人序号：',people) #打印留下来的人的序号
