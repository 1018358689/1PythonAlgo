# -*- coding: utf-8 -*-
"""
  Created on Mon Apr  6 10:36:01 2020
  @author: 刘瑜
  源代码文件是：L9missile.py
"""
Missile=[290,480,120,99,700,500]
i=0   #统计拦截套数
j=0   #从第一枚导弹开始
n=len(Missile) #来袭导弹数量
print('来袭导弹：',Missile)
while  i<n:
    firstH=3000  #拦截弹初始高度 
    Intercept=[] #记录一套拦截导弹的高度
    j=i
    while j<n:   #一套拦击系统可以击落的导弹
       if firstH>Missile[j] and Missile[j]!=0:  #拦截弹高于来袭导弹的高度
           Intercept.append(Missile[j])
           firstH=Missile[j]  #拦截弹新的高度
           Missile[j]=0       #0为已经被拦截   
       j+=1
    i+=1
    print('第',i,'套拦截了：',Intercept)     
    if sum(Missile)==0:
        break
print('完全拦截来袭导弹，需要%d套拦截系统。'%(i))      