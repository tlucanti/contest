import sys
sys.setrecursionlimit(1000000)


def dfs(d, x, y):
    an = 0
    fx = d.get((x + 1, y), 0)
    fy = d.get((x, y + 1), 0)
    if fx == 0 and fy == 0:
        d[(x, y)] = 1
        return 1
    if fx:
        if fx == -1:
            an += dfs(d, x + 1, y)
        else:
            an += fx
    if fy:
        if fy == -1:
            an += dfs(d, x, y + 1)
        else:
            an += fy
    d[(x, y)] = an
    return an % 1000000007


n = int(input())
ans = 0
d = dict()
for i in range(n):
    x, y = input().split()
    x, y = int(x), int(y)
    d[(x, y)] = -1
print(dfs(d, 1, 1))
