
def inp():
    return list(map(int, input().split()))


for _ in range(int(input())):
    m, n, k = inp()
    a = inp()
    a2 = list(a)
    if sum(a) < m * n:
        print('NO')
        continue
    ok = False
    ki = 0
    ni = 0
    pos1 = False
    pos2 = False
    if n % 2:
        for i in range(k):
            add = a[i] // m
            if add >= 3:
                ni += 3
                pos1 = True
                a[i] -= m * 3
                break
    else:
        pos1 = True
    if pos1:
        while True:
            if ki >= k:
                break
            add = a[ki] // m
            a[ki] -= add * m
            if add > 1:
                ni += add
            else:
                ki += 1
            if ni >= n:
                ok = True
                break
    if ok:
        print('YES')
        continue

    a = a2
    ki = 0
    del ni
    mi = 0
    if m % 2:
        for i in range(k):
            add = a[i] // n
            if add >= 3:
                mi += 3
                pos2 = True
                a[i] -= n * 3
                break
    else:
        pos2 = True
    if pos2:
        while True:
            if ki >= k:
                break
            add = a[ki] // n
            a[ki] -= add * n
            if add > 1:
                mi += add
            else:
                ki += 1
            if mi >= m:
                ok = True
                break

    if ok:
        print('YES')
    else:
        print('NO')
