# -*- coding: utf-8 -*-
"""
   Created on Sun Jan 19 16:27:02 2020
   背包动态规划
   @author: 刘瑜
   源代码文件是:U9DP_Bag.py
"""
vol_max=5   #背包最大可以装载体积
values=[20,10,15,25] #物品价值
volumes=[3,1,2,4]     #蛋糕对应的体积

def bagValue(volume,value,m):
    i_len=len(volume) #物品数量
    dp=[[0]*(m+1) for _ in range(i_len)] #值都为0的4行、6列二维列表
    for j in range(1,m+1): #处理i=0行时的解
        if volume[0]<=j:
            dp[0][j]=value[0] #第一个蛋糕能装进去，就赋值第一个蛋糕的价值
    for i in range(1,i_len): #处理1到3行的物品
        for j in range(1,m+1): #处理每行的1到5列的最优解
            if j<volume[i]:   #如果蛋糕装不下
               dp[i][j]=dp[i][j-1] #上一行对应的价值赋给当前值
            else:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-volume[i]]+value[i])
    for line in dp:
        print(line)
    return dp[-1][-1]

Solve=bagValue(volumes,values,vol_max)
print('在空间为%d的包里最多可以放价值为%d的蛋糕'%(vol_max,Solve))
'''
import numpy as np
def bag(weight,values,weight_cont):
    num = len(weight)
    weight.insert(0,0)
    values.insert(0,0)
    bag = np.zeros((num+1,weight_cont+1),dtype=np.int)
    for i in range(1,num+1):
        for j in range(1,weight_cont+1):
            if j >= weight[i]:
                bag[i][j] = max(bag[i-1][j],bag[i-1][j-weight[i]]+values[i])
            else:
                bag[i][j] = bag[i][j-1]
    return bag[-1][-1]
if __name__ == '__main__':
    weight = [1, 2, 4, 10, 12]
    values = [1200, 1500, 2000, 1300, 2500]
    weight_cont = 20
    re = bag(weight,values,weight_cont)
    print(re)
'''
