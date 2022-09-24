
def inp():
    return [int(i) for i in input().split()]

for _ in range(int(input())):
    n, k = inp()
    a = inp()
    ans = 0
    for i in range(k):
        ans += max(a[i] for i in range(i, n, k))
    print(ans)

