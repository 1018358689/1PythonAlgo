# -*- coding: utf-8 -*-
"""
   Created on Sat Feb 22 16:37:41 2020
   随机梯度下降算法
   @author: 刘瑜
   源代码文件是：U11SGD.py
"""
import random
import matplotlib.pyplot as plt
x=[[1],[1],[2],[3],[5],[5],[6],[7],[8],[9],[10],[10]]
y =[[2.1],[2.8],[3.5],[4.8],[3.5],[5.2],[4.2],[6],[7.2],[9],[12.5],[11]]
plt.plot(x,y,'o')           #绘制所有样本数的散点图

def SGD(x,y,r=0.002,countMax=50,T=0.00001):#随机批量下降,r为步长，countMax迭代最大次数,T收敛阈值
    m=len(x)
    count=0          #迭代统计变量
    Next_er=0        #损失函数初始值
    er0=0            #损失函数初始值
    g1=0             #梯度初始值
    w=[0,0]          #记录迭代过程损失函数值、梯度值
    while True:
        i=random.randint(0,m-1)  #随机选取一个样本数下标
        count+=1
        w[0]=er0+g1*x[i][0]-y[i][0]  #损失函数(部分)
        w[1]=(er0+g1*x[i][0]-y[i][0])*x[i][0] #梯度
        er0=er0-r*0.5*w[0]**2        #损失函数值迭代公式
        g1=g1-r*w[1]                 #梯度迭代公式
        if abs(Next_er-er0)<T:       #小于收敛阈值
            break
        if(count>countMax):         #大于迭代次数
            break
        Next_er=er0
    print('迭代最后损失函数值%f,最后梯度值%f,迭代次数%f'%(er0,g1,count))
    return er0,g1
x2=[x[0][0],x[-1][0]]              #获取x轴首尾两个值
t0,d1=SGD(x,y,countMax=100)        #调用SGD算法函数
y2=[t0+d1*x2[0],t0+d1*x2[1]]       #获取y轴首尾两个值
def showBGD(x,y):                  #显示梯度下降预测线
    plt.plot(x,y)                  #梯度下降预测线
    plt.show()
showBGD(x2,y2)