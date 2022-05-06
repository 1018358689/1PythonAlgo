#
# @lc app=leetcode.cn id=278 lang=python
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 注意 isBadVersion(M)==True是错误版本
        L,R=1,n # [1,n]
        while L<=R:
            M=(L+R)//2
            if isBadVersion(M)==True:
                R=M-1
            elif isBadVersion(M)==False:
                L=M+1
        return L

# @lc code=end

