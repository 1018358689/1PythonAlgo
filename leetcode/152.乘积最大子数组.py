#
# @lc app=leetcode.cn id=152 lang=python
#
# [152] 乘积最大子数组
#


# @lc code=start
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        思路： 求最大值，可以看成求被0拆分的各个子数组的最大值。

        当一个数组中没有0存在，则分为两种情况：

        1.负数为偶数个，则整个数组的各个值相乘为最大值；

        2.负数为奇数个，则从左边开始，乘到最后一个负数停止有一个“最大值”，从右边也有一个“最大值”，比较，得出最大值。
        '''
        maxmul = float('-inf')
        r = 1
        for n in nums:
            r *= n
            maxmul = max(maxmul, r)
            if n == 0:
                r = 1
        r = 1
        for n in nums[::-1]:
            r *= n
            maxmul = max(maxmul, r)
            if n == 0:
                r = 1
        return maxmul


# @lc code=end
