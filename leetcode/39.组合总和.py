#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(path, start_index):
            if sum(path) == target:
                res.append(path[:])
                return
            if sum(path) > target:
                return
            for i in range(start_index, len(candidates)):
                path.append(candidates[i])
                dfs(path, i)
                path.pop()

        dfs(path, 0)
        return res

# @lc code=end

