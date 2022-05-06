#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#


# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        ha = {0: 1}

        def dfs(target: int):
            if target < 0:
                return 0
            if target not in ha:
                ha[target] = sum(dfs(target - n) for n in nums)
            return ha[target]

        return dfs(target)


# @lc code=end
