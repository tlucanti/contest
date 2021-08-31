
def check(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):# or 9 - x1 + x2 == y1 - y2:
        return 1
    return 0


ans = 0
n = 8
f = [list(map(int, input().split())) for i in range(n)]
for i in range(n - 1):
    for j in range(i + 1, n):
        ans += check(f[i][0], f[i][1], f[j][0], f[j][1])

print("YES" if ans else "NO")
