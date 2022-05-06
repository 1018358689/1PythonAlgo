#
# @lc app=leetcode.cn id=304 lang=python3
#
# [304] 二维区域和检索 - 矩阵不可变
#

# @lc code=start
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.ps = self.pre_sum()

    def pre_sum(self):
        row = len(self.matrix)
        col = len(self.matrix[0])
        res = [[0] * (col + 1) for _ in range(row + 1)]
        for r in range(row):
            for c in range(col):
                res[r + 1][c + 1] = res[r][c + 1] + res[r + 1][c] - res[r][c] + self.matrix[r][c]
        return res

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s1 = self.ps[row2 + 1][col2 + 1]
        s0 = self.ps[row1][col1]
        s3 = self.ps[row1][col2 + 1]
        s4 = self.ps[row2 + 1][col1]
        # s1 = s3 + s4 - s0 + r
        return s1 - s3 - s4 + s0


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

