# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 23:01:18 2020

@author: 111
"""
def combination_k(s, k):
    if k == 0: return ['']
    # recursive chain
    subletters = []
    # 此处涉及到一个 python 遍历循环的特点：当遍历的对象为空（列表，字符串...）时，循环不会被执行，range(0) 也是一样
    for i in range(len(s)):
        for letter in combination_k(s[i+1:], k-1):
             subletters += [s[i] + letter]
    return subletters
s=combination_k('+-*/',3)
print(s)