# -*- coding: utf-8 -*-
"""
  Created on Thu Jan  2 19:31:22 2020
  求斐波那契数列递归算法改进
  @author: 刘瑜
  源代码文件是：U7Fibonacci_Good.py
"""
def solve_fibona1(n):
   if n <= 1:
       return (n,0)
   else:
       f1,f2=solve_fibona1(n-1)
   return(f1+f2,f1)
n=5
print('%d斐波那契数列为：'%(n))
for i in range(1,n+1):
    print(solve_fibona1(i)[0])