#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0

        def dfs(node: TreeNode):
            hi_left = hi_right = 0
            tmp_l = tmp_r = node
            while tmp_l:
                tmp_l = tmp_l.left
                hi_left += 1
            while tmp_r:
                tmp_r = tmp_r.right
                hi_right += 1
            if hi_left == hi_right:  # 如果左右子树的高度相同，则是一棵满二叉树
                return 2**hi_left - 1
            # 如果左右高度不同，则按照普通二叉树的逻辑计算
            cnt_left = dfs(node.left)
            cnt_right = dfs(node.right)
            return 1 + cnt_left + cnt_right

        return dfs(root)


# @lc code=end
