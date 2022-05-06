#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            if height[l] < height[r]:
                area = (r - l) * height[l]
                l += 1
            else:
                area = (r - l) * height[r]
                r -= 1
            ans = max(ans,area)
        return ans
# @lc code=end

