# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:00:02 2020

@author: 111
"""

# coding=utf-8

class Maze():
    # 初始化迷宫的规格大小
    def __init__(self, n):
        self.n = n
        # 初始化结果矩阵
        self.flag = [[0 for _ in range(n)] for _ in range(n)]

    # 判断位置是否合法，如果可以走，那么返回True，否则返回False
    def isSafe(self, maze, x, y):
        return x >= 0 and x <= self.n - 1 and y >= 0 and y <= self.n - 1 and maze[x][y] == 1

    # 打印矩阵
    def printSolution(self, flag):
        for i in flag:
            for j in i:
                print('%4s' % str(j), end='')
            print('\n')

    # 获取走出迷宫的结果矩阵
    def getPath(self, maze, x, y):

        # 如果此处位置合法但是此处走过了，返回到上一步
        if self.isSafe(maze, x, y) and self.flag[x][y] == '-':
            return False

        # 如果到达了目的地，返回True
        if x == self.n - 1 and y == self.n - 1:
            self.flag[x][y] = '-'
            self.printSolution(self.flag)
            return True

        # 没有到达目的地，继续往下走
        if self.isSafe(maze, x, y):

            # 标记结果矩阵中当前位置为*（*表示行走的路线）
            self.flag[x][y] = '-'

            # 尝试向右走，递归
            if self.getPath(maze, x + 1, y):
                return True

            # 尝试向下走，递归
            if self.getPath(maze, x, y + 1):
                return True

            # 尝试向左走，递归
            if self.getPath(maze, x - 1, y):
                return True

            # 尝试向上走，递归
            if self.getPath(maze, x, y - 1):
                return True

            # 此路不通，标记当前的单元为0，表示此处不可能到达目的地，返回上一步
            self.flag[x][y] = 0
            return False

        # 此位置不合法，返回False
        return False


if __name__ == '__main__':
    maze = [[1, 1, 0, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 1],
            [0, 1, 1, 1, 0, 1, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 1, 1, 1],
            [0, 0, 1, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0, 1],
            [0, 1, 1, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 1], ]

    rat = Maze(len(maze))
    ret = rat.getPath(maze, 0, 0)
    if ret == False:
        print("No solution!")
'''
————————————————
版权声明：本文为CSDN博主「M.Philip.Lu」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_43029747/article/details/99725061
'''