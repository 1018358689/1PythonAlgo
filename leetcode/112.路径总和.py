#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        path = [root.val]
        signal = False

        def dfs(node: TreeNode):
            nonlocal signal
            if node.left is None and node.right is None:
                if sum(path) == targetSum:
                    signal = True
                return
            for n in [node.left, node.right]:
                if n: 
                    path.append(n.val)
                    dfs(n)
                    path.pop()

        dfs(root)
        return signal


# @lc code=end
