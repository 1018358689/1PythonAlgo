#
# @lc app=leetcode.cn id=875 lang=python3
#
# [875] 爱吃香蕉的珂珂
#


# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        # x:变量速度  f(x):吃piles所需时间 单调递减函数
        def f(x: int) -> int:
            h = 0
            for p in piles:
                if x >= p:
                    h += 1
                elif x < p:
                    h += p // x + min(1, p % x)
            return h

        l, r = 1, max(piles)  # [1,max(piles)]
        while l <= r:
            m = l + (r - l) // 2
            if H > f(m):
                r = m - 1
            elif H < f(m):
                l = m + 1
            elif H == f(m):
                r = m - 1
        return l


# @lc code=end
