#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#


# @lc code=start
# import copy
class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [['.'] * n for _ in range(n)]
        path = board
        cnt=0
        res = []

        def choose(path, row, col):
            copy_row, copy_col = row, col
            # 检查上方
            row, col = copy_row - 1, copy_col
            while row >= 0:
                if path[row][col] == 'Q': return False
                row -= 1
            # 检查左上
            row, col = copy_row - 1, copy_col - 1
            while row >= 0 and col >= 0:
                if path[row][col] == 'Q': return False
                row -= 1
                col -= 1
            # 检查右上
            row, col = copy_row - 1, copy_col + 1
            while row >= 0 and col <= n - 1:
                if path[row][col] == 'Q': return False
                row -= 1
                col += 1
            return True

        def dfs(path, row):
            nonlocal cnt
            if row == n - 1 + 1:
                cnt+=1
                # tmp = [''.join(p) for p in path[:]]
                # res.append(tmp)
                # res.append(copy.deepcopy(path))
                return
            for col in range(n):
                if not choose(path, row, col):
                    continue
                path[row][col] = 'Q'
                dfs(path, row + 1)
                path[row][col] = '.'

        dfs(path, 0)
        return cnt


# @lc code=end
