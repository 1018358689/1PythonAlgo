#
# @lc app=leetcode.cn id=53 lang=python
#
# [53] 最大子序和
#


# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        r = -float('inf')
        nums.append(0)
        for L in range(len(nums) - 1):
            for R in range(L + 1, len(nums)):
                s = sum(nums[L:R])
                if s > r: r = s
        return r
        '''
        for i in range(1, len(nums)):
            nums[i]= nums[i] + max(nums[i-1], 0)
        return max(nums)

# @lc code=end
