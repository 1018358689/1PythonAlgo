#
# @lc app=leetcode.cn id=119 lang=python
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        r = [1]
        for row in range(1, rowIndex + 1):
            r.insert(0, 0)
            for idx in range(row):
                r[idx] = r[idx] + r[idx + 1]
        return r
# @lc code=end

