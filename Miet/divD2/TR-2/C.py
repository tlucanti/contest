
def inp():
    return list(map(int, input().split()))

n = int(input())
ans = int(1e9)
for i in range(n):
    a, b = inp()
    ans = min(ans, a + b)
print(ans)
