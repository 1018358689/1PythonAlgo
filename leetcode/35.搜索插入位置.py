#
# @lc app=leetcode.cn id=35 lang=python
#
# [35] 搜索插入位置
#


# @lc code=start
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        L = 0
        R = len(nums) - 1  # [L,R]
        while L <= R:
            M = (L + R) // 2
            if nums[M] > target:
                R = M - 1
            elif nums[M] < target:
                L = M + 1
            elif nums[M] == target:
                R = M - 1
        return L


# @lc code=end
