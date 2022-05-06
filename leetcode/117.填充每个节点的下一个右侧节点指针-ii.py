#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        deque = [root]
        while deque:
            sz = len(deque)
            for _ in range(sz):
                node = deque.pop(0)
                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)
            for i in range(len(deque) - 1):
                deque[i].next = deque[i + 1]
        return root
        
# @lc code=end

