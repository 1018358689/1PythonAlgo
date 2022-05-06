# -*- coding: utf-8 -*-
"""
   Created on Sat Jan 18 19:19:03 2020
   数字三角形动态规划算法
   三角形值限制在非负整数
   输出最小路径最优解
   @author: 刘瑜
   源代码文件是：L9triangleDP.py
"""
triangle=[
           [5],
          [2,3],
         [5,6,3],
        [6,1,2,4]
         ]
def minPath(t1):
    dp=[]   #存放动态规划过程最优解
    for row in t1:
        dp.append([0]*len(row))  #初始化dp值都为0
    n=len(dp)

    dp[0][0]=t1[0][0]    #第一个节点的最优解就是其本身
    for i in range(n-1):
        len1=len(t1[i][:])
        for j in range(len1): #i层的长度
            if dp[i+1][j]==0 and j==0:  #父节点（i,0）,i+1层左边第一个节点值为0
                dp[i+1][j]=dp[i][j]+t1[i+1][j]  #i+1子左节点
                dp[i+1][j+1]=dp[i][j]+t1[i+1][j+1] #i+1子右节点
            else:                               #父节点（i,j>0）
                dp[i+1][j]=min(dp[i+1][j],dp[i][j]+t1[i+1][j])#父亲节点的左子节点
                dp[i+1][j+1]=dp[i][j]+t1[i+1][j+1]              #父亲节点的右子节点 
    
    print('最后一层最优解记录：'+str(dp[n-1]))
    minValue=dp[n-1][0]
    bottomLength=len(dp[n-1])
    f=1
    while f<bottomLength:
        if minValue> dp[n-1][f]:
           minValue=dp[n-1][f]
        f+=1
    print('三角形最小路径最优解为%d'%(minValue))
    return dp,minValue #返回最优解列表和最优解,***求最小路径代码修改开始位置
r,minValue=minPath(triangle)
print(r)
h=len(triangle)-1
Value=triangle[h][r[h].index(minValue)]
mPath=[Value,]
while h>0:
    i=triangle[h].index(Value)                  #获取当前层最优解的下标
    h-=1
    if h>0:
        if i==0:                                #当层最左边情况
           Value=triangle[h][0]
        elif i+1==len(triangle[h]):             #当层最右边情况
           Value=triangle[h][-1]
        else:                                   #中间位置
            if triangle[h][i-1]<triangle[h][i]: #上一层左边值小
                Value=triangle[h][i-1]
            else:
                Value=triangle[h][i]            #上一层右边值小
    else:   #根节点
        Value=triangle[0][0]
    mPath.insert(0,Value) #把最小路径上的节点找出来
print('原始三角形数值：',triangle)    
print('该三角形最优解的最小路径是：',mPath)        