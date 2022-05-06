#
# @lc app=leetcode.cn id=1518 lang=python
#
# [1518] 换酒问题
#

# @lc code=start
class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        cnt = numBottles
        while numBottles >= numExchange:
            quo, rem = divmod(numBottles, numExchange)
            cnt += quo
            numBottles = quo + rem
        return cnt

# @lc code=end

