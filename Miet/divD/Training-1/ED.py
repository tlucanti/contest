
nn, x, y = input().split()
nn, x, y = int(nn), int(x), int(y)

n = nn // 2
if (x == n or x == n + 1) and (y == n or y == n + 1):
    print("NO")
else:
    print("YES")
