#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None: return 0
        res = float('inf')

        def dfs(root, deepth):
            nonlocal res
            if root.left == None and root.right == None:
                res = min(res, deepth)
                return
            if root.left:
                deepth += 1
                dfs(root.left, deepth)
                deepth -= 1
            if root.right:
                deepth += 1
                dfs(root.right, deepth)
                deepth -= 1

        dfs(root, 1)
        return res


# @lc code=end
