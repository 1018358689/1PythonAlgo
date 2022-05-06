def f(expression: str):

    def dfs(l, r):  # expression [l,r] 的所有可能结果
        if l == r:
            return [int(expression[l])]
        res = []
        for i, op in enumerate(expression):
            if l <= i < r:
                if op in {'+', '-', '*'}:
                    leftRes = dfs(l, i - 1)
                    rightRes = dfs(i + 1, r)
                    # print(leftRes, rightRes)
                    for left in leftRes:
                        for right in rightRes:
                            res.append(eval(f'{left}{op}{right}'))
        return res

    return dfs(0, len(expression) - 1)


print(f('2-1-1'))