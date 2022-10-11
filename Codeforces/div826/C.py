
def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = inp()
    ans = n
    for i in range(1, n + 1):
        sm = sum(a[:i])
        ln = 0
        ln_cur = 0
        cur = 0
        ok = True
        #print ('-----', i)
        for j in range(n):
            #print(a[j], j, cur, ln)
            if cur + a[j] == sm:
                ln += 1
                ln_cur = max(ln_cur, ln)
                cur = 0
                ln = 0
            elif cur + a[j] < sm:
                cur += a[j]
                ln += 1
                ln_cur = max(ln_cur, ln)
            else:
                ok = False
                break
        if cur != 0 or ln > i:
            ok = False
        if ok:
            ans = min(ans, ln_cur)
    print(ans)
