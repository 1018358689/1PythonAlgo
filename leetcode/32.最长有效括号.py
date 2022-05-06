#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        mark = [0] * len(s)
        stack = []
        for i, n in enumerate(s):
            if n == '(':  # 左括号入栈
                stack.append(i)
            else:  # 如果右括号
                if stack:  # 栈不为空 则弹出
                    stack.pop()
                else:  # 栈为空 则标记i为1
                    mark[i] = 1
        for i in stack:  # 剩下未匹配的i都为1
            mark[i] = 1

        length = 0
        cnt = 0
        for m in mark:
            if m == 0:
                cnt += 1
                length = max(length, cnt)
            elif m == 1:
                cnt = 0

        return length
# @lc code=end

