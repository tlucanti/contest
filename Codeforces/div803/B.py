
def inp():
    return list(map(int, input().split()))


for _ in range(int(input())):
    n, k = inp()
    a = inp()
    if k == 1:
        if n % 2 == 0:
            n -= 1
        print(n // 2)
    else:
        ans = 0
        for i in range(1, n - 1):
            if a[i] > a[i - 1] + a[i + 1]:
                ans += 1
        print(ans)

