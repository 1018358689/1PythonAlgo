# -*- coding: utf-8 -*-
"""
  Created on Tue Sep 10 19:41:07 2019
  BM字符串搜索算法
  @author: 刘瑜等
  源代码文件是：U6BM.py
"""

def BoyerMooreHorspool(keys, text):
    m = len(keys)                  #模式串
    n = len(text)                  #文本串
    if m > n: return -1            #文本串长度小于模式串，结束检索
    skip = []
    for k in range(256):           #
        skip.append(m)
    for k in range(m - 1): 
        skip[ord(keys[k])] = m - k - 1
    skip = tuple(skip)
    k = m - 1
    while k < n:
        j = m - 1; i = k
        while j >= 0 and text[i] == keys[j]:
            j -= 1;
            i -= 1
        if j == -1: 
            return i + 1
        k += skip[ord(text[k])]
    return -1

if __name__ == '__main__':
    text = "this is the string to search in"
    keys = "the"
    s = BoyerMooreHorspool(keys, text)
    print('Text:',text)
    print('Pattern:',keys)
    if s > -1:
        print('Pattern \"' + keys + '\" found at position',s)
