#
# @lc app=leetcode.cn id=1446 lang=python
#
# [1446] 连续字符
#

# @lc code=start
from collections import Counter


class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1: return 1
        L = 0
        R = 1
        maxlength = 0
        while R <= len(s) - 1:
            while R <= len(s) - 1 and s[R] == s[L]:
                R += 1
            maxlength = max(maxlength, R - L)
            L = R
        return maxlength


# @lc code=end
