# [Delete N Nodes After M Nodes of a Linked List][title]

## Description

给定链表 `head` 和两个整数 `m` 和 `n`. 遍历该链表并按照如下方式删除节点:

  * 开始时以头节点作为当前节点.
  * 保留以当前节点开始的前 `m` 个节点.
  * 删除接下来的 `n` 个节点.
  * 重复步骤 2 和 3, 直到到达链表结尾.

在删除了指定结点之后, 返回修改过后的链表的头节点.



**示例 1:**

**![](https://assets.leetcode.com/uploads/2020/06/06/sample_1_1848.png)**
            **输入:** head = [1,2,3,4,5,6,7,8,9,10,11,12,13], m = 2, n = 3    **输出:** [1,2,6,7,11,12]    **解析:** 保留前(m = 2)个结点,  也就是以黑色节点表示的从链表头结点开始的结点(1 ->2).    删除接下来的(n = 3)个结点(3 -> 4 -> 5), 在图中以红色结点表示.    继续相同的操作, 直到链表的末尾.    返回删除结点之后的链表的头结点.

**示例 2:**

**![](https://assets.leetcode.com/uploads/2020/06/06/sample_2_1848.png)**
            **输入:** head = [1,2,3,4,5,6,7,8,9,10,11], m = 1, n = 3    **输出:** [1,5,9]    **解析:** 返回删除结点之后的链表的头结点.

**示例 3:**
            **输入:** head = [1,2,3,4,5,6,7,8,9,10,11], m = 3, n = 1    **输出:** [1,2,3,5,6,7,9,10,11]    

**示例  4:**
            **输入:** head = [9,3,7,7,9,10,8,2], m = 1, n = 2    **输出:** [9,7,8]    



**提示:**

  * 链表中节点数目在范围 `[1, 104]` 内
  * `1 <= Node.val <= 106`
  * `1 <= m, n <= 1000`



**进阶:** 你能通过 **就地** 修改链表的方式解决这个问题吗?


**Tags:** Linked List

**Difficulty:** Easy

## 思路

[title]: https://leetcode-cn.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list
