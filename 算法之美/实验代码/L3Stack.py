# -*- coding: utf-8 -*-
"""
  Created on Tue Mar  24 19:09:55 2020
  处理公式
  @author: 刘瑜等
  源代码文件是：U3Stack.py
"""
def Formula(F):
    Stack=[]
    b=0
    p=0
    for one in F:          #入栈过程
        
        if one=="(":
            p=b     
        if one==')':
            V=OutStack(Stack[p+1:b])
            Stack=Stack[0:p]
            Stack.append(V)
            print('Go',Stack,V)
        else:
            Stack.append(one)
        b+=1
    OutStack(Stack)
    return Stack
def OutStack(S):      #从栈里出来
    print(S)
    i=1
    n=len(S)
    while i<n-1:
        if S[i]=="*":
            S[i-1]=str(float(S[i-1])*float(S[i+1]))
            S.pop(i+1)
            S.pop(i)
            n-=2
        elif S[i]=='/':
            S[i-1]=str(float(S[i-1])/float(S[i+1]))
            S.pop(i+1)
            S.pop(i)
            n-=2
        else:
            i+=1
        print(i,n,S)
    i=0
    while i<n-1:
        if S[i]=="+":
            S[i-1]=str(float(S[i-1])+float(S[i+1]))
            S.pop(i+1)
            S.pop(i)
            n-=2
        elif S[i]=='-':
            print('%s'%(str(float(S[i-1])-float(S[i+1]))))
            S[i-1]=str(float(S[i-1])-float(S[i+1]))
            S.pop(i+1)
            S.pop(i)
            n-=2
        else:
            i+=1
    print('End:',S)        
    return S[0]

#code='3+5*(9-2)/2'      #数字控制在1到9之间
code='3+5*(9-2+5)/2'     #若小括号嵌套还需要完善代码
V=Formula(code)
print(code,'=',V)
