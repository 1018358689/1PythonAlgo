#
# @lc app=leetcode.cn id=740 lang=python
#
# [740] 删除并获得点数
#

# @lc code=start
# 定义：dp[i] 为小于等于 i 的点数, 通过特殊操作(删或不删)所能获得到的最大值.
# 状态转移：dp[i] = max(dp[i-1],dp[i-2]+numsmap[i]*i)
# 边界初始化：basecase dp[0]=0, dp[1]=numsmap[1]*1
from collections import Counter


class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsmap = Counter(nums)
        maxnum = max(nums)
        dp = [0] + [0] * maxnum  # 为了取到maxnum 所以长度加1
        dp[0] = 0
        dp[1] = numsmap[1] * 1
        for i in range(2, maxnum + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + numsmap[i] * i)
        return dp[maxnum]


# @lc code=end
