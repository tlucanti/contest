
t = int(input())
for i in range(t):
    x, y, a, b = map(int, input().split())
    if (y - x) % (a + b) != 0:
        print(-1)
    else:
        print((y - x) // (a + b))
