#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#


# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        res = []
        l_cnt, r_cnt = 0, 0

        def dfs(l_cnt, r_cnt):
            if l_cnt > n or r_cnt > n or r_cnt > l_cnt:
                return
            if len(path) == 2 * n:
                tmp = ''.join(path)
                res.append(tmp)
                return
            for i in ['(', ')']:
                if i == '(':
                    path.append('(')
                    dfs(l_cnt + 1, r_cnt)
                    path.pop()
                elif i == ')':
                    path.append(')')
                    dfs(l_cnt, r_cnt + 1)
                    path.pop()

        dfs(l_cnt, r_cnt)
        return res


# @lc code=end
