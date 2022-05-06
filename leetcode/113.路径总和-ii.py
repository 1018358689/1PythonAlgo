#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        res = []
        path = [root.val]

        def dfs(node: TreeNode, path: list):
            if node.left is None and node.right is None:
                if sum(path) == targetSum:
                    res.append(path[:])
                return
            for n in [node.left, node.right]:
                if n:
                    path.append(n.val)
                    dfs(n, path)
                    path.pop()

        dfs(root, path)
        return res


# @lc code=end
