#
# @lc app=leetcode.cn id=77 lang=python
#
# [77] 组合
#

# @lc code=start
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        path = []
        res = []

        def dfs(start_index):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(start_index, n + 1):
                path.append(i)
                dfs(i + 1)
                path.pop()

        dfs(1)
        return res
# @lc code=end

