#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#


# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []

        def dfs(path, candidates, target, start_index):
            if sum(path) > target:
                return
            if sum(path) == target:
                res.append(path[:])
                return
            for i in range(start_index, len(candidates)):
                if i >= start_index + 1 and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                dfs(path, candidates, target, i + 1)
                path.pop()

        dfs(path, candidates, target, 0)
        return res


# @lc code=end
