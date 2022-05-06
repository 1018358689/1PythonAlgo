#
# @lc app=leetcode.cn id=122 lang=python
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prices += [-float('inf')]
        length = len(prices)
        profit = 0
        L, R = 0, 1
        while R < length:
            if prices[R] < prices[R - 1]:
                profit += prices[R - 1] - prices[L]
                L = R
            R += 1
        return profit
# @lc code=end

