
t = int(input())
for i in range(t):
    n, x = input().split()
    x, n = int(x), int(n)

    if n <= 2:
        print(1)
    else:
        print((n - 3) // x + 2)
