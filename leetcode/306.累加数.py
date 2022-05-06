#
# @lc app=leetcode.cn id=306 lang=python3
#
# [306] 累加数
#

# @lc code=start
class Solution:
    def isAdditiveNumber(self, nums: str) -> bool:
        if len(nums) < 3:
            return False

        def check(nums: list):  # 用来判断是否可以构成累加序列
            for i in range(len(nums) - 2):
                if nums[i] + nums[i + 1] != nums[i + 2]:
                    return False
            return True

        def dfs(path: list, si: int, res_num: str):
            # print(path)
            if len(path) > 2:
                if check(path) == False:  # 半路遇到不符合就回溯
                    return
            if len(path) > 2 and len(res_num) == 0:  # nums中所有数字都用上 且path长度大于等于3
                if check(path) == True:  # 找到一个就退出
                    # print(path)
                    return True

            for i in range(si, len(nums)):
                if nums[si] == '0' and i > si:  # 0开头数字排除
                    break
                cur = int(nums[si:i + 1])  # 添加当前数字
                if dfs(path+[cur], i + 1, nums[i + 1:]):
                    return True
            return False

        return dfs([], 0, nums)
# @lc code=end

