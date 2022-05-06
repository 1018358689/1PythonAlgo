#
# @lc app=leetcode.cn id=144 lang=python
#
# [144] 二叉树的前序遍历
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 中左右
# 反序入栈判断 取消if
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        if root: stack.append(root)
        while stack:
            root = stack.pop() # 弹出判断
            res.append(root.val) # 写哪里都一样
            if root.right: stack.append(root.right) # 右左顺序入栈 出栈就是左右
            if root.left: stack.append(root.left)
        return res


# @lc code=end
