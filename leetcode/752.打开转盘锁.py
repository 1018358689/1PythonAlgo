#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#


# @lc code=start
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        cnt = 0
        q1 = set()
        q1.add('0000')
        q2 = set()
        q2.add(target)
        visited = set()
        deadends = set(deadends)

        def up(content, index):
            tmp = list(map(int, list(content)))
            tmp[index] = (tmp[index] + 1) % 10
            tmp = map(str, tmp)
            return ''.join(tmp)

        def down(content, index):
            tmp = list(map(int, list(content)))
            tmp[index] = (tmp[index] - 1) % 10
            tmp = map(str, tmp)
            return ''.join(tmp)

        while q1 and q2:
            if len(q1) > len(q2):
                q1, q2 = q2, q1
            tmp_q = set()
            for root in q1:
                if root in deadends:
                    continue
                if root in q2:
                    return cnt
                visited.add(root)
                for i in range(4):
                    tmp = up(root, i)
                    if tmp not in visited:
                        tmp_q.add(tmp)
                    tmp = down(root, i)
                    if tmp not in visited:
                        tmp_q.add(tmp)

            cnt += 1
            q1 = q2
            q2 = tmp_q
        return -1


# @lc code=end
