# -*- coding: utf-8 -*-
"""
  Created on Thu Feb 20 21:32:44 2020
  一维问题的梯度下降算法
  @author: 刘瑜
  源代码文件是：U11GadientDescent1.py
"""
import numpy as np
import matplotlib.pyplot as plt
def f(x):  #目标函数，这里是f(x)=x**2+1
    return np.array(x)**2 + 1 #求f(x)

def d1(x): #对f(x)求导，即是目标函数的梯度
    return x * 2  #对f(x)求导

def gradient_descent_1d(cur_x=0.1, learn_rate=0.01, e=0.001, count=5000):
    #cur_x为初始x值，learn_rate为学习率，e为误差，count为最大迭代次数
    for i in range(count):
        grad=d1(cur_x)       #求当前x的梯度
        if abs(grad) <e:   #梯度收敛到指定误差内
            break                       #退出迭代过程
        cur_x=cur_x-grad*learn_rate #一维梯度下降迭代公式
        print("第%d次迭代逼近值为 %f"%(i+1,cur_x))
    print("最小值 ：", cur_x)
    print('最小值保留小数点后6位%.6f'%(cur_x))
    return cur_x
def ShowLine(minX,minY):    #显示目标函数曲线，及梯度下降最小值逼近情况
    x=[x for x in range(10)]+[x*(-1) for x in range(1,10)]
    x.sort()
    print(x)
    plt.plot(x,f(x))         #显示目标曲线
    plt.plot(minX,minY,'ro') #显示逼近的最小值
    plt.show()

minValue=gradient_descent_1d(cur_x=1, learn_rate=0.2, e=0.0001,count=10)
minY=f(minValue)
print('目标函数f(x)的最小值约是',minY)
ShowLine(minValue,minY)