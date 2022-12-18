
def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    k, n = inp()
    gap = n - k
    next = 0
    ans = [0] * k
    ans[0] = 1
    i = 1
    while next <= gap and i < k:
        ans[i] = ans[i - 1] + next + 1
        gap -= next
        next += 1
        i += 1
    while i < k:
        ans[i] = ans[i - 1] + 1
        i += 1
    print(*ans)

