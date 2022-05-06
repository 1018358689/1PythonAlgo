# -*- coding: utf-8 -*-
"""
  Created on Wed Dec  4 19:09:55 2019
  二值图像处理
  @author: 刘瑜等
  源代码文件是：U3BinImage.py
"""
import matplotlib.pyplot as plt    #导入pyplot模块
img=plt.imread(r'G:\2019年FiveBook视频计划兼算法书\算法图片\jfm.jpg') #读取指定路径下的PNG图片
plt.imshow(img)                                        #显示图片
#print(img)                                             #打印img数组
print(type(img))                                       #输出是数组类型
print(img.shape)                                       #输出图片大小
#print(img[2000:2500,500:1000,:])                       #观察加菲猫白色部分的数值
hight,width,length=img.shape                           #获取图片的高、宽，像素点值
img1=img.copy()
for h in range(hight):
    for w in range(width):
        for l in range(length):
            if img1[h,w,l]>=127:                       #大于255/2
                img1[h,w,l]=255                        #白色
            else:
                img1[h,w,l]=0                           #黑色
plt.imshow(img1)                                        #显示图片