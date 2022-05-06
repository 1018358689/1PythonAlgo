# -*- coding: utf-8 -*-
"""
  Created on Fri Feb 14 17:01:12 2020
  一元线性回归算法（最小二乘法）
  @author: 刘瑜
  源代码文件是：U11LR.py
"""
import numpy as np
import matplotlib.pyplot as plt
people=[2,5,7,8,12,15,17,20,20,25]
money=[50,143,145,208,215,320,332,390,455,510]
plt.scatter(people,money, label='Sale Data', color='k')
plt.show()
def LR(x,y):
    x_mean=np.mean(x)    #求x自变量均值
    y_mean=np.mean(y)    #求y应变量均值
    a=np.sum((x-x_mean)*(y-y_mean))/np.sum((x-x_mean)**2)  #求斜率
    b=y_mean-a*x_mean    #求误差
    return [a,b]         #列表形式返回a,b
ab=LR(people,money)
print('斜率，误差分别为：',ab)
y=ab[0]*np.array(people)+ab[1]
plt.scatter(people,money, label='Sale Data', color='k')
plt.plot(people, y, label='regression line')
plt.xlabel("购买人数",fontproperties="STCAIYUN",fontsize=20)  #华文彩云
plt.ylabel("金额（元）", fontproperties="STCAIYUN",fontsize=20) 
plt.legend()
plt.show()