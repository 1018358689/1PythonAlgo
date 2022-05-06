#
# @lc app=leetcode.cn id=322 lang=python
#
# [322] 零钱兑换
#


# @lc code=start
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # BaseCase
        dp = [float('inf')] * amount + [float('inf')]
        # BaseCase
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if coin > i: continue
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


# @lc code=end
