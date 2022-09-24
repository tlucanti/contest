
def inp():
    return list(map(int, input().split()))


n, m = inp()
a = inp()
a.sort()
quart = sum(a) // 4

ans = 1
for i in range(1, n + 1):
    ans *= m * i


print(ans)