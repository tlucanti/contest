
import math as m

def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = inp()
    s = dict()
    b = []
    for i in range(n):
        if a[i] not in s:
            b.append(a[i])
        s[a[i]] = i + 1

    ans = -1
    ii, jj = 0, 0
    for i in range(len(b)):
        for j in range(i, len(b)):
            #print(i, j, b[i], b[j], m.gcd(i, j))
            if m.gcd(b[i], b[j]) == 1:
                ii = s[b[i]]
                jj = s[b[j]]
                if ii + jj > ans:
                    ans = ii + jj
    print(ans)
