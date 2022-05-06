#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(board: list, row: int, col: int, content: str):
            for c in range(9):
                if c == col:
                    continue
                if board[row][c] == content:
                    return False
            for r in range(9):
                if r == row:
                    continue
                if board[r][col] == content:
                    return False
            s_r = row // 3 * 3
            s_c = col // 3 * 3
            for r in range(s_r, s_r + 3):
                for c in range(s_c, s_c + 3):
                    if r == row and c == col:
                        continue
                    if board[r][c] == content:
                        return False
            return True

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if check(board, r, c, board[r][c]) == False:
                    return False
        return True
# @lc code=end

