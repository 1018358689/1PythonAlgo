# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:55:44 2020

@author: 111
"""

a=[7,6,5,7,100]
n=len(a)+1
s=[[0]*n for i in range(n)]
p=[[0]*n for i in range(n)]
for i in range(1,n):
    s[i][i]=a[i-1]
for i in range(1,n):
    for b in range(1,n-i):
        c=b+i
        for d in range(b,c):
            s[b][c]=s[b][d]+s[d+1][c]
            if p[b][c]==0:
                p[b][c]=p[b][d]+p[d+1][c]+s[b][c]
            else:
                p[b][c]=min(p[b][c],p[b][d]+p[d+1][c]+s[b][c])
print(p[1][c])  