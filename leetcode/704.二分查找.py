#
# @lc app=leetcode.cn id=704 lang=python
#
# [704] 二分查找
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        L, R = 0, len(nums) - 1  # [L,R]
        while L <= R:
            M = (L + R) // 2
            if target > nums[M]: L = M + 1
            elif target < nums[M]: R = M - 1
            else: return M
        return -1
# @lc code=end

