#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.

# 经典问题了，先给出递归函数的定义：给该函数输入三个参数 root，p，q，它会返回一个节点：
# 情况 1，如果 p 和 q 都在以 root 为根的树中，函数返回的即使 p 和 q 的最近公共祖先节点。
# 情况 2，那如果 p 和 q 都不在以 root 为根的树中怎么办呢？函数理所当然地返回 null 呗。
# 情况 3，那如果 p 和 q 只有一个存在于 root 为根的树中呢？函数就会返回那个节点。
# 根据这个定义，分情况讨论：
# 情况 1，如果 p 和 q 都在以 root 为根的树中，那么 left 和 right 一定分别是 p 和 q（从 base case 看出来的）。
# 情况 2，如果 p 和 q 都不在以 root 为根的树中，直接返回 null。
# 情况 3，如果 p 和 q 只有一个存在于 root 为根的树中，函数返回该节点。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node: TreeNode):
            # BaseCase (递归)
            if node is None:
                return None
            if node == p or node == q:
                return node
            # 前序位置 (递归)
            left = dfs(node.left) # 回溯前会返回None或node
            right = dfs(node.right) # 回溯会带着p或q或node或None
            # 后序 (回溯)
            if left and right:  # 都存在 最后必然会发生
                return node
            elif left is None and right is None:  # 都不存在
                return None
            elif left and right is None:  # 存在左
                return left
            else:  # 存在右
                return right

        return dfs(root)
# @lc code=end

