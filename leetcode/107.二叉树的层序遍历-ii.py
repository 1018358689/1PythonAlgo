#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层序遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        queue = deque([root])
        while queue:
            size = len(queue)
            tmp = []
            for _ in range(size):
                root = queue.popleft()
                tmp.append(root.val)
                if root.left: queue.append(root.left)
                if root.right: queue.append(root.right)
            res.append(tmp)
        return res[::-1]


# @lc code=end
