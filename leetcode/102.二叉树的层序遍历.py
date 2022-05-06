#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        deepth = 0

        def dfs(root, deepth):
            if root == None:
                return
            if len(res) == deepth:
                res.append([])
            res[deepth].append(root.val)
            dfs(root.left, deepth + 1)
            dfs(root.right, deepth + 1)

        dfs(root, deepth)
        return res


# @lc code=end
