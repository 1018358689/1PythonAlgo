#
# @lc app=leetcode.cn id=350 lang=python
#
# [350] 两个数组的交集 II
#


# @lc code=start
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        '''
        from collections import Counter
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        c12 = c1 & c2
        r = []
        for i in c12:
            r += [i] * c12[i]
        return r
        '''
        inter = set(nums1) & set(nums2)
        r = []
        for i in inter:
            r+=[i]*min(nums1.count(i),nums2.count(i))
        return r
# @lc code=end
