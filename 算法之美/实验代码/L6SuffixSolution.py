# -*- coding: utf-8 -*-
"""
  Created on Wed Apr  1 19:35:01 2020
  逆波兰公式转为实际计算
  @author: 刘瑜
  源代码文件是：L6SuffixSolution.py
"""
def SuffixS(formula):
    i=0
    Stack=[]
    length=len(formula)
    while i<length :
        if formula[i]=='*':
           Stack.append(Stack.pop(-1)*Stack.pop(-1))
        elif  formula[i]=='/':
            D=Stack.pop(-1)              #分母
            Stack.append(Stack.pop(-1)/D)
        elif formula[i]=='+' :
            Stack.append(Stack.pop(-1)+Stack.pop(-1))
        elif formula[i]=='-':
            Stack.append(Stack.pop(-1)-Stack.pop(-1))
        else:
            Stack.append(int(formula[i]))   #数字进栈
        i+=1
    print('最终计算结果是:',Stack[0])
SuffixS(['3', '4', '3', '8', '*', '+', '/'])