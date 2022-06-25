
def inp():
    return list(map(int, input().split()))


def mm_gen(a):
    n = len(a)
    mx = [0] * n
    mn = [0] * n

    m = a[0]
    mi = 0
    cnt = 1
    for i in range(1, n):
        if a[i] < m:
            cnt += 1
        else:
            for j in range(cnt):
                mx[mi + j] = j
            mi = i
            cnt = 1
            m = a[i]
    for j in range(cnt):
        mx[mi + j] = j

    m = a[-1]
    mi = n - 1
    cnt = 1
    for i in range(n - 1, -1, -1):
        if a[i] > m:
            cnt += 1
        else:
            for j in range(cnt):
                mn[mi - j] = j
            mi = i
            cnt = 1
            m = a[i]
    for j in range(cnt):
        mn[mi - j] = j
    return mx, mn


def solve(a):
    n = len(a)

    mx1, mn1 = mm_gen(a)
    mx2, mn2 = mm_gen(a[::-1])
    mx2 = mx2[::-1]
    mn2 = mn2[::-1]

    ans = 0
    i = 0
    while i < n - 1:
        if mx1[i] == 0:
            if mx1[i + mn1[i]] == mn1[i] and mn1[i] != 0:
                i += mn1[i]
                ans += 1
                continue
        if mn2[i] == 0:
            if mn2[i + mx2[i]] == mx2[i] and mx2[i] != 0:
                i += mx2[i]
                ans += 1
                continue
        if mn2[i + mx2[i]] - mn2[i] == mx2[i] and mx2[i] != 0:
            i += mx2[i]
            ans += 1
            continue
        if mx1[i + mn1[i]] - mx1[i] == mn1[i] and mn1[i] != 0:
            i += mn1[i]
            ans += 1
            continue
        i += 1
        ans += 1
    return ans


for _t in range(int(input())):
    n = int(input())
    a = inp()
    if len(a) == 1:
        print(0)
        continue
    # print(solve(a))
    print(min(solve(a), solve(a[::-1])))
