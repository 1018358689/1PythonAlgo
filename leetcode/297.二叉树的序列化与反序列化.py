#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:
    def serialize(self, root: TreeNode):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = ''

        def dfs(node: TreeNode):
            nonlocal res
            if node is None:
                res += '#,'
                return

            res += str(node.val)+','
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return res

    def deserialize(self, data: str):
        deque = data.split(',')

        def dfs(deque):
            # BaseCase
            if not deque:
                return
            # BaseCase 递归
            value = deque.pop(0)
            if value == '#':
                return None
            root = TreeNode(int(value))
            root.left = dfs(deque)
            root.right = dfs(deque)
            # 回溯
            return root

        return dfs(deque)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

