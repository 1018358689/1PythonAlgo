# -*- coding: utf-8 -*-
"""
  Created on Sat Mar 28 22:21:40 2020
  回溯查找
  @author: 刘瑜等
  源代码文件是：U5Backtracking.py
"""
def FindNext(m,record,r,c):    #判断当前节点的下一个节点解
    n=len(m)
    if (c+1<n):                #在n范围内，
        if record[r][c+1]==0:  #试探往右走,且没有走过的
            if m[r][c+1]==1:   #可行，标记1 
                record[r][c+1]=1
                return r,c+1   #返回新坐标
        else:                  #已经走过
            b_r,b_c=r,c+1      #记录上一个走过的坐标
    if r+1<n:
        if record[r+1][c]==0:  #在n范围内，试探往下走
            if m[r+1][c]==1:   #可行，标记1 
                record[r+1][c]=1
                return r+1,c   #返回新坐标
        else:                  #已经走过
            b_r,b_c=r+1,c      #记录上一个走过的坐标
    if r-1>=0:
        if record[r-1][c]==0:  #在n范围内，试探往左走
            if m[r-1][c]==1:   #可行，标记1 
                record[r-1][c]=1
                return r-1,c   #返回新坐标
        else:                  #已经走过
            b_r,b_c=r-1,c      #记录上一个走过的坐标
    if c-1>=0:
        if record[r][c-1]==0:  #在n范围内，试探往上走
            if m[r][c-1]==1:   #可行，标记1 
                record[r][c-1]=1
                return r,c-1   #返回新坐标
        else:                  #已经走过
            b_r,b_c=r,c-1      #记录上一个走过的坐标
    m[r][c]=0                  #走不通的路设置maze当前节点设置0，回溯
    if r+1==n and m[r][0]==0:  #在最后一行情况下，如果回溯到r,0位置
        print(r,c)
        b_r,b_c=r+1,0          #准备所有试探回溯都结束
    return b_r,b_c             #返回走不通节点的前一节点坐标

def solution_maze(m,record):
    row,col=0,0
    n=len(m)                   #长度
    i=0
    while i<n:
        if m[i][0]==1:
            row=i              #求得初始行
            record[i][0]=1       #标值走过
            break
        i+=1
    if i==n-1:
        print('第1列无入门地方，终止执行！')
    while i<n:
        if (row<n and row>=0) and (col<n and col>=0): #当前坐标在范围之内
            if col==n-1:
                for one in record:
                    print(one)  #打印最后结果
                return 1
            row,col=FindNext(m,record,row,col)        
            if col==0:          #回溯到开始位置
                i+=1            #从下一行开始求解
                row=i
    return 0
if __name__ == '__main__': 
    maze = [[0, 1, 0, 1, 1, 1, 1, 1, 0],
            [1, 1, 0, 1, 0, 1, 0, 1, 1],
            [0, 1, 1, 1, 0, 1, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 1, 1, 1],
            [0, 0, 1, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0, 1],
            [0, 1, 1, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 1]]           
    n=len(maze)
    recordPath=[([0]*n) for _ in range(n)] 
    solution_maze(maze,recordPath)

