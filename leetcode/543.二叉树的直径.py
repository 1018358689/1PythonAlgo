#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return False
        max_diameter = 0

        def dfs(node: TreeNode):  # 该节点为起点的最长路径
            nonlocal max_diameter
            if node is None:
                return -1
            max_left = dfs(node.left)
            max_right = dfs(node.right)
            max_diameter = max(max_diameter, 2 + max_left + max_right)
            return 1 + max(max_left, max_right)

        dfs(root)
        return max_diameter


# @lc code=end
