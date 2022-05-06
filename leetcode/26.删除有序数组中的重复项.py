#
# @lc app=leetcode.cn id=26 lang=python
#
# [26] 删除有序数组中的重复项
#


# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        L = 1
        R = 1
        while R <= len(nums) - 1:
            if nums[R] != nums[R - 1]:
                nums[L] = nums[R]
                L += 1
            R += 1
        return L


# @lc code=end
