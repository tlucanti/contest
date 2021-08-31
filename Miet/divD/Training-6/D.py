
def dfs(y, x):
    global cnt

    matr[y][x] = 2
    if y > 0:
        if matr[y - 1][x] == 0:
            dfs(y - 1, x)
        elif matr[y - 1][x] == 1:
            cnt += 1
    if y + 1 < h:
        if matr[y + 1][x] == 0:
            dfs(y + 1, x)
        elif matr[y + 1][x] == 1:
            cnt += 1
    if x > 0:
        if matr[y][x - 1] == 0:
            dfs(y, x - 1)
        elif matr[y][x - 1] == 1:
            cnt += 1
    if x + 1 < w:
        if matr[y][x + 1] == 0:
            dfs(y, x + 1)
        elif matr[y][x + 1] == 1:
            cnt += 1


h, w, k = map(int, input().split())
matr_or = [list(map(lambda x: int(x == '*'), input())) for _ in range(h)]
for i in range(k):
    matr = [matr_or[_][:] for _ in range(len(matr_or))]
    yy, xx = map(int, input().split())
    cnt = 0
    dfs(yy - 1, xx - 1)
    matr.clear()
    print(cnt)
