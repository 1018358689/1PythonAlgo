#
# @lc app=leetcode.cn id=921 lang=python3
#
# [921] 使括号有效的最少添加
#

# @lc code=start
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = rneed = 0
        for i in s:
            if i == '(':
                rneed += 1
            else:
                rneed -= 1
                if rneed == -1:
                    res += 1
                    rneed = 0
        return res + rneed
# @lc code=end

