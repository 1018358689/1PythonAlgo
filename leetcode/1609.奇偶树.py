from typing import Optional
#
# @lc app=leetcode.cn id=1609 lang=python3
#
# [1609] 奇偶树
#

# @lc code=start
# Definition for a binary tree node.
import collections


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = collections.deque([(root, True)])  # True表示偶数层 False表示奇数层
        while q:
            pre = 0
            for _ in range(len(q)):
                cur, sig = q.popleft()
                if (not cur.val % 2) is sig:
                    return False
                if pre > 0 and ((sig and pre >= cur.val) or (not sig and pre <= cur.val)):
                    return False
                pre = cur.val
                if cur.left: q.append((cur.left, not sig))
                if cur.right: q.append((cur.right, not sig))
        return True


# @lc code=end
