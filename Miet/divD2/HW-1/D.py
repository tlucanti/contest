
def inp():
    return list(map(int, input().split()))

n = int(input()) + 1
k = sum(inp())
ans = 0
for i in range(1, 6):
    if (k + i - 1) % n != 0:
        ans += 1
print(ans)
