#
# @lc app=leetcode.cn id=1011 lang=python3
#
# [1011] 在 D 天内送达包裹的能力
#


# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def f(x):
            w = weights[:]
            w.append(float('inf'))
            cnt = 0
            s = 0
            fast = 0
            while fast <= len(w) - 1:
                s += w[fast]
                if s > x:
                    s = w[fast]
                    cnt += 1
                fast += 1
            return cnt

        l, r = max(weights), sum(weights)
        while l <= r:
            m = l + (r - l) // 2
            if D > f(m):
                r = m - 1
            elif D < f(m):
                l = m + 1
            elif D == f(m):
                r = m - 1
        return l


# @lc code=end
