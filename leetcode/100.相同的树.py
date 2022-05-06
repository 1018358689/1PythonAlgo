#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:  # p q 都不存在
            return True
        elif not p or not q:  # 有前一个条件限制 此处意思为右一个为空
            return False
        elif p.val != q.val:  # p q 都存在 但值不同
            return False  # 以上前序 进入节点时
        # 剩下p q都存在 且值相同 这时候就看子树了 子树都True才可以
        bool_left = self.isSameTree(p.left, q.left)
        bool_right = self.isSameTree(p.right, q.right)
        return bool_left and bool_right  # 后序 离开节点时


# @lc code=end
