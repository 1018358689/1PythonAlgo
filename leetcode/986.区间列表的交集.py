#
# @lc app=leetcode.cn id=986 lang=python3
#
# [986] 区间列表的交集
#

# @lc code=start
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        a = b = 0
        res = []
        while a < len(firstList) and b < len(secondList):
            a1, a2 = firstList[a]
            b1, b2 = secondList[b]
            if not (a1 > b2 or b1 > a2):
                res.append([max(a1, b1), min(a2, b2)])
            if b2 < a2:
                b += 1
            else:
                a += 1
        return res
# @lc code=end

