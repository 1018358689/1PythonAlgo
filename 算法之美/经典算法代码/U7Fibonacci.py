# -*- coding: utf-8 -*-
"""
  Created on Sun Dec 29 14:43:22 2019
  用递归函数求斐波那契数列
  @author: 刘瑜
  源代码文件是：U7Fibonacci.py
"""

def solve_fibona(n):
   if n <= 1:
       return n
   else:
       return(solve_fibona(n-1) + solve_fibona(n-2))

n=10
print('%d斐波那契数列为：'%(n))
for i in range(1,n+1):
    print(solve_fibona(i))