#
# @lc app=leetcode.cn id=1109 lang=python3
#
# [1109] 航班预订统计
#


# @lc code=start
class Difference:
    def __init__(self, nums) -> None:
        diff = [-1] * len(nums)
        diff[0] = nums[0]
        for i in range(1, len(nums)):
            diff[i] = nums[i] - nums[i - 1]
        self.diff = diff

    def increment(self, i, j, val):
        self.diff[i] += val
        if j + 1 < len(self.diff):
            self.diff[j + 1] -= val

    def result(self):
        res = [-1] * len(self.diff)
        res[0] = self.diff[0]
        for i in range(1, len(self.diff)):
            res[i] = res[i - 1] + self.diff[i]
        return res


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        nums = [0] * n
        D = Difference(nums)
        for update in bookings:
            s, e, val = update
            D.increment(s - 1, e - 1, val)
        return D.result()


# @lc code=end
