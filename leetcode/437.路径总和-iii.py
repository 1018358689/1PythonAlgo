#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if root is None: return 0
        prefix = defaultdict(int)
        prefix[0] = 1
        cnt = 0

        def dfs(node: TreeNode, cur_sum: int):
            nonlocal cnt
            cur_sum += node.val
            cnt += prefix[cur_sum - targetSum]
            for n in [node.left, node.right]:
                if n:
                    prefix[cur_sum] += 1
                    dfs(n, cur_sum)
                    prefix[cur_sum] -= 1

        dfs(root, 0)
        return cnt


# @lc code=end
