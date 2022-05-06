#
# @lc app=leetcode.cn id=652 lang=python3
#
# [652] 寻找重复的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        mem = defaultdict(int)
        res = []

        def dfs(node: TreeNode):  # 输出该节点的序列化形式
            if not node:
                return '#'
            left = dfs(node.left)
            right = dfs(node.right)
            sub_tree = str(left) + ',' + str(right) + ',' + str(node.val)
            mem[sub_tree] += 1
            if mem[sub_tree]==2:
                res.append(node)
            return sub_tree

        dfs(root)
        return res
# @lc code=end

