def inp():
    return list(map(int, input().split()))

def log2(n):
    ii = 1
    ans = 0
    while ii != n:
        ii *= 2
        ans += 1
    return ans

Dprint=lambda *a: a
#Dprint = print

for _ in range(int(input())):
    n = int(input())
    a = inp()
    ans = 0
    ok = True
    step = 1
    while step <= n//2:
        for j in range(0, n, 2 * step):
            Dprint ('--', a[j], a[j + step], j, j + step, step)
            if a[j] > a[j + step]:
                #Dprint('+')
                ans += 1
                a[j], a[j + step] = a[j + step], a[j]
            if a[j + step] - a[j] != step:
                ok = False
                break
        step *= 2
    #Dprint ('--', a[n//2], a[0])
    #if n > 1 and a[0] > a[n//2]:
    #    ans += 1
    #    if abs(a[n//2] - a[0]) != n // 2:
    #        ok = False
    if ok:
        print(ans)
    else:
        print(-1)
