#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L = R = 0
        while R <= len(nums) - 1:
            if nums[R] != 0:  # 慢指针只要当快指针碰到非0 交换完 才往前一步
                nums[L], nums[R] = nums[R], nums[L]
                L += 1
            R += 1
        return nums
# @lc code=end

