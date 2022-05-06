# -*- coding: utf-8 -*-
"""
  Created on Thu Mar  6 20:55:10 2020
  回溯算法求八皇后问题
  @author: 刘瑜
  源代码文件是：U12queen8.py
"""
count=0
dec=0

def queen8(solution,cur=0,length=8):#solution记录已经放入的皇后位置,cur记录第几个皇后
    if cur ==length:              #8个皇后数量都摆齐了,给出一个答案 
        print(solution)
        global count
        count+=1                  #统计找到的答案数量
        return -1
    for col in range(length):     #从0列开始对所有列进行比较,棋盘的列长度为8
        solution[cur]=col         #从第cur行开始,对当前列进行比较,cur记录最后皇后放入列表时的位置
        OK=True
        for row in range(cur):    #比较已选皇后之间的冲突，在第cur列情况下,对0到cur-1行进行比较
            if solution[row]==col or abs(col-solution[row])==cur-row: #行相等或在对角线上*
                OK= False
                break
        if OK:                    #如果当前放入的皇后不冲突,则继续找下一个皇后放入的位置
            queen8(solution,cur+1)#递归找下一个皇后的位置
    if not OK and count==1:
        global dec
        dec+=1
        print('抛弃次数%d'%(dec))
solution=[None]*8                 #对应记录已经放入的皇后位置(行位置),列表索引对应棋盘的列
queen8(solution)
print('总共找到了%d个答案'%(count))
#*solution列表里最多只能一行最多只能出现一次，在棋盘里一行行往下比较，
#由于列表solution每列只存入一个唯一位置的值，找一个追加一个，所以每列确保唯一，不冲突。
#cur在比较时除了记录皇后顺序外，还可以用作棋盘上的行、列索引，因为比较是行列索引值对称的。