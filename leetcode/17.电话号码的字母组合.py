#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#


# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        hash_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        path = []
        deepth = 0
        res = []

        def dfs(path, deepth, digits):
            if deepth == len(digits):
                res.append(''.join(path))
                return
            for i in hash_map[digits[deepth]]:
                path.append(i)
                dfs(path, deepth + 1, digits)
                path.pop()

        dfs(path, deepth, digits)
        return res


# @lc code=end
