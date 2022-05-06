#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#


# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        j = 0
        for j in range(len(nums) - 3):
            if j > 0 and nums[j] == nums[j - 1]:
                continue
            for i in range(j + 1, len(nums) - 2):
                if i > j + 1 and nums[i] == nums[i - 1]:
                    continue
                L = i + 1
                R = len(nums) - 1  # [L,R]
                while L < R:
                    s = nums[j] + nums[i] + nums[L] + nums[R]
                    if s > target:
                        while L < R and nums[R] == nums[R - 1]:
                            R -= 1
                        R -= 1
                    elif s < target:
                        while L < R and nums[L] == nums[L + 1]:
                            L += 1
                        L += 1
                    elif s == target:
                        res.append([nums[j], nums[i], nums[L], nums[R]])
                        while L < R and nums[L] == nums[L + 1]:
                            L += 1
                        while L < R and nums[R] == nums[R - 1]:
                            R -= 1
                        L += 1
                        R -= 1
        return res


# @lc code=end
