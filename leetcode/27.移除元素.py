#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        L=0
        R=0
        while R<=len(nums)-1:
            if nums[R]!=val:
                nums[L] = nums[R]
                L+=1
            # 当 R 指针遇到要删除的元素时停止赋值
            # L 指针停止移动, R 指针继续前进
            R+=1
        return L
# @lc code=end

