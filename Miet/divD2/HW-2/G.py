
import math as m

def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = inp()
    sm2 = 2 * sum(a)
    if sm2 % n != 0:
        print(0)
        continue
    sm2 = sm2 // n
    d = dict()
    for i in a:
        d[i] = d.get(i, 0) + 1
    ans = 0
    for a1 in d:
        a2 = sm2 - a1
        if a1 == a2:
            ans += m.comb(d[a1], 2) * 2
        else:
            ans += d[a1] * d.get(a2, 0)
    print(ans // 2)
