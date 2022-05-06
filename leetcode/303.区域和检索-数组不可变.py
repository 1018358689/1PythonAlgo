#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#

# @lc code=start
from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.ps = [-1] * (len(nums) + 1)
        self.ps[0] = 0
        for i in range(len(nums)):
            self.ps[i + 1] = self.ps[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        r = self.ps[right + 1] - self.ps[left]
        return r


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

