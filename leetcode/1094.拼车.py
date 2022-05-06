#
# @lc app=leetcode.cn id=1094 lang=python3
#
# [1094] 拼车
#


# @lc code=start
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        length = max(i[2] for i in trips)+1
        diff = [0] * length
        for val, s, e in trips:
            diff[s] += val
            if e < length:
                diff[e] -= val

        res = [-1] * length
        res[0] = diff[0]
        if res[0] > capacity:
            return False
        for i in range(1, length):
            res[i] = res[i - 1] + diff[i]
            if res[i] > capacity:
                return False
        return True


# @lc code=end
