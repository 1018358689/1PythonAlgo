# -*- coding: utf-8 -*-
"""
  Created on Sun Sep 15 14:33:56 2019
  判断是否回文算法
  @author: 刘瑜、阚伟
  源代码文件是：U6Palindrome.py
"""
def Palindrome(arr):
    n=len(arr)
    i=0
    mid=n//2
    while i<mid:
        if arr[i]!=arr[n-i-1]:
            mid=-1
        i+=1
    if i==mid :
        return True
    else:
        return False
s1='abcdcba'
#s1='abcddcbd'
if Palindrome(s1):
    print('OK！是回文')
else:
    print('No!不是回文')
    
            
        