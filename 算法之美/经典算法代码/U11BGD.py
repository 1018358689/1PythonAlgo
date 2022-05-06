# -*- coding: utf-8 -*-
"""
  Created on Fri Feb 21 11:59:01 2020
  批量梯度下降算法
  @author: 刘瑜
  源代码文件是：U11BGD.py
"""
import matplotlib.pyplot as plt
x=[[1],[1],[2],[3],[5],[5],[6],[7],[8],[9],[10],[10]]
y =[[2.1],[2.8],[3.5],[4.8],[3.5],[5.2],[4.2],[6],[7.2],[9],[12.5],[11]]
plt.plot(x,y,'o')          #绘制所有样本数的散点图
'''
#批量梯度下降函数BGD_a(),参数r为步长，经验值，需要合理调试，否则预测线可能出错
三种终止梯度下降迭代方法：
1、E为前后损失函数值差的阈值，小于E可以终止迭代
2、为最大迭代次数，超过该值迭代终止
3、当损失函数值小于设定值t时，也可以终止迭代
'''
def BGD_a(x,y,r=0.001,E=0.01,MaxCount=30,t=0.05):             
    m=len(x)                #样本数量
    t0=0                    #假设函数初始值0
    d1=0                    #梯度初始值0
    count=0                 #统计迭代次数
    next_error=0            #记录下一个误差值
    while True:
        count=count+1
        grad=[0,0]          #记录迭代过程目标函数值、梯度值
        er=0                #损失函数初始值
        for i in range(m):   #对所有样本数据求梯度
            grad[0]+=t0+d1*x[i][0]-y[i][0]    #求所有样本的假设函数值
            grad[1]+=(t0+d1*x[i][0]-y[i][0])*x[i][0] #求所有样本的梯度
        t0=t0-r/m*grad[0]    #新的假设函数值的迭代公式
        d1=d1-r/m*grad[1]    #新的梯度下降的迭代公式
        for i in range(m):
            er+=1/(2*m)*((t0+d1*x[i][0]-y[i][0])**2)#求所有样本的损失函数值和
        if abs(next_error-er)<E:  #前后损失函数值差的距离是否小于阈值E
            print('超过误差设置阈值%f，终止迭代！'%(E))  #终止迭代
            break;
        if count>MaxCount:
            print('超过最大迭代次数%d，终止迭代！'%(count))  #终止迭代
            break;
        if er<t:     #所有样本迭代损失函数值小于设定值时，也可以终止迭代
            print('超过所有样本迭代损失函数值设定的最小值%f，终止迭代！'%(t))
            break
        next_error=er
    print('最后一次迭代，损失函数值1:%f,梯度值:%f,error:%f'%(t0,d1,er))
    print('迭代次数：',count)
    return t0,d1        #返回迭代的最后一个损失函数值、梯度值
x2=[x[0][0],x[-1][0]]         #获取x轴首尾两个值
t0,d1=BGD_a(x,y,r=0.002)    #调用BGD算法函数
y2=[t0+d1*x2[0],t0+d1*x2[1]] #获取y轴首尾两个值
def showBGD(x,y):            #显示梯度下降预测线
    plt.plot(x,y)            #梯度下降预测线
    plt.show()
showBGD(x2,y2)
