# -*- coding: utf-8 -*-
"""
  Created on Tue Mar 10 21:20:13 2020
  求24点游戏
  @author:刘瑜
  源代码文件是：U12game24.py
"""
import random
import copy
cards=[i for i in range(1,14)]
cards=cards*4               #4种花色的牌子，去掉大王、小王
print('一副扑克牌的参与24点计算的牌：\n',cards)
n=len(cards)
def randomCard4(cards):    #随机抽取4张牌
    points=[]
    index=random.sample(range(1,n),4)  #随机抽四张
    for i in index:
        points.append(cards[i])
    return points

def perm(numbers, position, end,s): #全排列组合
    if position == end:
        #global solution
        return numbers
        #print(numbers)
    else:
        for index in range(position, end): 
            numbers[index],numbers[position] =numbers[position],numbers[index]#交换两比较数
            r=perm(numbers, position+1, end,s)                                    #递归进行下一个数在子范围内的排序
            if r!=None:
                s.append(copy.deepcopy(r))                                   #递归进行下一个数在子范围内的排序
            numbers[index],numbers[position] =numbers[position],numbers[index] #递归,每一步恢复原先状态
    return 

def operator():
    p=[]
    op=['+','-','*','/']
    perm(['+','-','*'],0,3,p)  
    perm(['+','-','/'],0,3,p)
    perm(['+','/','*'],0,3,p) 
    perm(['/','-','*'],0,3,p)
    i=0
    n=len(op)
    while i<n:
        j=0
        while j<n:
            if i!=j:
                p.append([op[i],op[i],op[j]])
                p.append([op[j],op[i],op[i]])
                p.append([op[i],op[j],op[i]])
            j+=1
        p.append([op[i]]*3)           
        i+=1
    return p
#print(operator())
def twoCalcu(one,two,op):
    if op=='+':
        return one+two
    elif op=='-':
        return one-two
    elif op=='*':
        return one*two
    else:
        return one/two
def perm_card4(rc4):#4只牌的全排列组合
    c=[]
    perm(rc4,0,4,c) #4只牌进行全排列组合
    return c

def Calculation24(cards4,op3): #计算24点
    cds4=perm_card4(cards4)
    #print('4张牌组合：\n',cds4)
    #print('计算符号组合：\n',op3) 
    for one_c in cds4:     #取出4只牌的组合
        for one in op3 :  #取运算符号一个组合
            r1=twoCalcu(one_c[0],one_c[1],one[0]) #计算第一对数字
            r1=twoCalcu(r1,one_c[2],one[1])    #计算第二对数字
            r1=twoCalcu(r1,one_c[3],one[2])    #计算第三对数字
            #print(r1)
            if r1==24 :
               return str(cards4)+'是一组解'  
    return str(cards4)+'无解'
def game24():
   n=4    #抽取次数
   print('一次随机抽取4张，抽%d四次，进行24点计算：' %(n))
   for i in range(n): #连续出4次牌
       rc4=randomCard4(cards)
       op3=operator()
       v=Calculation24(rc4,op3)
       print(v)
game24()        
          
        
        
        