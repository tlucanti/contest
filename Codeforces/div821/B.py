
def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n, x, y = inp()
    if x * y != 0:
        print(-1)
        continue
    x = max(x, y)
    if x == 0 or (n - 1) % x != 0:
        print(-1)
        continue
    i = 1
    while i < n:
        for j in range(x):
            print(i + 1, end=' ')
        i += x
    print()

