#
# @lc app=leetcode.cn id=2006 lang=python
#
# [2006] 差的绝对值为 K 的数对数目
#

# @lc code=start
class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        r = 0
        for i in range(len(nums) - 1): 
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) == k: r += 1
        return r
# @lc code=end

