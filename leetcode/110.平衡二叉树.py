#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        signal = True

        def dfs(node: TreeNode):
            nonlocal signal
            if not node:
                return 0
            hi_l = dfs(node.left)
            hi_r = dfs(node.right)
            if abs(hi_l - hi_r) > 1:
                signal = False
            return 1 + max(hi_l, hi_r)

        dfs(root)
        return signal
# @lc code=end

