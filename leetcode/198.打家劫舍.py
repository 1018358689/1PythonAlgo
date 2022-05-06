#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#


# @lc code=start
class Solution:
    def rob(self, moneys: List[int]) -> int:
        if len(moneys) == 1: return moneys[0]
        if len(moneys) == 2: return max(moneys[0], moneys[1])
        prev = moneys[0]
        cur = max(moneys[0], moneys[1])
        for i in range(2, len(moneys)):
            prev, cur = cur, max(prev + moneys[i], cur)
        return cur


# @lc code=end
