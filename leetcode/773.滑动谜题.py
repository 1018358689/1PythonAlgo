#
# @lc app=leetcode.cn id=773 lang=python3
#
# [773] 滑动谜题
#

# @lc code=start
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = board[0] + board[1]
        index_neighbor = {0: (1, 3), 1: (0, 2, 4), 2: (1, 5), 3: (0, 4), 4: (1, 3, 5), 5: (2, 4)}
        target = [1, 2, 3, 4, 5, 0]
        visited = set()
        visited.add(tuple(start))
        queue = deque([start])
        res = 0
        while queue:
            sz = len(queue)
            # 将该层进行扩散
            for _ in range(sz):
                cur = queue.popleft()
                if cur == target:
                    return res
                zero = cur.index(0)
                for neighbor in index_neighbor[zero]:
                    tmp = cur[:]
                    tmp[zero], tmp[neighbor] = tmp[neighbor], tmp[zero]
                    if tuple(tmp) not in visited:
                        visited.add(tuple(tmp))
                        queue.append(tmp)
            res += 1 # 扩散完 次数+1
        return -1
# @lc code=end

