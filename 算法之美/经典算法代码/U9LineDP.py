# -*- coding: utf-8 -*-
"""
   Created on Sat Jan 11 19:25:54 2020
   线性动态规划求最长升序子字符串
   @author: 刘瑜等
   源代码文件是：U9LineDP.py
"""
txt1=['A','B','C','A','B','C','D','E','F','E','O','T']
dp=[1,]
len1=len(txt1)
j=0
max1=1
while j<len1-1:
    if txt1[j]<txt1[j+1]:
        dp.append(dp[j]+1)
        if dp[-1]>max1:
            max1=dp[-1]
    else:
        dp.append(1)
    #print(txt1[j+1])
    j+=1
print('最大子串长度为：%d'%(max1))