# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:59:01 2020
    批量梯度下降算法
@author: 刘瑜
"""
import matplotlib.pyplot as plt
import numpy as np
# -*- coding: UTF-8 -*-

import numpy as np
import math

# 定义基础变量
learning_rate = 0.1
n_iterations = 10000
m = 100

x = 2 * np.random.rand(m, 1)  # 生成一组服从0~1均匀分布的随机样本，此处表示生成100行一列的二维数组，下同
y = 4 + 3 * x + np.random.randn(m, 1)  # 正态分布
x_b = np.c_[np.ones((m, 1)), x]  # np.((100, 1)):表示生成100行1列的矩阵，内部填充为1

# 设置阈值
threshold = 0.15
# 1，初始化theta，w0...wn
theta = np.random.randn(2, 1)
count = 0
before_value = 1
# 4，设置阈值，之间设置超参数，迭代次数，迭代次数到了或者满足阈值，我们就认为收敛了
for iteration in range(n_iterations):
    count += 1
    # 2，接着求梯度gradient
    gradients = 1/m * x_b.T.dot(x_b.dot(theta)-y)  # 求平均梯度
    print('平均梯度：',gradients)
    # 3，应用公式调整theta值，theta_t + 1 = theta_t - grad * learning_rate
    theta = theta - learning_rate * gradients
    # 判断是否满足阈值
    mid = math.sqrt(math.pow((theta[0][0] - 4), 2) + math.pow((theta[1][0] - 3), 2))
    if mid <= threshold:
        print('总共执行{}次迭代，可知迭代次数设置过大，建议适当减小！'.format(count))
        break
    # 若与上一次的中间结果比较差值过小也同样结束循环
    err = math.fabs(mid - before_value)
    if err < 0.001:
        if before_value > threshold:
            print('多次迭代都不能满足阈值，请修改阈值或重新处理数据！')
            break
        else:
            print('总共执行{}次迭代，可知迭代次数设置过大，建议适当减小！'.format(count))
            break
    # 暂时保存上一次的中间结果
    before_value = mid
print('迭代次数：',count)
print('结果：\n x is : {}\n y is : {}\n 误差 : {}'.format(theta[0][0], theta[1][0], before_value))
'''
—https://www.cnblogs.com/yszd/p/9255495.html
'''