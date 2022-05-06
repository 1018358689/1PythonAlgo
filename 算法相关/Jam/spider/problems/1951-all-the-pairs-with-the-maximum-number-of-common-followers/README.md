# [All the Pairs With the Maximum Number of Common Followers][title]

## Description

表: `Relations`
            +-------------+------+    | Column Name | Type |    +-------------+------+    | user_id     | int  |    | follower_id | int  |    +-------------+------+    (user_id, follower_id) 是这个表的主键.    这个表的每一行，表示这个user_id的用户和他的关注者，关注者的id 就是本表的 user_id.    



写出一个查询语句，找到具有最多共同关注者的所有两两结对组。换句话说，如果有两个用户的共同关注者是最大的，我们应该返回所有具有此最大值的两两结对组

The result table should contain the pairs `user1_id` and `user2_id` where
`user1_id < user2_id`.

结果返回表，每一行应该包含`user1_id`和 `user2_id，`其中`user1_id < user2_id`.

返回结果  **不要求顺序**  。

查询结果格式如下例：


            Relations 表:    +---------+-------------+    | user_id | follower_id |    +---------+-------------+    | 1       | 3           |    | 2       | 3           |    | 7       | 3           |    | 1       | 4           |    | 2       | 4           |    | 7       | 4           |    | 1       | 5           |    | 2       | 6           |    | 7       | 5           |    +---------+-------------+        Result 表:    +----------+----------+    | user1_id | user2_id |    +----------+----------+    | 1        | 7        |    +----------+----------+        用户1 和用户 2 有2个共同的关注者（3和4）。    用户1 和用户 7 有3个共同的关注者（3，4和5）。    用户2 和用户7 有2个共同的关注者（3和4）。    既然两两结对的所有组队的最大共同关注者的数值是3，所以，我们应该返回所有拥有3个共同关注者的两两组队，这就是仅有的一对(1, 7).    我们返回的是(1, 7).，而不是(7, 1).    注意，我们没有关于用户3，4，5的任何关注者信息，我们认为他们有0个关注者。    


**Tags:** Database

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/all-the-pairs-with-the-maximum-number-of-common-followers
