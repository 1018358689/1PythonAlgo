#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#


# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):return False
        from collections import defaultdict
        need, window = defaultdict(int), defaultdict(int)
        for s in s1:
            need[s] += 1
        for i in range(len(s1) - 1):
            window[s2[i]] += 1
        window_length = len(s1)
        L = 0
        R = L + window_length - 1  # [L,R]
        while R <= len(s2) - 1:
            # 窗口更新
            c = s2[R]
            window[c] += 1
            # 窗口判断
            if window == need:
                return True
            # 窗口更新
            d = s2[L]
            window[d] -= 1
            if window[d]==0:
                del window[d]
            # 移动窗口
            L += 1
            R = L + window_length - 1
        return False


# @lc code=end
