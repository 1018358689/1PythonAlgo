#
# @lc app=leetcode.cn id=1905 lang=python3
#
# [1905] 统计子岛屿
#

# @lc code=start
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        row = len(grid1)
        col = len(grid1[0])
        res = 0

        def dfs(grid, r, c):
            queue = deque([(r, c)])
            while queue:
                sz = len(queue)
                for _ in range(sz):
                    r, c = queue.popleft()
                    if 0 <= r < row and 0 <= c < col and grid[r][c] == 1:
                        grid[r][c] = 0
                        queue.append((r - 1, c))
                        queue.append((r + 1, c))
                        queue.append((r, c + 1))
                        queue.append((r, c - 1))

        for r in range(row):
            for c in range(col):
                if grid1[r][c] == 0 and grid2[r][c] == 1:
                    dfs(grid2, r, c)

        for r in range(row):
            for c in range(col):
                if grid2[r][c] == 1:
                    res += 1
                    dfs(grid2, r, c)

        return res
# @lc code=end

