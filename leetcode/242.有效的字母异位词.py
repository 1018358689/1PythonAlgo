#
# @lc app=leetcode.cn id=242 lang=python
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t) or set(s)!=set(t):return False
        r = 0
        for i in (ord(i) for i in s+t):
            r ^= i
        return r==0
# @lc code=end

