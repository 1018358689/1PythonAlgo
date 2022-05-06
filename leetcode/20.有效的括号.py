#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        ha = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for i in s:
            if i in ha:
                stack.append(i)
            else:
                if stack and ha[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
        return not stack
# @lc code=end

