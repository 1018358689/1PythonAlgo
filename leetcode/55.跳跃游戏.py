#
# @lc app=leetcode.cn id=55 lang=python
#
# [55] 跳跃游戏
#

# @lc code=start
# dp[i] 为下标i这个点所能跳到的最远距离
# dp[i] = max(nums[i],dp[i-1]-1)
# dp[0] = nums[0]
# 在每次循环开始，我们判断dp[i-1]是否等于0，若是，则不可能到达下标i处，因此直接返回false。循环结束后 返回true
# 因为转移状态数组dp只和前一位有关，因此可以用滚动数组简化空间复杂度
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        size = len(nums)
        dp = [0] * size
        dp[0] = nums[0]
        for i in range(1, size):
            print(dp[i - 1])
            dp[i] = max(nums[i], dp[i - 1] - 1)
            if dp[i - 1] == 0: return False
        return True
# @lc code=end

