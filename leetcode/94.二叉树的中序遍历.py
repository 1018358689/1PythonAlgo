#
# @lc app=leetcode.cn id=94 lang=python
#
# [94] 二叉树的中序遍历
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):  # 左中右 -入栈 右中左
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        if root: stack.append(root)
        while stack:
            root = stack.pop()
            if root:
                if root.right: stack.append(root.right)
                stack.append(root)
                stack.append(None)
                if root.left: stack.append(root.left)
            else:
                root = stack.pop()
                res.append(root.val)
        return res


# @lc code=end
