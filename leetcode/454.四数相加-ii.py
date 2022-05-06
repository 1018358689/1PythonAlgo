#
# @lc app=leetcode.cn id=454 lang=python
#
# [454] 四数相加 II
#

# @lc code=start
from collections import Counter

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        countAB = Counter(a+b for a in A for b in B)
        cnt=0
        for c in C:
            for d in D:
                cnt += countAB.get(-c-d,0)
        return cnt
# @lc code=end

