
def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = inp()
    m = int(input())
    b = inp()
    ans = 0
    cur = 0
    dp1 = [0] * max(n, m)
    dp2 = [0] * max(n, m)
    fora = [0] * (n + 1)
    forb = [0] * (m + 1)
    baca = [0] * (n + 1)
    bacb = [0] * (m + 1)

    fora[1] = a[0]
    forb[1] = b[0]
    baca[-2] = a[-1]
    bacb[-2] = b[-1]
    for i in range(1, n):
        fora[i + 1] = fora[i] + a[i]
    for i in range(1, m):
        forb[i + 1] = forb[i] + b[i]
    for i in range(n - 2, -1, -1):
        #print('--', baca)
        baca[i] = baca[i + 1] + a[i]
    for i in range(m - 2, -1, -1):
        bacb[i] = bacb[i + 1] + b[i]

    ans = 0
    #print(fora)
    #print(forb)
    #print(baca)
    #print(bacb)
    for i in range(n + 1):
        for j in range(m + 1):
            aa = fora[i] + forb[j]
            ans = max(aa, ans)
            ans = max(ans, aa + baca[i])
            ans = max(ans, aa + bacb[j])
            ans = max(ans, aa + baca[i] + bacb[j])
    print(ans)
    continue

    dp1[0] = a[0]
    dp2[0] = b[0]

    for i in range(1, max(m, n)):
        d = max(dp1[i - 1], dp2[i - 1])
        if i < n:
            dp1[i] = d + a[i]
        else:
            dp1[i] = d

        if i < m:
            dp2[i] = d + b[i]
        else:
            dp2[i] = d
    print(max(dp1[-1], dp2[-1]))
    print(dp1)
    print(dp2)
    continue


    while i < n or j < m:
        if i < n and j < m:
            if a[i] > b[j]:
                c = a[i]
                i += 1
            else:
                c = b[j]
                j += 1
            cur += c
        elif i < n:
            cur += a[i]
            i += 1
        else:
            cur += b[j]
            j += 1
        ans = max(ans, cur)
    print(ans)
