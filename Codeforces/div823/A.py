
def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n, c = inp()
    a = inp()
    d = dict()
    ans = 0
    for i in a:
        d[i] = d.get(i, 0) + 1
    for i in d:
        if d[i] > c:
            ans += c
        else:
            ans += d[i]
    print(ans)

