#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        res = 0

        def bfs(grid, r, c):
            queue = deque([(r, c)])
            while queue:
                sz = len(queue)
                for _ in range(sz):
                    r, c = queue.popleft()
                    if r < 0 or r > row - 1 or c < 0 or c > col - 1 or grid[r][c] == '0':
                        continue
                    grid[r][c] = '0'
                    queue.append((r - 1, c))
                    queue.append((r + 1, c))
                    queue.append((r, c - 1))
                    queue.append((r, c + 1))

        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    res += 1
                    bfs(grid, r, c)
        return res
# @lc code=end

