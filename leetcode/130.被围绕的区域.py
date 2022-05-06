#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        q = collections.deque([])
        for c in range(cols):
            if board[0][c] == 'O': q.append((0, c))
            if board[rows - 1][c] == 'O': q.append((rows - 1, c))
        for r in range(rows):
            if board[r][0] == 'O': q.append((r, 0))
            if board[r][cols - 1] == 'O': q.append((r, cols - 1))
        while q:
            sz = len(q)
            for _ in range(sz):
                r, c = q.popleft()
                if r < 0 or r > rows - 1 or c < 0 or c > cols - 1 or board[r][c] == 'X' or board[r][c] == 'T':
                    continue
                board[r][c] = 'T'
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    q.append((nr, nc))
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'
        return board

# @lc code=end

