#
# @lc app=leetcode.cn id=1020 lang=python3
#
# [1020] 飞地的数量
#

# @lc code=start
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def bfs(grid: list, path_set: list):
            q = collections.deque(path_set)
            while q:
                sz = len(q)
                for _ in range(sz):
                    r, c = q.popleft()
                    if r < 0 or r > rows - 1 or c < 0 or c > cols - 1 or grid[r][c] == 0:
                        continue
                    grid[r][c] = 0
                    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        q.append((nr, nc))

        path_set = []
        for c in range(cols):
            for r in (0, rows - 1):
                if grid[r][c] == 1:
                    path_set.append((r, c))
        for r in range(rows):
            for c in (0, cols - 1):
                if grid[r][c] == 1:
                    path_set.append((r, c))
        bfs(grid, path_set)
        cnt = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    cnt += 1
        return cnt
# @lc code=end

