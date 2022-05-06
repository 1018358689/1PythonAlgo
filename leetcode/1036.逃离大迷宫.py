#
# @lc app=leetcode.cn id=1036 lang=python3
#
# [1036] 逃离大迷宫
#

# @lc code=start
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if len(blocked) < 2:  # 1或0个阻碍很容易突破
            return True
        # 离散化 将图缩小
        rows = sorted(set(i[0] for i in blocked + [source] + [target]))  # 排序且去重
        cols = sorted(set(i[1] for i in blocked + [source] + [target]))
        r_map, c_map = {}, {}  # 创建原值和离散后的映射，以便将原值映射到新图
        # 对横坐标离散化
        r = 0 if rows[0] == 0 else 1  # r表示索引 初始状态，如果初始贴边，离散也贴边，初始不贴边，离散就在离边最近的1位置
        r_map[rows[0]] = r
        for i in range(1, len(rows)):
            step = 1 if rows[i] == rows[i - 1] + 1 else 2  # 和前面比较，相同的已经去重去过了，如果隔壁(差1)那就离散也隔壁(差1)，否则差2
            r += step  # 往前走步数
            r_map[rows[i]] = r
        sz_row = r + 1 if rows[-1] == 10**6 - 1 else r + 2  # 新图大小，如果最大值贴边(索引10**6 - 1)，那么新图也和离散最大值贴边，那么新图大小r+1，否则r+2
        # 同理对纵坐标离散化
        c = 0 if cols[0] == 0 else 1
        c_map[cols[0]] = c
        for i in range(1, len(cols)):
            step = 1 if cols[i] == cols[i - 1] + 1 else 2
            c += step
            c_map[cols[i]] = c
        sz_col = c + 1 if cols[-1] == 10**6 - 1 else c + 2

        grid = [[0] * sz_col for _ in range(sz_row)]  # 创建新图
        for r, c in blocked + [source]:  # 初始化不能走的位置
            grid[r_map[r]][c_map[c]] = 1
        # pprint(grid)
        sr, sc = r_map[source[0]], c_map[source[1]]  # 初始位置
        er, ec = r_map[target[0]], c_map[target[1]]  # 结束位置
        # 启动广度优先遍历
        queue = deque([(sr, sc)])
        while queue:
            sz = len(queue)
            for _ in range(sz):
                r, c = queue.popleft()
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if 0 <= nr < sz_row and 0 <= nc < sz_col and grid[nr][nc] != 1:
                        if nr == er and nc == ec:  # 一旦找到就推出
                            return True
                        grid[nr][nc] = 1
                        queue.append((nr, nc))
        return False  # 无法走出包围圈
# @lc code=end

