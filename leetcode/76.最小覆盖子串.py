#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#


# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict

        window, ht = defaultdict(int), defaultdict(int)
        for i in t:
            ht[i] += 1
        l = r = 0
        valid = 0
        res = s + '_'
        while r <= len(s) - 1:
            # 窗口更新
            c = s[r]  # 即将移入窗口的值
            if ht.get(c, 0) != 0:
                window[c] += 1
                if window[c] == ht[c]:
                    valid += 1
            # 判断左窗口是否要收缩
            while valid == len(ht):
                if len(res) > r + 1 - l:  # 最优解寻找 更新res
                    res = s[l:r + 1]

                # 窗口更新
                d = s[l]  # 即将移出窗口的值
                if ht.get(d, 0) != 0:
                    if window[d] == ht[d]:
                        valid -= 1
                    window[d] -= 1
                l += 1  # 左移窗口
            r += 1  # 右移窗口
        return res if res != s + '_' else ''


# @lc code=end
