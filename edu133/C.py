
def inp():
    return list(map(int, input().split()))


def count(xx, yy, a):
    xxx = xx
    for xx in range(xxx + 1, n):
        a = max(a, m[yy][xx]) + 1
    yy = 1 - yy
    for xx in range(n - 1, xxx - 1, -1):
        a = max(a, m[yy][xx]) + 1
    return a


for _ in range(int(input())):
    n = int(input())
    m = [inp(), inp()]
    x = 0
    y = 0
    mx = [[0] * n, [0] * n]
    mx[0][-1] = m[0][-1]
    mx[1][-1] = m[1][-1]
    for i in range(n - 2, -1, -1):
        mx[0][i] = max(mx[0][i + 1], m[0][i])
        mx[1][i] = max(mx[1][i + 1], m[1][i])
    ans = 0
    cnt = False
    while x < n - 2:
        if y == 0:
            if mx[0][x + 1] < mx[1][x]:
                ans += count(x, y, ans)
                cnt = True
                break
            else:
                ans = max(ans, m[1][x]) + 1
                ans = max(ans, m[0][x + 1]) + 1
        else:
            if mx[1][x + 1] < mx[0][x]:
                ans += count(x, y, ans)
                cnt = True
                break
            else:
                ans = max(ans, m[0][x]) + 1
                ans = max(ans, m[1][x + 1]) + 1
        x += 1
    if not cnt:
        if y == 0:
            ans = max(ans, m[1][-1]) + 1
        else:
            ans = max(ans, m[0][-1]) + 1
    print(ans)
