#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        queue = [root]
        while queue:
            res.append(queue[-1].val)
            tmp = []
            for root in queue:
                if root.left: tmp.append(root.left)
                if root.right: tmp.append(root.right)
            queue = tmp
        return res
# @lc code=end

