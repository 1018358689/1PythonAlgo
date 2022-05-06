#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#


# @lc code=start
class Solution(object):
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def check(path, row, col, target):
            row_copy, col_copy = row, col
            # 检查行
            row = row_copy
            for col in range(9):
                if path[row][col] == target: return False
            # 检查列
            col = col_copy
            for row in range(9):
                if path[row][col] == target: return False
            # 检查九宫格
            row_start = (row_copy // 3) * 3
            col_start = (col_copy // 3) * 3
            for row in range(row_start, row_start + 3):
                for col in range(col_start, col_start + 3):
                    if path[row][col] == target: return False
            return True

        def dfs(path):
            for row in range(9):
                for col in range(9):
                    if path[row][col] != '.': continue
                    for i in range(1, 10):  # (row,col) 这个位置放i是否合适
                        if check(path, row, col, str(i)) == False: continue
                        path[row][col] = str(i)  # 放置i
                        if dfs(path) == True:
                            return True # 如果找到合适一组立刻返回
                        else:
                            path[row][col] = '.'  # 全部数字试了都不行 则回溯 撤销i
                    return False  # 全部数字试了都不行
            return True  # 遍历完没有返回false，说明找到了合适棋盘位置了

        dfs(board)
        return board


# @lc code=end
