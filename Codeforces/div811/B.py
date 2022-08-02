
def inp():
    return list(map(int, input().split()))


for _ in range(int(input())):
    n = int(input())
    a = inp()
    d = dict()
    for i in a:
        d[i] = d.get(i, 0) + 1
    remaining = 0
    for i in d.values():
        if i > 1:
            remaining += 1
    ans = 0
    for i in a:
        if remaining == 0:
            break
        if d[i] == 2:
            d[i] -= 1
            remaining -= 1
        if d[i] > 1:
            d[i] -= 1
        ans += 1
    print(ans)

