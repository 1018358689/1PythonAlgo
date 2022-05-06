#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#


# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        L = 0
        R = len(nums) - 1
        while L <= R:
            M = (L + R) // 2
            if target < nums[M]:
                R = M - 1
            elif target > nums[M]:
                L = M + 1
            elif target == nums[M]:
                R = M - 1
        if L > len(nums) - 1:
            return [-1, -1]
        if nums[L] != target:
            return [-1, -1]
        left = L
        L = 0
        R = len(nums) - 1
        while L <= R:
            M = (L + R) // 2
            if target < nums[M]:
                R = M - 1
            elif target > nums[M]:
                L = M + 1
            elif target == nums[M]:
                L = M + 1
        return [left, R]


# @lc code=end
