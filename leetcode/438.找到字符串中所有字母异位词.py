#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p): return []
        window, need = defaultdict(int), defaultdict(int)
        window_length = len(p)
        for i in p:
            need[i] += 1
        for i in range(len(p) - 1):
            window[s[i]] += 1
        l = 0
        r = l + window_length - 1
        res = []
        while r <= len(s) - 1:
            window[s[r]] += 1
            if window == need:
                res.append(l)
            window[s[l]] -= 1
            if window[s[l]] == 0:
                del window[s[l]]
            l += 1
            r += 1
        return res
# @lc code=end

