
def rotate(x, y, n):
    return n - y - 1, x


for _ in range(int(input())):
    n = int(input())
    m = [list(map(int, input())) for _ in range(n)]
    ans = 0
    for _y in range(n):
        for _x in range(n):
            x, y = _x, _y
            r = list()
            r.append(m[y][x])
            x, y = rotate(x, y, n)
            r.append(m[y][x])
            x, y = rotate(x, y, n)
            r.append(m[y][x])
            x, y = rotate(x, y, n)
            r.append(m[y][x])
            z = r.count(0)
            # print(min(z, 4 - z))
            ans += min(z, 4 - z)
            # if z > 2:
            #     ans += 4 - z
            # else:
            #     ans += z
    print(ans // 4)
