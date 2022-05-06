# -*- coding: utf-8 -*-
"""
  Created on Sun Sep 15 09:28:37 2019
  前缀表达式
  @author: 刘瑜
  源代码文件是：L6FSuffix.py
"""
def Suffix(arr):
    Stack=[]   #装运算符和左右小括号
    L=[]       #装前缀式
    for value in arr:
        if value=='(':
            Stack.append(value)
        elif value==')':
            S_n=len(Stack)-1
            while S_n!=-1 and Stack[S_n]!='(':
                L.insert(0,Stack.pop())
                S_n-=1
            if Stack!=[]:
                Stack.pop()            #去掉(
        elif ord(value)>=48 and ord(value)<=57:  #0到9的数值，ord()取字符的ASCII码，0的ASCII码位48，9的ASCII码位57
            L.insert(0,value)
        else:  #判断是运算符号,仅限于+，-，*，/
            S_n=len(Stack)-1
            while S_n!=-1 and Stack[S_n]!='(':
                if Stack[S_n]=='*' or Stack[S_n]=='/':
                    if value=='-' or value=='+':    #value为-或+
                        L.insert(0,Stack.pop())
                else:
                    break
                S_n-=1
            Stack.append(value)
        print('当前元素%s，前缀表达式%s,栈状态%s'%(value,L,Stack))
    while Stack!=[]:
        L.insert(0,Stack.pop())
    return L

#formula='3/(4+3*8)'
#formula='(1+2)*((3-4)*(5-6))'
#formula='7+4*2-3+6'
formula='7+(4*2-3+6/2)'
L=Suffix(formula)
print('前缀表达式',L)
           
           
