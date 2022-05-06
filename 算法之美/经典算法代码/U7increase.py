# -*- coding: utf-8 -*-
"""
  Created on Sun Dec 15 10:27:20 2019
  累加递归
  @author: 刘瑜
  源代码文件是：U7increase.py
"""
def increase(n=3):                  #定义累加递归函数
    if n==1:                        #当n=1时，返回最小值1，开始出栈
        return 1
    else:
        return n+increase(n-1)      #n不等于1时，压栈，在临时地址存储
print('递归结果：%d'%(increase(3)))  #递归调用，并打印结果，2957溢出
