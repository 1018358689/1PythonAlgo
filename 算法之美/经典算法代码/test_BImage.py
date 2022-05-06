# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 20:02:18 2019

@author: 111
"""

import numpy as np
import matplotlib.pyplot as plt    #导入pyplot模块
img=plt.imread(r'G:\2019年FiveBook视频计划兼算法书\算法图片\hbtu.jpg') #读取指定路径下的PNG图片
plt.imshow(img)                                        #显示图片
print(img)                                             #打印img数组
print(type(img))                                       #输出是数组类型
print(img.shape)                                       #输出图片大小