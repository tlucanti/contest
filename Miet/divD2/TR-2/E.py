
def inp():
    return list(map(int, input().split()))

n = int(input())
a = []
for i in range(n):
    a.append(inp())

a.sort(key=lambda x: x[1])
ans = 0
maxr = 0
for i in range(n):
    if a[i][0] > maxr:
        ans += 1
        maxr = a[i][1]
print(ans)

