
def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = inp()
    mn = min(a)
    ans = 0
    for i in range(n):
        ans += a[i] // (mn * 2 - 1) - 1 + (a[i] % (mn * 2 - 1) != 0)

    print(ans)

