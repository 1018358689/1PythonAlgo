#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
#

# @lc code=start
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        sz_row = len(mat)
        sz_col = len(mat[0])
        q = collections.deque([])
        res = [[0] * sz_col for _ in range(sz_row)]
        for r in range(sz_row):
            for c in range(sz_col):
                if mat[r][c] == 0:
                    q.append((r, c))
        step = 0
        visited = set(q)
        while q:
            sz = len(q)
            for _ in range(sz):
                r, c = q.popleft()

                if mat[r][c] == 1:
                    res[r][c] = step

                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if nr < 0 or nr > sz_row - 1 or nc < 0 or nc > sz_col-1:
                        continue
                    if (nr, nc) in visited:
                        continue
                    visited.add((nr, nc))
                    q.append((nr, nc))
            step += 1
        return res
# @lc code=end

