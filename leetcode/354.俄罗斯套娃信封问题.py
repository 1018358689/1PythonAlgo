#
# @lc app=leetcode.cn id=354 lang=python3
#
# [354] 俄罗斯套娃信封问题
#


# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        nums = [i[1] for i in envelopes]

        def f(nums: list) -> int:
            if not nums: return 0
            dp = [1] * len(nums)
            for i in range(len(nums)):
                for j in range(i):
                    if nums[j] < nums[i]:  # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                        dp[i] = max(dp[i], dp[j] + 1)
            return max(dp)

        return f(nums)


# @lc code=end
