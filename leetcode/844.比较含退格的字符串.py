#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#


# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def txt(s: str) -> list:
            l = []
            for i in s:
                if i != '#':
                    l.append(i)
                elif i == '#' and l:
                    l.pop()
            return l

        return txt(s) == txt(t)


# @lc code=end
