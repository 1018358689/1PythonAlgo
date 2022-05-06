#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
from collections import deque
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = [''] * numRows
        q = deque(s)
        tmp = list(range(numRows))
        res_index = tmp + tmp[1:numRows - 1][::-1]
        # print(res_index)
        while q:
            for i in res_index:
                if not q:
                    break
                res[i] += q.popleft()
        return ''.join(res)
            


# @lc code=end

