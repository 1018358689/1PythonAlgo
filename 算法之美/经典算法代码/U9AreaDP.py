# -*- coding: utf-8 -*-
"""
  Created on Thu Jan 16 09:06:12 2020
  区域动态规划，石子归并
  @author: 刘瑜等
  源代码文件是：U9AreaDP.py
"""
#stones=[4,5,6,7]           #每堆石子数量
stones=[7,6,5,7,100]           #每堆石子数量
n=len(stones)              #n堆石子

dp=[[0]*n for _ in range(n)]#初始化存放最优求解过程的二维列表dp[n,n],其值都为0

def StonesSum(substones):   #传递需要累加的子stones
    return sum(substones)  #返回子问题的石子总数

def StonesDP(stone):
    i=1
    while i<n:
        j=0
        while j<n and (j+i)<n:
            k=j
            while k<j+i:
                curCost=dp[j][k]+dp[k+1][j+i]+StonesSum(stone[j:(j+i+1)]) #当前子问题合并后的解（成本）
                print('i=%d j=%d 当前解是%d,当前石子累加%d'%(i,j,curCost,StonesSum(stone[j:(j+i+1)])))
                if dp[j][j+i]==0:
                    dp[j][j+i]=curCost                   #同一子问题第一个解
                else:
                    dp[j][j+i]=min(dp[j][j+i],curCost)    #同一子问题不同解里取最优解（最小解）
                k+=1          #控制不同子问题的求解次数，如2，5，3，求解两个解（第1解为15，第2解为18）
            j+=1             
        i+=1    
StonesDP(stones)
for line in dp:
    print(line)