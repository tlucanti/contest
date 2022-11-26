
from collections import Counter

def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = Counter(inp())
    a = list(a.items())
    if len(a) == 1:
        print(a[0][1] // 2)
        continue
    elif len(a) == 2:
        print(a[0][1] * a[1][1])
        continue
    a.sort(key=lambda x: x[0])
    n = len(a)
    sfront = [0] * n
    sfront[0] = a[0][1]
    for i in range(1, n):
        sfront[i] = sfront[i - 1] + a[i][1]

    sback = [0] * n
    sback[-1] = a[-1][1]
    for i in range(n - 2, -1, -1):
        sback[i] = sback[i + 1] + a[i][1]


    ans = 0
    #print(a)
    #print(sfront)
    #print(sback)
    for i in range(n - 1):
        aa = sfront[i] * sback[i + 1]
        ans = max(aa, ans)
    print(ans)


