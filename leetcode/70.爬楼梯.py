#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#


# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        def g(n: int, mem: list) -> int:
            if n == 1: return 1
            if n == 2: return 2
            if mem[n] == -1:
                mem[n] = g(n - 1, mem) + g(n - 2, mem)
            return mem[n]

        mem = [-1] * (n + 1)
        return g(n, mem)


# @lc code=end
