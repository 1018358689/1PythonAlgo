#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        i=0
        while i <=len(nums)-3:
            if nums[i]>0:
                break
            if i >0 and nums[i]==nums[i-1]:
                i+=1
                continue
            L = i+1
            R = len(nums)-1 # [L,R]
            while L<R:
                s = nums[i]+nums[L]+nums[R]
                if s>0:
                    R-=1
                elif s<0:
                    L+=1
                elif s==0:
                    res.append([nums[i],nums[L],nums[R]])
                    while L<R and nums[L]== nums[L+1]:
                        L+=1
                    while L<R and nums[R] == nums[R-1]:
                        R-=1
                    L+=1
                    R-=1
            i+=1
        return res
# @lc code=end

