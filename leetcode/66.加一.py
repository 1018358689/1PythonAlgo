#
# @lc app=leetcode.cn id=66 lang=python
#
# [66] 加一
#


# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return [int(j) for j in str(int(''.join(str(i) for i in digits)) + 1)]


# @lc code=end
