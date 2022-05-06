#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ha = {}
        for i, n in enumerate(nums):  # 获得value-index字典 相同值的索引为大的那个索引
            ha[n] = i
        for i, n in enumerate(nums):
            j = ha.get(target - n)
            if j != None and j != i:  # j存在 且i和j不一样（说明j和i不重叠)
                return [i, j]


# @lc code=end
