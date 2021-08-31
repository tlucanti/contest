def dfs(y, x):
    matr[y][x] = 1
    if y > 0 and v[x] == '^':
        if matr[y - 1][x] == 0:
            dfs(y - 1, x)
    if y + 1 < h and v[x] == 'v':
        if matr[y + 1][x] == 0:
            dfs(y + 1, x)
    if x > 0 and g[y] == '<':
        if matr[y][x - 1] == 0:
            dfs(y, x - 1)
    if x + 1 < w and g[y] == '>':
        if matr[y][x + 1] == 0:
            dfs(y, x + 1)


h, w = map(int, input().split())
g = input()
v = input()
f = True
for yy in range(h):
    for xx in range(w):
        matr = [[0 for _ in range(w)] for __ in range(h)]  # 0 - not visited, 1 - pending, 2 - ended
        dfs(yy, xx)
        if sum(list(map(sum, matr))) < h * w:
            f = False
print('YES' if f else 'NO')
