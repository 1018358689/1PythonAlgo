#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# https://leetcode-cn.com/problems/add-two-numbers/solution/2-liang-shu-xiang-jia-python-lian-biao-b-xsy6/
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = curr = ListNode()
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            add = x + y + carry
            curr.next = ListNode(add % 10)
            carry = add // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            curr = curr.next
        if carry:
            curr.next = ListNode(carry)
        return dummy.next


# @lc code=end
