from collections import defaultdict


class Solution:

    def p3388(self):
        # n, m = map(int, input().split())
        # adj = defaultdict(list)
        # for _ in range(m):
        #     x, y = map(int, input().split())
        #     adj[x - 1].append(y - 1)
        #     adj[y - 1].append(x - 1)

        n, m = 7, 8
        adj = {0: [1, 2, 3], 1: [0, 4], 2: [0, 4], 3: [0, 4], 4: [1, 2, 3, 5], 5: [4, 6], 6:[5]}

        dfn = [0] * n
        low = [0] * n
        time = 0
        ans = [0] * n

        def tarjan(x, fa):
            nonlocal time
            time += 1
            dfn[x] = low[x] = time
            child = 0
            for y in adj[x]:
                if y == fa: continue
                if not dfn[y]:
                    tarjan(y, x)
                    low[x] = min(low[x], low[y])
                    if dfn[x] <= low[y]:
                        child += 1
                        if fa != -1 or child > 1:
                            ans[x] = 1
                else:
                    low[x] = min(low[x], dfn[y])
        for i in range(n):
            if not dfn[i]:
                tarjan(i, -1)

        print(sum(ans))
        print(' '.join(map(str, (i + 1 for i, x in enumerate(ans) if x))))


s = Solution()
s.p3388()