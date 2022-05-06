#
# @lc app=leetcode.cn id=51 lang=python
#
# [51] N 皇后
#


# @lc code=start
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [['.'] * n for _ in range(n)]
        res = []
        path = board

        def choose(path, row, col):
            copy_row, copy_col = row, col
            # 列是否有重
            row, col = copy_row - 1, copy_col
            while row >= 0:
                if path[row][col] == 'Q':
                    return False
                row -= 1
            # 右上角是否有重
            row, col = copy_row - 1, copy_col + 1
            while row >= 0 and col <= n - 1:
                if path[row][col] == 'Q':
                    return False
                row -= 1
                col += 1
            # 左上角是否有重
            row, col = copy_row - 1, copy_col - 1
            while row >= 0 and col >= 0:
                if path[row][col] == 'Q':
                    return False
                row -= 1
                col -= 1
            return True

        def dfs(path, row):
            if row == n - 1 + 1:
                tmp = [''.join(p) for p in path[:]]
                res.append(tmp)
                return
            for col in range(n):
                if choose(path, row, col) == False:
                    continue
                path[row][col] = 'Q'
                dfs(path, row + 1)
                path[row][col] = '.'

        dfs(path, 0)
        return res


# @lc code=end
