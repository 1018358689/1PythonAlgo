#
# @lc app=leetcode.cn id=1995 lang=python3
#
# [1995] 统计特殊四元组
#

# @lc code=start
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        path = []
        cnt = 0

        def dfs(si):
            nonlocal cnt
            if len(path) == 4 and sum(path[:3]) == path[-1]:
                cnt += 1
                return
            if len(path) == 4:
                return
            for i in range(si, len(nums)):
                path.append(nums[i])
                dfs(i + 1)
                path.pop()

        dfs(0)
        return cnt

# @lc code=end

