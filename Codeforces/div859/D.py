
def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n, q = inp()
    a = inp()
    pref = [0] * n
    suff = [0] * n

    pref[0] = a[0]
    for i in range(1, n):
        pref[i] = pref[i - 1] + a[i]

    suff[-1] = a[-1]
    for i in range(n - 2, -1, -1):
        suff[i] = suff[i + 1] + a[i]

    for i in range(q):
        l, r, k = inp()
        l -= 1
        r -= 1
        if l == 0:
            L = 0
        else:
            L = pref[l - 1]
        if r == n - 1:
            R = 0
        else:
            R = suff[r + 1]

        ans = L + R + k * (r - l + 1)
        if ans % 2 == 0:
            print('NO')
        else:
            print('YES')

