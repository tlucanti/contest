
def inp():
    return list(map(int, input().split()))


for _ in range(int(input())):
    n = int(input())
    d = list(zip(inp(), inp()))
    d.sort(key=lambda x: x[0] - x[1])
    le = 0
    ri = n - 1
    ans = 0
    while le < ri:
        if d[le][0] + d[ri][0] <= d[le][1] + d[ri][1]:
            ans += 1
            le += 1
            ri -= 1
        else:
            ri -= 1
    print(ans)

