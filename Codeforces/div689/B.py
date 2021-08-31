
def check(s, y, x, h, w, num):
    x = x + num - 1
    for i in range(num):
        yy = y - num + i + 1
        xx = x + i
        if yy >= h or xx >= w or s[yy][xx] == 0:
            return 0
        if i != 0:
            if s[yy][xx - 1] == 0:
                return 0
    for i in range(num):
        yy = y - num + i + 1
        xx = x + i
        s[yy][xx] = 0
        if i != 0:
            s[yy][xx - 1] = 0
    return 1


def ss(nn):
    return (nn * (nn + 1) * (2 * nn + 1)) // 6


for t in range(int(input())):
    n, m = map(int, input().split())
    st = [list(map(lambda x: int(x == '*'), input())) for _ in range(n)]
    ans = 0
    for i in range(n - 1, -1, -1):
        for j in range(m):
            if st[i][j]:
                if j + 1 < m and st[i][j + 1]:
                    v = 1         # y  x  h  w  num
                    while check(st, i, j, n, m, v + 1):
                        v += 1
                    ans += ss(v)
                else:
                    ans += 1
                    st[i][j] = 0
    print(ans)
