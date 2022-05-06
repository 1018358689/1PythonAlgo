#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#


# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = list(range(1, 10))
        res = []
        deepth = 1
        path = []

        def dfs(path, start_index, deepth):
            if deepth > k and sum(path) == n:
                res.append(path[:])
                return
            if deepth > k:
                return
            for i in range(start_index, len(nums)):
                path.append(nums[i])
                dfs(path, i + 1, deepth + 1)
                path.pop()

        dfs(path, 0, deepth)
        return res


# @lc code=end
