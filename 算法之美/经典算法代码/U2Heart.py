# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 17:13:19 2019
笛卡尔心形
@author: 刘瑜等
源代码文件：U2Heart.py
"""
import matplotlib.pyplot as plt     #导入matplotlib第三方绘图库
import numpy as np                  #导入numpy第三方科学计算库

x= np.linspace(0, 2*np.pi,500)      #0到2π范围内均匀取500个值
a=6
rho =a*(1-np.sin(x))                #笛卡尔心形公式
plt.subplot(polar=True)             #设置为极坐标
plt.plot(x, rho, c='r')             #绘制红色的心形图
plt.text(0,0,'Love You!',color='m') #标注“Love You!”
plt.show()                          #显示绘制结果