#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#


# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ha = defaultdict(list)
        for i, n in enumerate(t):
            ha[n].append(i)

        def search(nums: list, target: int) -> int:
            l, r = 0, len(nums) - 1  # [l,r]
            while l <= r:
                m = l + (r - l) // 2
                if target > nums[m]:
                    l = m + 1
                elif target < nums[m]:
                    r = m - 1
                elif target == nums[m]:
                    r = m - 1
            if r == len(nums) - 1:
                return -1
            else:
                return l

        target = 0
        for i in s:
            if i not in ha:
                return False
            else:
                nums = ha[i]
            target = search(nums, target)
            if target == -1:
                return False
            target = nums[target] + 1
        return True


# @lc code=end
