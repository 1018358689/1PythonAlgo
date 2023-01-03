def dfs(n):
    res = []
    for x in range(2, n + 1):
        if not n % x:
            res.append(x)
            res += dfs(n // x)
            break
    return res


print(dfs(99))