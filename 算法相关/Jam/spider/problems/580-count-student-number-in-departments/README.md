# [Count Student Number in Departments][title]

## Description

表: `Student`
            +--------------+---------+    | Column Name  | Type    |    +--------------+---------+    | student_id   | int     |    | student_name | varchar |    | gender       | varchar |    | dept_id      | int     |    +--------------+---------+    Student_id是该表的主键。    dept_id是Department表中dept_id的外键。    该表的每一行都表示学生的姓名、性别和所属系的id。    



表: `Department`
            +-------------+---------+    | Column Name | Type    |    +-------------+---------+    | dept_id     | int     |    | dept_name   | varchar |    +-------------+---------+    Dept_id是该表的主键。    该表的每一行包含一个部门的id和名称。



编写一个SQL查询，为 `Department` 表中的所有部门(甚至是没有当前学生的部门)报告各自的部门名称和每个部门的学生人数。

按 `student_number` **降序  **返回结果表。如果是平局，则按 `dept_name` 的  **字母顺序  **排序。

查询结果格式如下所示。



**示例 1:**
            **输入:**     Student 表:    +------------+--------------+--------+---------+    | student_id | student_name | gender | dept_id |    +------------+--------------+--------+---------+    | 1          | Jack         | M      | 1       |    | 2          | Jane         | F      | 1       |    | 3          | Mark         | M      | 2       |    +------------+--------------+--------+---------+    Department 表:    +---------+-------------+    | dept_id | dept_name   |    +---------+-------------+    | 1       | Engineering |    | 2       | Science     |    | 3       | Law         |    +---------+-------------+    **输出:**     +-------------+----------------+    | dept_name   | student_number |    +-------------+----------------+    | Engineering | 2              |    | Science     | 1              |    | Law         | 0              |    +-------------+----------------+


**Tags:** Database

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/count-student-number-in-departments
