# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 20:53:20 2020

@author: 111
"""
# -*- coding: utf-8 -*-
"""
  Created on Thu Jan  2 19:31:22 2020
  求兔子12个月的总只数
  @author: 刘瑜
  源代码文件是：U7Rabbit.py
"""
def solve_fibona1(n):
   if n <= 1:
       return (n,0)
   else:
       f1,f2=solve_fibona1(n-1)
   return(f1+f2,f1)
n=12
print('%d个月兔子共有：'%(n))
for i in range(1,n+1):
    print(solve_fibona1(i)[0])
