def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = sorted(inp())
    ans = 1
    if a[0] != 0:
        ans += 1
    for i in range(n - 1):
        if i + 1 < a[i + 1] and i >= a[i]:
            ans += 1
    print(ans)
