#
# @lc app=leetcode.cn id=46 lang=python
#
# [46] 全排列
#


# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        path = []  # 选择的路径
        res = []  # 结果的集合

        def dfs():
            if len(path) == len(nums):  # 遍历到底了 添加结果
                res.append(path[:])  # path要拷贝一下
                return
            for n in nums:  # 横向遍历
                if n in path:  # path里已经收录的元素，直接跳过
                    continue
                path.append(n)  # 做选择
                dfs()  # 纵向递归
                path.pop()  # 撤销选择 (回溯)

        dfs()
        return res


# @lc code=end
