
def inp():
    return list(map(int, input().split()))


for _ in range(int(input())):
    n, m = inp()
    a = inp()
    a.sort()
    d = [a[i] - a[i - 1] - 1 for i in range(1, m)]
    d.append(a[0] + (n - a[-1]) - 1)
    # print(d)
    d.sort(reverse=True)
    ans = 0
    turn = 0
    for i in range(m):
        add = min(d[i], turn * 2)
        ans += add
        d[i] -= add
        if d[i] == 0:
            continue
        if d[i] == 1:
            turn += 1
            continue
        elif d[i] == 2:
            turn += 1
            ans += 1
            continue
        turn += 2
        ans += 1
    print(ans + m)
