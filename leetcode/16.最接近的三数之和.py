#
# @lc app=leetcode.cn id=16 lang=python
#
# [16] 最接近的三数之和
#


# @lc code=start
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = []  # 存结果
        best = 10**7
        nums.sort()  # 先升序 方便后续判断左右移动
        for i in range(len(nums) - 2):
            L, R = i + 1, len(nums) - 1  # 三个数初始化索引 i  L  R
            while L < R:
                cur = nums[i] + nums[L] + nums[R]  # 计算和
                if abs(cur - target) < abs(best - target):
                    best = cur  # 更新best最接近target值
                    res = best  # 存储结果
                if cur == target:  # 刚好abs为0 直接返回
                    return cur
                elif cur < target:  # 因为已经是升序，所以和小于target那么 L右移 这样才能增大cur
                    L += 1
                else:  # 和大于target那么 R左移
                    R -= 1
        return res


# @lc code=end
