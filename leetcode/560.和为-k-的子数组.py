#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mem = {0: 1}
        cur_sum = 0
        cnt = 0
        for n in nums:
            cur_sum += n
            need_sum = cur_sum - k
            cnt += mem.get(need_sum, 0)
            mem[cur_sum] = mem.get(cur_sum, 0) + 1

        return cnt
# @lc code=end

