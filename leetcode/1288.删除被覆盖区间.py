#
# @lc app=leetcode.cn id=1288 lang=python3
#
# [1288] 删除被覆盖区间
#

# @lc code=start
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        r = intervals[0][1]
        res = 0
        for _, e in intervals[1:]:
            if e <= r:
                res += 1
            elif r < e:
                r = e
        return len(intervals) - res
# @lc code=end

