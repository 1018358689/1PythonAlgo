#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        res = [intervals[0]]
        for s, e in intervals[1:]:
            l, r = res[-1]
            if l <= s and e <= r:
                continue
            elif l <= s <= r and e >= r:
                res[-1][1] = e
            elif s >= r:
                res.append([s, e])
        return res
# @lc code=end

