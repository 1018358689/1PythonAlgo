#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#


# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = R = 0
        minlength = float('inf')
        while R <= len(nums) - 1:
            while sum(nums[L:R + 1]) >= target:
                minlength = min(minlength, R + 1 - L)
                L += 1
            R += 1
        return minlength if minlength != float('inf') else 0


# @lc code=end
