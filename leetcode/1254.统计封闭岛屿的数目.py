#
# @lc app=leetcode.cn id=1254 lang=python3
#
# [1254] 统计封闭岛屿的数目
#

# @lc code=start
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        res = 0

        def bfs(grid: list, r: int, c: int):
            queue = deque([(r, c)])
            while queue:
                sz = len(queue)
                for _ in range(sz):
                    r, c = queue.popleft()
                    if r < 0 or r > row - 1 or c < 0 or c > col - 1 or grid[r][c] == 1:
                        continue
                    grid[r][c] = 1
                    queue.append((r - 1, c))
                    queue.append((r + 1, c))
                    queue.append((r, c - 1))
                    queue.append((r, c + 1))

        for r in range(row):
            if grid[r][0] == 0:
                bfs(grid, r, 0)
            if grid[r][col - 1] == 0:
                bfs(grid, r, col - 1)

        for c in range(col):
            if grid[0][c] == 0:
                bfs(grid, 0, c)
            if grid[row - 1][c] == 0:
                bfs(grid, row - 1, c)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    res += 1
                    bfs(grid, r, c)

        return res
# @lc code=end

