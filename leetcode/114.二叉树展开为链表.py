#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # BaseCase
        if not root:
            return
        # 递归拉平左右子树
        self.flatten(root.left)
        self.flatten(root.right)
        # 后序位置 拉平后操作 从下往上拉平
        left = root.left  # 存储一下左右
        right = root.right

        root.left = None  # 左为None
        root.right = left  # 右为left

        node = root
        while node.right != None:
            node = node.right  # 一直走到最右下方
        node.right = right  # 把原来的右放到现在的右
# @lc code=end

