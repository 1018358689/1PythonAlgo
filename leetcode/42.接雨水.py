#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        height_lr = 0
        height_rl = 0
        ans = 0
        while l < r:
            height_lr = max(height_lr, height[l])
            height_rl = max(height_rl, height[r])
            if height_lr < height_rl:
                ans += height_lr - height[l]
                l += 1
            else:
                ans += height_rl - height[r]
                r -= 1
        return ans
# @lc code=end

