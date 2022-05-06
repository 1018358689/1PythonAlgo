#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        mem = {}

        def dfs(mem, i):
            nonlocal maxsum
            if i == 0: return nums[0]
            if i not in mem:
                mem[i] = max(dfs(mem, i - 1) + nums[i], nums[i])
                maxsum = max(maxsum, mem[i])
            return mem[i]

        dfs(mem, len(nums) - 1)
        return maxsum


# @lc code=end
