#
# @lc app=leetcode.cn id=14 lang=python
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        r = ''
        for i in zip(*strs):
            i_set = set(i)
            if len(i_set) == 1:
                r+=i[0]
            else:
                break
        return r
# @lc code=end

