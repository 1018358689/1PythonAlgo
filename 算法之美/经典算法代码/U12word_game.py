# -*- coding: utf-8 -*-
"""
   Created on Sun Mar  8 10:18:50 2020
   回溯法求3*3，所有相邻两数和为素数的游戏解
   所填写数字在1到16中选择，且每个数字不允许重复
   @author: 刘瑜
   源代码文件是：U12word_game.py
"""
import copy
def isPrime(number):     #**判断是否是素数
    i=2
    half=number//2+1                        #截取一半+1进行素数判断即可
    while i<half:                            #判断是否是素数
        if number%i==0:
            return 0                        #非素数
        i+=1
    return 1                                #素数
def printCb(cb):                            #**打印最后结果
    for one in cb:                          #输出一个答案
        print(one)
def Cross(cb,r,c,index):#**判断在棋盘里的比较方向，index=1为左边，-1为上边，0为左边上边
    if index==1:                            #左边方向判断是不是素数
        if isPrime(cb[r][c-1]+cb[r][c])==0: #不是素数
            return False                    #条件不符合
    elif index==-1:                         #上边方向判断是不是素数
        if isPrime(cb[r-1][c]+cb[r][c])==0: #不是素数
            return False                    #条件不符合
    else:                                   #上边、左边方向都判断，是不是素数
       if isPrime(cb[r-1][c]+cb[r][c])==0 or isPrime(cb[r][c-1]+cb[r][c])==0 : #不是素数
            return False                    #条件不符合 
    return True                             #条件符合
def go(row,col,index,num,m): #**控制棋盘里的坐标走向，并进行素数判断
    flag=True
    if row==0 and col==0:
        cb[0][0]=num[index]
        col+=1                              #向右一步
    elif row==0 and (col>0 and col<m):      #第1行比较
        cb[row][col]=num[index]             #尝试测试新数字
        if Cross(cb,row,col,1):             #第1行，1为比较左边符合要求
            col+=1
            if col==m:
                row+=1
                col=0
        else:
            flag=False                      #当前节点不符合要求
    elif col==0 and (row>0 and row<m):      #非第1行，但是第1列情况下比较
        cb[row][col]=num[index]
        if Cross(cb,row,col,-1):            #-1仅比较上一行    
            col+=1
        else:
            flag=False                      #当前节点不符合要求
    elif (col>0 and col<m) and (row>0 and row<m): #非第1行，也非第1列的情况
        cb[row][col]=num[index] 
        if Cross(cb,row,col,0):             #0为上一行，左一行都比较    
            col+=1
            if col==m:
                row+=1
                col=0
        else:
            flag=False                     #当前节点不符合要求
    return flag,row,col
    
checkerboard=[[0,0,0],
              [0,0,0],
              [0,0,0]]

def WordGame(cb,num,row=0,col=0,index=0):  #**开始填字
    back=-1
    m=len(cb)
    n=len(num)
    if cb[2][2]!=0:
        return 0                             # 找到一个答案
    while index<n:
        #print('row=%d,col=%d,index=%d'%(row,col,index))
        flag,row,col=go(row,col,index,num,m) #控制棋盘里的走向，并判断是否是素数
        if flag :                            #当前节点符合要求
            if row<m and col<m:              #都在棋盘范围内
                index+=1
                back=WordGame(cb,num,row,col,index)  #找下一个
                if back==0:                 #找到一个答案
                    break
            else:
                return -1
        else:                               #当前节点不符合要求
            if row<m:
                if index==n :               #数字用完
                    index=row*3+col+1       #当前坐标+1
                    cb[row][col]=0          #回溯
                else:                       #在当前试探基础上，继续试探下一个
                    index+=1                #试探范围[index+1,n-1]
                    if index<n:
                        cb[row][col]=num[index]
            else:
                return -1
    return back
i=0
numb=[i for i in range(1,16)]              #可以填写的数字列表,本案例i>=16,否则无解
ma=len(numb)
cb=copy.deepcopy(checkerboard)             #深度拷贝数字列表
print(numb)
while i<ma:       
    v=WordGame(cb,numb,0,0)                #开始填字，求解
    numb=numb[1:]+[numb[0]]                #一轮数组走完，准备第二轮数字，采用循环
    i+=1                                   
    if v==-1:
        print('第%d轮无解:'%(i))
        #printCb(cb)
    elif v==0:
        print('第%d轮有解:'%(i))
        printCb(cb)                        #输出找到了每轮第一个解
    cb=copy.deepcopy(checkerboard)
