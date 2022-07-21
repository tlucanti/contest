
def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = inp()
    if sum(a[1:]) == 0:
        print('YES')
        continue
    prev = list(a)
    while True:
        ok = True
        for i in range(n - 1, 0, -1):
            if a[i - 1] > a[i]:
                continue
            else:
                n = a[i] // a[i-1]
                a[i] -= n * a[i-1]
        if sum(a[1:]) == 0:
            break
        elif prev == a:
            ok = False
            break

    if ok:
        print('YES')
    else:
        print('NO')
