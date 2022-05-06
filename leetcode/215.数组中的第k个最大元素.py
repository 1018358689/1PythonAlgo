#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = list(map(lambda x: -x, nums))
        heapify(heap)
        res = 0
        for _ in range(k):
            res = heappop(heap)
        return -res
# @lc code=end

