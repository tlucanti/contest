
def inp():
    return list(map(int, input().split()))


for _ in range(int(input())):
    n, x = inp()
    a = inp()
    a.sort()
    ok = True
    for i in range(n):
        if a[i] + x > a[n + i]:
            ok = False
            break
    if ok:
        print('YES')
    else:
        print('NO')
