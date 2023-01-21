
def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n, k = inp()
    a = inp()
    idx = [0] * (n + 1)
    for i in range(n):
        idx[a[i]] = i

    ans = 0
    cur = 0
    last = n
    for i in range(1, n):
        if idx[i] > idx[i + 1]:
            idx[i + 1] = last
            last += 1
            cur += 1
        if cur == k:
            ans += 1
            cur = 0
    if cur != 0:
        ans += 1
    print(ans)

