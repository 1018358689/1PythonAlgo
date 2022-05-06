#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#


# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        path = []

        def dfs(path, si):
            res.append(path[:])
            # if si==len(nums):
            #     return
            for i in range(si, len(nums)):
                if i > si and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                dfs(path, i + 1)
                path.pop()

        dfs(path, 0)
        return res



# @lc code=end
