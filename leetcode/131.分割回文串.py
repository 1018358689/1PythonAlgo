#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#


# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def dfs(si):
            if si == len(s):
                res.append(path[:])
                return
            for i in range(si, len(s)):
                tmp = s[si:i + 1]
                if tmp != tmp[::-1]:
                    continue
                path.append(tmp)
                dfs(i + 1)
                path.pop()

        dfs(0)
        return res


# @lc code=end
